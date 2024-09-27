import requests

url = 'http://localhost:8000/api/create/'
payload = {
    'log_msg': 'Test log message',
    'StatusCode': '200',
    'user_mailid': 'test@example.com',
    'Plugin': 'Test Plugin',
    'function': 'Test Function'
}

response = requests.post(url, data=[payload])

print(response.json())
