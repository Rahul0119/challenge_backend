import json

from flask import Blueprint, jsonify, request

transaction_blueprint = Blueprint('transactions', __name__)

# Helper function to read transaction data from JSON file
def read_transactions_data():
    with open('transactions.json') as data_file:
        return json.load(data_file)

# Helper function to write transaction data to JSON file
def write_transactions_data(data):
    with open('transactions.json', 'w') as data_file:
        json.dump(data, data_file, indent=4)

@transaction_blueprint.route('/transaction/<id>', methods=['GET'])
def get_transaction(id):
    transactions_data = read_transactions_data()
    transaction = transactions_data.get(id, None)
    if transaction:
        return jsonify(transaction), 200
    else:
        return jsonify({"error": "Transaction not found"}), 404

@transaction_blueprint.route('/transaction', methods=['POST'])
def add_transaction():
    transaction_data = request.json
    transactions_data = read_transactions_data()
    transactions_data[transaction_data['id']] = transaction_data
    write_transactions_data(transactions_data)
    return jsonify({"message": "Transaction added successfully"}), 201

@transaction_blueprint.route('/transaction/<id>', methods=['PUT'])
def update_transaction(id):
    transaction_data = request.json
    transactions_data = read_transactions_data()
    if id in transactions_data:
        transactions_data[id] = transaction_data
        write_transactions_data(transactions_data)
        return jsonify({"message": "Transaction updated successfully"}), 200
    else:
        return jsonify({"error": "Transaction not found"}), 404

@transaction_blueprint.route('/transaction/<id>', methods=['DELETE'])
def delete_transaction(id):
    transactions_data = read_transactions_data()
    if id in transactions_data:
        del transactions_data[id]
        write_transactions_data(transactions_data)
        return jsonify({"message": "Transaction deleted successfully"}), 200
    else:
        return jsonify({"error": "Transaction not found"}), 404

@transaction_blueprint.route('/transactions', methods=['GET'])
def get_all_transactions():
    transactions_data = read_transactions_data()
    return jsonify(transactions_data), 200
