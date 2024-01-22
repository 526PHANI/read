# yourapp/management/commands/upload_to_drive.py

import os
from django.core.management.base import BaseCommand
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from django.conf import settings

class Command(BaseCommand):
    help = 'Upload files from the media folder to Google Drive'

    def handle(self, *args, **options):
        # Authenticate with Google Drive API
        drive_service = self.authenticate_google_drive()

        # Specify the path to the media folder
        media_folder = settings.MEDIA_ROOT

        # Loop through files in the media folder
        for filename in os.listdir(media_folder):
            file_path = os.path.join(media_folder, filename)

            # Upload each file to Google Drive
            self.upload_to_google_drive(file_path, drive_service)

    #
    # 
    def authenticate_google_drive(self):
        # ... (Same as before)
            # Load credentials from a file (you should secure this file)
        credentials_path = os.path.join(settings.BASE_DIR, 'C:/Users/pavan/OneDrive/Desktop/FileUploadDemo/client_secret_477906363182-m56e2de0t5j71ikts30s5prcrv722beb.apps.googleusercontent.com.json')
        token_path = os.path.join(settings.BASE_DIR, 'C:/Users/pavan/OneDrive/Desktop/FileUploadDemo/read-documents-410704-7f8cac616d97.json')


        creds = None
        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(token_path)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(credentials_path, ['https://www.googleapis.com/auth/drive.file'])
                creds = flow.run_local_server(port=0)
            with open(token_path, 'w') as token:
                token.write(creds.to_json())
        return build('drive', 'v3', credentials=creds)
     
    

    def upload_to_google_drive(self, file_path, drive_service):
        file_metadata = {'name': os.path.basename(file_path)}
        media = MediaFileUpload(file_path, mimetype='application/octet-stream')
        drive_service.files().create(body=file_metadata, media_body=media).execute()
  