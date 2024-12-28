from flask import Blueprint, jsonify, request
from utils.langchain import vectorstore

contacts_blueprint = Blueprint("contacts", __name__)

@contacts_blueprint.route("/", methods=["GET"])
def get_contacts():
    try:
        # Retrieve contacts from vectorstore
        results = vectorstore.similarity_search("contact")
        return jsonify({"contacts": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@contacts_blueprint.route("/add", methods=["POST"])
def add_contact():
    data = request.json
    try:
        # Add contact to vectorstore
        contact_info = f"Name: {data.get('name')}, Email: {data.get('email')}, Phone: {data.get('phone')}"
        vectorstore.add_texts([contact_info])
        return jsonify({"message": "Contact added successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500