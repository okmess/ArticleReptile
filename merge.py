import json
import os

data_list = []



for i in range(10):
    with open('journal_final_data.json') as f:
        data = json.load(f)
        data_list.extend(data)

with open('journal_final_data_copy_10.json', 'w') as f:
    json.dump(data_list, f)