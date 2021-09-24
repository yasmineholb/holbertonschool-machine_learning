#!/usr/bin/env python3
""" What will be next? """
import requests


if __name__ == '__main__':
    """ What will be next? Function """
    ln = "https://api.spacexdata.com/v4/launches/upcoming"
    r = requests.get(ln)
    js = r.json()
    date = float('inf')
    for i, launch in enumerate(js):
        if date > launch["date_unix"]:
            date = launch["date_unix"]
            index = i
    n = js[index]["name"]
    d = js[index]["date_local"]
    r_id = js[index]["rocket"]
    ln = "https://api.spacexdata.com/v4/rockets/{}".format(r_id)
    r_name = requests.get(ln).json()["name"]
    lp_id = js[index]["launchpad"]
    ln = "https://api.spacexdata.com/v4/launchpads/{}".format(lp_id)
    lp = requests.get(ln).json()
    lp_name = lp["name"]
    lp_loc = lp["locality"]
    print(n + " (" + d + ") " + r_name + " - " + lp_name + " (" + lp_loc + ")")
