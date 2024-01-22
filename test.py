


from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth import exceptions, load_credentials_from_file
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/drive.file']

def get_credentials():
    try:
        credentials, _ = load_credentials_from_file('C:/Users/pavan/OneDrive/Desktop/FileUploadDemo/client_secret_477906363182-m56e2de0t5j71ikts30s5prcrv722beb.apps.googleusercontent.com.json', SCOPES)
        if not credentials.valid:
            credentials.refresh(Request())
        return credentials
    except exceptions.GoogleAuthError:
        flow = InstalledAppFlow.from_client_secrets_file(
            'C:/Users/pavan/OneDrive/Desktop/FileUploadDemo/client_secret_477906363182-m56e2de0t5j71ikts30s5prcrv722beb.apps.googleusercontent.com.json',
            scopes=SCOPES,
            redirect_uri="https://developers.google.com/oauthplayground"
        )
        credentials = flow.run_local_server(port=0)
        return credentials

credentials = get_credentials()

# Now you can use the credentials for API calls
# For example, print the access token
print("Access token:", credentials.token)




curl --request POST --data "code=4/0AfJohXkD8pLXpc-hYM0hhqurzxJri74c5vYFtTsgw8x3lBsCVeIpqjovAbqvrZfIT1sSjg&client_id=477906363182-m56e2de0t5j71ikts30s5prcrv722beb.apps.googleusercontent.com&client_secret=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&redirect_uri=http://localhost&grant_type=authorization_code" https://oauth2.googleapis.com/token



https://accounts.google.com/o/oauth2/auth?client_id=477906363182-m56e2de0t5j71ikts30s5prcrv722beb.apps.googleusercontent.com&redirect_uri=https://developers.google.com/oauthplayground&response_type=code&scope=https://www.googleapis.com/auth/drive&access_type=offline&prompt=consent


4/0AfJohXkD8pLXpc-hYM0hhqurzxJri74c5vYFtTsgw8x3lBsCVeIpqjovAbqvrZfIT1sSjg