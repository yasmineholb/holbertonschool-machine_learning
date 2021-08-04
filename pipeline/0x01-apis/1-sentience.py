#!/usr/bin/env python3
""" Where I am? """
import requests


def sentientPlanets():
    """ method that returns the list of names
    of the home planets of all sentient species """
    Hplanets = []
    req = 'https://swapi-api.hbtn.io/api/species/'
    while req is not None:
        response = requests.get(req, headers={'Accept': 'application/json'})
        for pl in response.json()['results']:
            if pl["homeworld"] != "n/a" and pl["homeworld"] is not None:
                Hworls = prequests.get(species['homeworld'])
                Hplanets.append(Hworls.json()['name'])
        req = response.json()['next']
    return Hplanets
