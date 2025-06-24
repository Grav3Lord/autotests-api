import httpx

from tools.fakers import get_random_email
from json import dumps

create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_uri = "/users"
login_uri = "/authentication/login"

with httpx.Client(base_url="http://localhost:8000/api/v1") as client:
    create_user_response = client.post(create_user_uri, json=create_user_payload)
    create_user_response_data = create_user_response.json()

    print(f"Ответ на {create_user_uri}: {dumps(create_user_response_data, indent=4)}\n")
    print(f"Статус ответа на {create_user_uri}: {create_user_response.status_code}")

    login_payload = {
        "email": create_user_payload["email"],
        "password": create_user_payload["password"],
    }

    login_response = client.post(login_uri, json=login_payload)
    login_response_data = login_response.json()

    print(f"Ответ на {login_uri}: {dumps(login_response_data, indent=4)}")
    print(f"Статус ответа на {login_uri}: {login_response.status_code}\n")

    update_user_headers = {
        "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
    }

    update_user_payload = {
        "email": get_random_email(),
        "lastName": "Tolstoj",
        "firstName": "Lev",
        "middleName": "Nikolaevich"
    }

    patch_user_uri = f"/users/{create_user_response_data['user']['id']}"

    update_response = client.patch(patch_user_uri, json=update_user_payload, headers=update_user_headers)
    update_response_data = update_response.json()

    print(f"Ответ на {patch_user_uri}: {dumps(update_response_data, indent=4)}")
    print(f"Статус ответа на {patch_user_uri}: {update_response.status_code}")

    client.close()