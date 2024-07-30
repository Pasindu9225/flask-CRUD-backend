from models import collection
from flask import Flask, request, jsonify
from flask_cors import CORS
from bson import ObjectId

app = Flask(__name__)
CORS(app)

@app.route('/api/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    title = data['title']
    description = data['description']  # Fixed typo

    post = {
        'name': title,
        'description': description,
    }

    try:
        collection.insert_one(post)
        return jsonify("success")
    except Exception as e:
        return jsonify("error"), 500

@app.route('/api/get_tasks', methods=['GET'])  # Fixed the endpoint name
def get_tasks():
    data = list(collection.find())
    for doc in data:
        doc['_id'] = str(doc['_id'])
    return jsonify(data)

@app.route('/api/edit_task', methods=['POST'])
def edit_task():
    data = request.get_json()
    task_id = data['_id']
    updated_data = data['updated_data']

    try:
        collection.update_one({'_id': ObjectId(task_id)}, {'$set': updated_data})
        return jsonify("success")
    except Exception as e:
        return jsonify("error"), 500

@app.route('/api/delete_task', methods=['DELETE'])  # Fixed the endpoint name and method
def delete_task():
    data = request.get_json()
    task_id = data['_id']

    try:
        collection.delete_one({'_id': ObjectId(task_id)})
        return jsonify("success")
    except Exception as e:
        return jsonify("error"), 500

if __name__ == '__main__':
    app.run(debug=True)
