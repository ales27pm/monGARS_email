from caldav import DAVClient
from config import ICLOUD_USERNAME, ICLOUD_PASSWORD

CARD_DAV_URL = "https://contacts.icloud.com"
CAL_DAV_URL = "https://caldav.icloud.com"

def fetch_contacts():
    try:
        client = DAVClient(CARD_DAV_URL, username=ICLOUD_USERNAME, password=ICLOUD_PASSWORD)
        principal = client.principal()
        addressbooks = principal.addressbooks()
        contacts = []
        for addressbook in addressbooks:
            for card in addressbook.cards():
                contact_data = card.data
                contacts.append(contact_data)
        return contacts
    except Exception as e:
        print(f"Error fetching contacts: {e}")
        return []

def add_contact(name, email, phone):
    try:
        contact_vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
EMAIL:{email}
TEL:{phone}
END:VCARD"""
        client = DAVClient(CARD_DAV_URL, username=ICLOUD_USERNAME, password=ICLOUD_PASSWORD)
        principal = client.principal()
        addressbooks = principal.addressbooks()
        if addressbooks:
            addressbooks[0].add_card(contact_vcard)
    except Exception as e:
        print(f"Error adding contact: {e}")

def fetch_events():
    try:
        client = DAVClient(CAL_DAV_URL, username=ICLOUD_USERNAME, password=ICLOUD_PASSWORD)
        principal = client.principal()
        calendars = principal.calendars()
        events = []
        for calendar in calendars:
            for event in calendar.events():
                events.append(event.data)
        return events
    except Exception as e:
        print(f"Error fetching events: {e}")
        return []

def add_event_to_calendar(summary, start_time, end_time, description=""):
    try:
        client = DAVClient(CAL_DAV_URL, username=ICLOUD_USERNAME, password=ICLOUD_PASSWORD)
        calendars = client.principal().calendars()
        if calendars:
            event = f"""BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
SUMMARY:{summary}
DESCRIPTION:{description}
DTSTART:{start_time}
DTEND:{end_time}
END:VEVENT
END:VCALENDAR"""
            calendars[0].add_event(event)
    except Exception as e:
        print(f"Error adding event to calendar: {e}")