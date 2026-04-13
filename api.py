from flask import Flask, jsonify, request

app = Flask(__name__)

## Initial Data
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route("/")
def home():
    return "Welcome to the sample to-do list app"


# GET all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)


# GET single item
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(item)


# POST create item - API
@app.route('/items', methods=['POST'])
def create_item():

    if not request.json or 'name' not in request.json:
        return jsonify({"error": "Name is required"}), 400

    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json.get("description", "")
    }

    items.append(new_item)

    return jsonify(new_item), 201


# PUT update item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):

    item = next((item for item in items if item["id"] == item_id), None)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    if not request.json:
        return jsonify({"error": "Request must be JSON"}), 400

    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])

    return jsonify(item)


# DELETE item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):

    global items

    if not any(item["id"] == item_id for item in items):
        return jsonify({"error": "Item not found"}), 404

    items = [item for item in items if item["id"] != item_id]

    return jsonify({"result": "Item deleted"})
    

if __name__ == '__main__':
    app.run(debug=True)