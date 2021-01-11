import requests
import os

def reload():
    data = '{}'
    return requests.post(os.environ['hook_url'], data=data)

if __name__ == '__main__':
    response = reload()
    print(response.status_code)