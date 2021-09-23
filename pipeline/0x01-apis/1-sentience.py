#!/usr/bin/env python3
""" Where I am? """
import requests


def sentientPlanets():
    """ Function that returns the list of names
    of the home planets of all sentient species """
    ln = "https://swapi-api.hbtn.io/api/species/"
    plt = []
    while ln is not None:
        r = requests.get(ln)
        results = r.json()["results"]
        for specie in results:
            if (specie["designation"] == "sentient" or
                    specie["classification"] == "sentient"):

                plt_url = specie["homeworld"]
                if plt_url is not None:
                    p = requests.get(plt_url).json()
                    plt.append(p["name"])
        ln = r.json()["next"]
    return plt
