#!/usr/bin/env python3

import requests
import socket


def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"


def check_connectivity():
    request = requests.get("http://www.google.com")
    response = request
    return response.status_code == 200

if check_localhost() and check_connectivity():
    print("Everything ok")
else:
    print("Network checks failed")
