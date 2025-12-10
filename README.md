# Gestión de Inventario de Papelería

Una aplicación web desarrollada con **Python (Flask)** y **MongoDB** para gestionar el inventario de productos de una papelería. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y filtrar productos por nombre, marca, categoría y precio.

## 🚀 Características

* **Listado de Productos:** Visualización de productos en tarjetas con imagen, precio y stock.
* **Filtrado Avanzado:** Búsqueda por nombre, marca, categoría y rango de precios.
* **Gestión de Inventario:**
    * Registrar nuevos productos.
    * Editar detalles de productos existentes.
    * Eliminar productos.
* **Imágenes:** Soporte para URLs de imágenes externas con imagen genérica automática si no se proporciona una.
* **Base de Datos:** Conexión persistente a MongoDB Atlas.

## 🛠️ Tecnologías Utilizadas

* **Python 3** - Lenguaje principal.
* **Flask** - Framework web.
* **MongoDB** - Base de datos NoSQL (usando MongoDB Atlas).
* **PyMongo** - Driver de MongoDB para Python.
* **Bootstrap 5** - Framework CSS para el diseño responsive.
* **Jinja2** - Motor de plantillas para HTML.

## 📋 Requisitos Previos

Asegúrate de tener instalado Python en tu sistema:

```bash
python --version

## ⚙️ Instalación y Configuración
Clonar o descargar el proyecto en tu carpeta de trabajo.

Crear un entorno virtual (opcional pero recomendado):

Bash

python -m venv venv

# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
Instalar dependencias: Ejecuta el siguiente comando para instalar las librerías necesarias:

Bash

pip install flask pymongo certifi
Configuración de la Base de Datos: El archivo database.py ya contiene una URI de conexión a un cluster de MongoDB Atlas. Nota: Para producción, se recomienda mover la MONGO_URI a variables de entorno para mayor seguridad.

▶️ Ejecución
Para iniciar la aplicación, ejecuta el archivo principal:

Bash

python app.py
Si todo es correcto, verás un mensaje indicando que el servidor está corriendo (usualmente en http://127.0.0.1:4000).

Abre tu navegador web y ve a: http://localhost:4000

📂 Estructura del Proyecto
Plaintext

├── app.py              # Controlador principal y rutas de la aplicación
├── database.py         # Configuración y conexión a MongoDB
├── product.py          # Modelo de clase Product
├── templates/          # Plantillas HTML (Jinja2)
│   ├── layout.html     # Estructura base (navbar, imports)
│   ├── index.html      # Página principal (lista y filtros)
│   ├── create.html     # Formulario de creación
│   ├── edit.html       # Formulario de edición
│   └── delete.html     # Confirmación de eliminación
└── README.md           # Documentación del proyecto

🔍 Detalles de Uso
Crear Producto: Haz clic en "Nuevo Producto" en la barra de navegación. Si dejas el campo "URL de Imagen" vacío, se asignará una imagen gris por defecto.
Buscar/Filtrar: Usa la barra superior en la página de inicio para buscar cuadernos específicos, marcas o filtrar por precios.
Stock: El indicador de stock cambiará de color (verde/rojo) dependiendo de si hay más o menos de 10 unidades.
