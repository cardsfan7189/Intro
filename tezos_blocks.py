import requests
import math
from datetime import datetime

base_URL = "https://api.tzkt.io/v1/blocks?level="
resp = requests.get("https://api.tzkt.io/v1/head")
rec = resp.json()
starting_level = rec["level"]
while starting_level > -1:
    resp = requests.get(base_URL + str(starting_level))
    rec = resp.json()
    if rec[0]["blockRound"] > 0:
        print(rec[0]["hash"] + "," + str(rec[0]["blockRound"]))

    #print(rec[0]["blockRound"])
    #exit(0)
    starting_level = starting_level - 1
