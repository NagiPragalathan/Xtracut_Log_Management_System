import requests

url = 'https://xtracut-log-management-system.vercel.app/api/create/'
payload = {
    'log_msg': 'Test log message',
    'StatusCode': '200',
    'user_mailid': 'test@example.com',
    'Plugin': 'Test Plugin',
    'function': 'Test Function'
}

# Pass the payload directly as the data
response = requests.post(url, data=payload)

# Check if the request was successful
if response.status_code == 201:
    print("Log entry created:", response.json())
else:
    print(f"Failed to create log entry: {response.status_code}")
    print(response.text)
