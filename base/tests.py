
# # url = 'https://your-api-url.com/api/create-log/'
# payload = {
#     'log_msg': 'An error occurred during the scheduling process.',
#     'StatusCode': '500',
#     'user_mailid': 'user@example.com',
#     'Plugin': 'acuity_scheduling',
#     'function': 'OnScheduling'
# }



# # url = 'http://127.0.0.1:8000/api/create/'
# # payload = {
# #     'log_msg': 'Test log message',
# #     'StatusCode': '200',
# #     'user_mailid': 'test@example.com',
# #     'Plugin': 'Test Plugin',
# #     'function': 'Test Function'
# # }

# import requests

# url = 'https://xtracut-log-management-system.vercel.app/api/create/'
# # payload = {
# #     'log_msg': 'An error occurred during the scheduling process.',
# #     'StatusCode': '500',
# #     'user_mailid': 'user@example.com',
# #     'Plugin': 'acuity_scheduling',
# #     'function': 'OnScheduling'
# # }

# # Send the payload as JSON
# response = requests.post(url, json=payload)  # Use json=payload to send as JSON

# # Check if the request was successful
# if response.status_code == 201:
#     print("Log entry created:", response.json())
# else:
#     print(f"Failed to create log entry: {response.status_code}")
#     print(response.text)

import requests

# Define the URL of the endpoint
url = 'https://xtracut-log-management-system.vercel.app/api/create/'

# Define the payload (URL-encoded)
payload = {
    'log_msg': 'End Time Response',
    'StatusCode': '201',
    'user_mailid': 'hello@msandinnovationchallenge.com',
    'Plugin': 'acuity_scheduling',
    'function': 'onScheduleNew'
}

# Send the POST request as URL-encoded form data
response = requests.post(url, data=payload)  # `data=payload` sends the form-encoded data

# Check if the request was successful
if response.status_code == 201:
    print("Log entry created successfully!")
    print("Response JSON:", response.json())
else:
    print(f"Failed to create log entry: {response.status_code}")
    print("Response Text:", response.text)
