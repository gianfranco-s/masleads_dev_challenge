import base64

API_USR = 'masleads-api-usr'  # WARNING: these credentials are also hardcoded in app.py
API_PWD = 'masleads-api-pwd'  # WARNING: these credentials are also hardcoded in app.py

credentials = f"{API_USR}:{API_PWD}"
base64_credentials = base64.b64encode(credentials.encode()).decode()

HEADERS = {
    'Authorization': f'Basic {base64_credentials}'
}
