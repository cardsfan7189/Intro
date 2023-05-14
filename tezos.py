import requests
import math
from datetime import datetime

#URL = "https://prater.beaconcha.in/api/v1/validator/stats/66536"
#URL = "https://prater.beaconcha.in/api/v1/validator/stats/284747"
#URL = "https://api.tzkt.io/v1/cycles/200"
#URL = "https://api.tzkt.io/v1/statistics"
URL = "https://api.tzkt.io/v1/delegates?active=true&limit=700"
#687567698853889
#687960287985538
#693319188891231
#682314220224283
#685,911,936.003519

def calc_total_rewards(address,activationTime):
    total = 0
    resp = requests.get("https://api.tzkt.io/v1/rewards/bakers/" + address + "?limit=500")
    data = resp.json()
    cycle_count = 0;
    for rec in data:
        if int(rec["stakingBalance"]) < 8501000000:
            total = total + int(rec["endorsementRewards"]) + int(rec["ownBlockRewards"])
            cycle_count = cycle_count + 1
        else:
            return
    print("{0}: {1}, {2}, {3}".format(address,total / 1000000,(total / 1000000) / cycle_count, activationTime))


resp = requests.get(URL)
data = resp.json()
for rec in data:
    if int(rec["stakingBalance"]) > 8000000000 and int(rec["stakingBalance"]) < 8501000000:
        #print(rec)
        calc_total_rewards(rec["address"],rec["activationTime"])