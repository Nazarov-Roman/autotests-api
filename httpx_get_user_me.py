import httpx

BASE_URL = "http://localhost:8000"

login_data = {
    "email": "gorilla@zippo.com",
    "password": "password",
}

login_resp = httpx.post(f"{BASE_URL}/api/v1/authentication/login", json=login_data)
login_json = login_resp.json()

print("Login response:", login_json)
print("Status Code:", login_resp.status_code)

access_token = login_json["token"]["accessToken"]
auth_headers = {"Authorization": f"Bearer {access_token}"}

me_resp = httpx.get(f"{BASE_URL}/api/v1/users/me", headers=auth_headers)

print("User Info:", me_resp.json())
print("Status Code", me_resp.status_code)
