import msal
from config import client_id, authority, scopes

def get_token():
    app = msal.PublicClientApplication(client_id=client_id, authority=authority)
    flow = app.initiate_device_flow(scopes=scopes)

    if "user_code" not in flow:
        raise Exception(f"Autentificarea nu a putut fi inițiată: {flow}")
    
    print("🔐 Mergi la:", flow["verification_uri"])
    print("👉 Introdu codul:", flow["user_code"])

    result = app.acquire_token_by_device_flow(flow)

    if "access_token" in result:
        print("✅ Token obținut cu succes.")
        return result["access_token"]
    else:
        raise Exception("❌ Autentificare eșuată:", result.get("error_description"))
