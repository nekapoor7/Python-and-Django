"""Parse the above routing table into a structured format.
The interviewee should first define the data structure and
write code to parse the input
into the defined data structure. Feel free to ask any questions
 about the raw output."""

import re
import json

d = {'84.38.34.45/32': {'AD': 115, 'Metric': 20400, 'NextHop': '2.120.13.35','Interface': 'Bundle-Ether11'},
         '84.38.34.45/32': {'AD': 115, 'Metric': 20400, 'NextHop': '2.120.13.35','Interface': 'Bundle-Ether10'},
         '84.38.34.45/32': {'AD': 115, 'Metric': 20400, 'NextHop': '2.120.13.35','Interface': 'Bundle-Ether9'},
         '84.38.34.45/32': {'AD': 115, 'Metric': 20400, 'NextHop': '2.120.13.35','Interface': 'Bundle-Ether8'}}

def recursive_items(d):
    for key, value in d.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)

for key, value in recursive_items(d):
      print(key,value)

app_json = json.dumps(d)
print(app_json)

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\Regex_IP.txt",'r',encoding='utf-8') as f:
    data = f.read()

network_regex = re.findall(r'^[a-zA-Z0-9\W]+\W+\W+\W+\S+\W+\W+\S+\W+\S+\W+\W+\S+\W+'
                           r'\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+'
                           r'\S+\W+\S\W+\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+'
                           r'\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+\S+'
                           r'\W+\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+'
                           r'\S+\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+\S+\W+\S+',data)
for item in network_regex:
        print(item)





