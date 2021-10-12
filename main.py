"""
Main code structrure
"""

import json
from dataclasses import dataclass

def main () -> None:

    # read data from database
    with open("./database/data.json") as file:
        data = json.load(file)
    
    # take user input
    
    # dog on challenge
    dogs = []
    for dog in data["dogs"]:

    # compares dog in challenge