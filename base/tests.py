import requests

url = ' http://127.0.0.1:8000/api/create/'
payload = {
    'log_msg': 'An error occurred during the scheduling process.',
    'StatusCode': '500',
    'user_mailid': 'user@example.com',
    'Plugin': 'acuity_scheduling',
    'function': 'OnScheduling'
}

# Send the payload as JSON
response = requests.post(url, json=payload)  # Use json=payload instead of data=payload

if response.status_code == 201:
    print("Log entry created:", response.json())
else:
    print(f"Failed to create log entry: {response.status_code}")
    print(response.text)
