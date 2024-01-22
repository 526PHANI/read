# File: google_drive_utils.py
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import io

def get_google_drive_credentials():
    credentials = Credentials.from_authorized_user_file(r'C:\Users\pavan\OneDrive\Desktop\FileUploadDemo\client_secret_477906363182-m56e2de0t5j71ikts30s5prcrv722beb.apps.googleusercontent.com.json')
    return credentials

def upload_to_google_drive(file_name, file_content):
    credentials = get_google_drive_credentials()
    service = build('drive', 'v3', credentials=credentials)

    file_metadata = {
        'name': file_name,
        'mimeType': 'application/pdf',  # Adjust mime type accordingly
    }

    media = io.BytesIO(file_content)

    uploaded_file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    return uploaded_file.get('id')
