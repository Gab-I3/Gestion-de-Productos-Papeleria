from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
import database as dbase
from product import Product

db = dbase.dbConnection()
app = Flask(__name__)

# Rutas de la aplicación
@app.route('/')
@app.route('/products')
def home():
    products_col = db['products']
    
    # Capturar filtros de la URL
    search_query = request.args.get('q')
    category_filter = request.args.get('category')
    brand_filter = request.args.get('brand')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')

    # Construir la consulta para MongoDB
    query = {}
    
    # Búsqueda por nombre
    if search_query:
        query['name'] = {'$regex': search_query, '$options': 'i'}
    
    # Filtro por categoría
    if category_filter:
        query['category'] = category_filter
    
    # Búsqueda por marca
    if brand_filter:
        query['brand'] = {'$regex': brand_filter, '$options': 'i'}

    # Filtro de rango de precio
    if min_price or max_price:
        price_query = {}
        if min_price: price_query['$gte'] = float(min_price)
        if max_price: price_query['$lte'] = float(max_price)
        query['price'] = price_query

    products_received = products_col.find(query)
    return render_template('index.html', products=products_received)

# 2. Vista Crear Producto
@app.route('/products/new', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        products_col = db['products']
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']
        category = request.form['category']
        brand = request.form['brand']
        image_url = request.form['image_url'] or "https://via.placeholder.com/150"

        if name and price and stock:
            product = Product(name, description, price, stock, category, brand, image_url)
            products_col.insert_one(product.toDBCollection())
            return redirect(url_for('home'))
            
    return render_template('create.html')

# 3. Vista Editar Producto
@app.route('/products/<string:id>/edit', methods=['GET', 'POST'])
def edit_product(id):
    products_col = db['products']
    
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']
        category = request.form['category']
        brand = request.form['brand']
        image_url = request.form['image_url']

        products_col.update_one({'_id': ObjectId(id)}, 
        {'$set': {
            'name': name, 
            'description': description, 
            'price': float(price), 
            'stock': int(stock), 
            'category': category, 
            'brand': brand,
            'image_url': image_url
        }})
        return redirect(url_for('home'))
        
    # Método GET: Cargar datos actuales
    product = products_col.find_one({'_id': ObjectId(id)})
    return render_template('edit.html', product=product)

# 4. Vista Eliminar
@app.route('/products/<string:id>/delete', methods=['GET', 'POST'])
def delete_product(id):
    products_col = db['products']
    if request.method == 'POST':
        products_col.delete_one({'_id': ObjectId(id)})
        return redirect(url_for('home'))
    
    product = products_col.find_one({'_id': ObjectId(id)})
    return render_template('delete.html', product=product)

@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=4000)
