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
