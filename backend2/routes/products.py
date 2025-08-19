# routes/products.py
from flask import Blueprint, request, jsonify
# <-- CAMBIO AQUÍ: Importamos todas las funciones necesarias del controlador
from controllers.product_controller import (
    get_all_products, 
    get_product_by_id,
    create_product, 
    update_product,
    delete_product
)

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods=['GET'])
def get_products_route():
    products = get_all_products()
    return jsonify(products)

@products_bp.route('/<int:product_id>', methods=['GET'])
def get_product_route(product_id):
    product = get_product_by_id(product_id)
    if product:
        return jsonify(product)
    return jsonify({"message": "Producto no encontrado"}), 404

@products_bp.route('/', methods=['POST'])
def add_product_route():
    data = request.get_json()
    new_product = create_product(data)
    return jsonify(new_product), 201

# <-- CAMBIO AQUÍ: Ruta PUT para actualizar un producto por su ID
@products_bp.route('/<int:product_id>', methods=['PUT'])
def update_product_route(product_id):
    data = request.get_json()
    updated_product = update_product(product_id, data)
    if updated_product:
        return jsonify(updated_product)
    return jsonify({"message": "Producto no encontrado"}), 404

# <-- CAMBIO AQUÍ: Ruta DELETE para eliminar un producto por su ID
@products_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    result = delete_product(product_id)
    if result:
        return jsonify({"message": "Producto eliminado exitosamente"})
    return jsonify({"message": "Producto no encontrado"}), 404