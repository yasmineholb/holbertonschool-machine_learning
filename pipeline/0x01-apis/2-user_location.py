#!/usr/bin/env python3
""" Rate me is you can! """
import sys
import time
import requests


if __name__ == '__main__':
    ln = sys.argv[1]
    req = requests.get(ln, params=ld)
    js = r.json()
    if req.status_code == 403:
        lt = req.headers["X-Ratelimit-Reset"]
        x = (int(lt) - int(time.time())) / 60
        print("Reset in {} min".format(int(x)))
    if req.status_code == 200:
        print(js["location"])
    if req.status_code == 404:
        print("Not found")
