import httpx
from json import dumps

login_payload = {
    "email": "i.ivanov@example.com",
    "password": "ivan"
}

login_uri = "/authentication/login"
user_uri = "/users/me"

client = httpx.Client(base_url="http://localhost:8000/api/v1")

login_response = client.post(login_uri, json=login_payload)
login_response_data = login_response.json()

access_token = login_response_data['token']['accessToken']
auth_headers = {'Authorization': f'Bearer {access_token}'}

print(f"Ответ на {login_uri}: {dumps(login_response_data, indent=4)}")
print(f"Статус ответа на {login_uri}: {login_response.status_code}\n")

me_response = client.get(user_uri, headers=auth_headers)
me_response_data = me_response.json()

print(f"Ответ на {user_uri}: {dumps(me_response_data, indent=4)}")
print(f"Статус ответа на {user_uri}: {me_response.status_code}")