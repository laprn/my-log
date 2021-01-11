import requests
import config

def reload():
    data = '{}'
    return requests.post(config.hook_url, data=data)

if __name__ == '__main__':
    response = reload()
    print(response.status_code)