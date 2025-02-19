import json
from operator import itemgetter
from pprint import pprint

data_file = open('data.json')
humidity_data = json.load(data_file)

print(humidity_data['type'], 'data avg:', end=" ")
cnt = 0
sum = 0
for h in humidity_data['data']:
    sum = sum + h['value']
    cnt = cnt + 1
print(sum/cnt)

# append with new sensor data
print('adding data:')
last_data_item = max(humidity_data['data'], key=itemgetter('eventId'))
next_id = last_data_item['eventId'] + 1
humidity_data['data'].append({'value': 56, 'eventId': next_id})
pprint(humidity_data)
