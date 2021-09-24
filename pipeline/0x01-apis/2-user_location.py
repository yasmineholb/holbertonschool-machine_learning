#!/usr/bin/env python3
""" Rate me is you can! """
import sys
import requests
import time


if __name__ == '__main__':
    """ Rate me is you can Function"""
    ln = sys.argv[1]
    js = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(ln, params=js)
    if r.status_code == 403:
        limit = r.headers["X-Ratelimit-Reset"]
        x = (int(limit) - int(time.time())) / 60
        print("Reset in {} min".format(int(x)))
    if r.status_code == 200:
        loc = r.json()["location"]
        print(loc)
    if r.status_code == 404:
        print("Not found")
