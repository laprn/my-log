import dropbox
import os

def download_file():
    dbx = dropbox.Dropbox(os.environ['TOKEN'])
    api_result = dbx.files_download('/url.txt')[1].text
    format_result = api_result.splitlines()
    return format_result

if __name__ == '__main__':
    print(download_file())