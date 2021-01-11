import fetch_title
import os
from datetime import date

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import google.oauth2.credentials

CLIENT_SECRETS_FILE = 'D:/Documents/blogger-post/client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/blogger']
blogId = '7479026719872323323'
blog_boddy = {
  'title': f'{date.today()}',
  'content': fetch_title.main(r'D:\next\url.txt')
}

def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  print(credentials.refresh_token)
  return build('blogger', 'v3', credentials = credentials)

def blogger_post(service, **kwargs):
    results = service.posts().insert(**kwargs).execute()
    print(results['url'])

if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  service = get_authenticated_service()
  blogger_post(service, blogId=blogId, body=blog_boddy)