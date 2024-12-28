from flask import Blueprint, jsonify, request
from utils.icloud import fetch_events, add_event_to_calendar

calendar_blueprint = Blueprint("calendar", __name__)

@calendar_blueprint.route("/", methods=["GET"])
def get_calendar_events():
    try:
        events = fetch_events()
        return jsonify({"events": events})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@calendar_blueprint.route("/add", methods=["POST"])
def add_event():
    data = request.json
    try:
        add_event_to_calendar(
            summary=data.get("summary"),
            start_time=data.get("start_time"),
            end_time=data.get("end_time"),
            description=data.get("description", "")
        )
        return jsonify({"message": "Event added successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500