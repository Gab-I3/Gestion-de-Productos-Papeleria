class Product:
    def __init__(self, name, description, price, stock, category, brand, image_url):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category
        self.brand = brand
        self.image_url = image_url

    def toDBCollection(self):
        return {
            'name': self.name,
            'description': self.description,
            'price': float(self.price),
            'stock': int(self.stock),
            'category': self.category,
            'brand': self.brand,
            'image_url': self.image_url
        }
