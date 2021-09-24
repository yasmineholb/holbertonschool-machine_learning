#!/usr/bin/env python3
""" How many by rocket? """
import requests


if __name__ == '__main__':
    """ How many by rocket? Function """
    ln = "https://api.spacexdata.com/v4/launches"
    r = requests.get(ln)
    launches = r.json()
    dict = {}
    for i, launch in enumerate(launches):
        rk_id = launch["rocket"]
        rk_url = "https://api.spacexdata.com/v4/rockets/{}".format(
            rk_id)
        rocket = requests.get(rk_url).json()["name"]
        if rocket in dict.keys():
            dict[rocket] += 1
        else:
            dict[rocket] = 1
    rk = sorted(dict.items(), key=lambda kv: kv[0])
    rk = sorted(rk, key=lambda kv: kv[1], reverse=True)
    for rocket in rk:
        print(*rocket, sep=": ")
