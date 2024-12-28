from flask import Blueprint, jsonify, request
from utils.auth import get_access_token
from utils.langchain import conversation_chain, vectorstore
import requests

email_blueprint = Blueprint("emails", __name__)

MICROSOFT_GRAPH_URL = "https://graph.microsoft.com/v1.0/me"

@email_blueprint.route("/process", methods=["POST"])
def process_emails():
    user_input = request.json.get("user_input", "")
    try:
        # Retrieve emails
        access_token = get_access_token()
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(f"{MICROSOFT_GRAPH_URL}/messages", headers=headers)
        response.raise_for_status()

        emails = response.json().get("value", [])
        processed_emails = []

        # Use LangChain to analyze emails
        for email in emails:
            result = conversation_chain.run({"query": email["bodyPreview"]})
            processed_emails.append({
                "subject": email["subject"],
                "sender": email["from"]["emailAddress"]["address"],
                "body": email["bodyPreview"],
                "analysis": result["answer"]
            })

        return jsonify({"processed_emails": processed_emails})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
