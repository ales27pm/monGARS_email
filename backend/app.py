from flask import Flask, request, jsonify
from flask_cors import CORS
from routes.emails import email_blueprint
from routes.contacts import contacts_blueprint
from routes.calendar import calendar_blueprint
from utils.langchain import initialize_langchain

app = Flask(__name__)
CORS(app)

# Initialize LangChain
initialize_langchain()

# Register routes
app.register_blueprint(email_blueprint, url_prefix="/api/emails")
app.register_blueprint(contacts_blueprint, url_prefix="/api/contacts")
app.register_blueprint(calendar_blueprint, url_prefix="/api/calendar")

@app.route("/ask", methods=["POST"])
def ask():
    from utils.langchain import conversation_chain, vectorstore
    data = request.json
    user_input = data.get("user_input", "")
    
    # Process input with LangChain
    result = conversation_chain.run({"query": user_input})
    vectorstore.add_texts([user_input, result["answer"]])

    # Return result
    return jsonify({
        "response": result["answer"],
        "sources": result.get("source_documents", [])
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
