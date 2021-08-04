#!/usr/bin/env python3
""" Get requests"""
import requests


def availableShips(passengerCount):
    """ method that returns the list of ships that can
    hold a given number of passengers """
    Sships = []
    req = 'https://swapi-api.hbtn.io/api/starships/'
    while req is not None:
        response = requests.get(req, headers={'Accept': 'application/json'})
        for ship in response.json()['results']:
            if ship["passengers"] != "n/a" and ship["passengers"] != "unknown":
                passenger = ship['passengers'].replace(',', '')
                if passenger.isnumeric() and int(passenger) >= passengerCount:
                    Sships.append(ship['name'])
        req = response.json()['next']
    return Sships
