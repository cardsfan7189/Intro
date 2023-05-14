import requests
import math
from datetime import datetime

def get_block_time(block_hash):
    resp = requests.get("https://api.tzkt.io/v1/blocks/" + block_hash)
    if resp.status_code == 200:
        data = resp.json()
        timestamp = data["timestamp"]
        return tuple((datetime.strptime(timestamp,'%Y-%m-%dT%H:%M:%SZ'),data["level"]))
    return None
base_time = datetime.strptime("Sep 28 03:00:00 2022",'%b %d %H:%M:%S %Y')
total_secs_subtotal = 0
subtotal_counter = 0
total_secs = 0
total_counter = 0
max_secs = 0
pid = "90130"

with open("C:\\Users\\DREWA\\Downloads\\validations.txt") as f:
    while True:
        record = f.readline()
        if not record:
            break
        #print(record)
        if "block " in record:

            start_pos = record.index("block ") + 6
            end_pos = start_pos + 51
            block_hash = record[start_pos:end_pos]
            block_time_tuple = get_block_time(block_hash)
            if block_time_tuple:
                time_obj = datetime.strptime(record[0:15] + " 2022",'%b %d %H:%M:%S %Y')
                if time_obj:
                    num_secs = (time_obj - block_time_tuple[0]).total_seconds()
                    if num_secs > 8:
                        print("Level {0} more than 8 seconds, {1} seconds".format(block_time_tuple[1],num_secs))
                    if num_secs > max_secs:
                        max_secs = num_secs
                    total_secs = num_secs + total_secs
                    total_counter = total_counter + 1

print("Overall avg: {0}, max {1}".format(total_secs/total_counter,max_secs))
exit(0)
resp = requests.get("https://api.tzkt.io/v1/rights?type=endorsing&baker=tz1ffYUjwjduZkoquw8ryKRQaUjoWJviFVK6&cycle=529&limit=8000")
data = resp.json()
missed_slots = 0
endorsed_slots = 0
total_slots = 0
for rec in data:
    if rec["status"] == "realized":
        endorsed_slots = endorsed_slots + int(rec["slots"])
    elif rec["status"] == "missed":
        missed_slots = missed_slots + int(rec["slots"])
total_slots = missed_slots + endorsed_slots
print("Total slots: {0}, endorsed slots: {1}, missed slots: {2}, reliability {3}".format(total_slots,endorsed_slots,missed_slots,endorsed_slots/total_slots))

