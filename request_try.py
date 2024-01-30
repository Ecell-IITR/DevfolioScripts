import requests
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiZDIxZThiMDUyZmRlNDMxNjg1NWM4MDk2OTZjZDllNmIiLCJtYWlsYm94Ijoidm94b2c0MjA1OEBnb3Nhcmxhci5jb20iLCJpYXQiOjE3MDY0NjcxOTB9.yAt_bLUd26nFBh5f78ceY5JLFtZc6RPatNXaAxw-cEk',
}

response =requests.get('https://web2.temp-mail.org/mailbox',headers=headers)
print(response.status_code)
print(response.content)