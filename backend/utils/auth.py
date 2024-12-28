import msal
from config import MICROSOFT_CLIENT_ID, MICROSOFT_CLIENT_SECRET, TENANT_ID

def get_access_token():
    app = msal.ConfidentialClientApplication(
        client_id=MICROSOFT_CLIENT_ID,
        client_credential=MICROSOFT_CLIENT_SECRET,
        authority=f"https://login.microsoftonline.com/{TENANT_ID}"
    )
    result = app.acquire_token_silent(scopes=["https://graph.microsoft.com/.default"], account=None)
    if not result:
        result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
    if "access_token" in result:
        return result["access_token"]
    raise Exception("Unable to get access token")
