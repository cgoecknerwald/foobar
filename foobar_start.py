# This script was created to enter the foobar challenge.

import requests
import json
import math

r = requests.get('https://www.find.foo/api/challenge?token=KTNyMXTMijcpp74VhwtWpd')
j =  r.text
j = json.loads(j)
line1  =  eval(j["challenge"].split()[7])
line2  =  eval(j["challenge"].split()[8])

dist = math.ceil(math.sqrt((line1[0]-line2[0])**2 + (line1[1] -line2[1])**2))

s = str(int(dist))
token = "KTNyMXTMijcpp74VhwtWpd"
params = {"answer": s, "token": token}
r = requests.post("https://www.find.foo/api/challenge", data=params)
r = r.text
j = json.loads(r)
challenge = j["challenge"]
challenge = challenge[challenge.index('['):]
line = eval(challenge)
lineNew = []
for s in line:
	lineNew.append(s)
	lineNew.append(s)

lineNew = str(lineNew)

params = {"answer": lineNew, "token": token}

r = requests.post("https://www.find.foo/api/challenge", data=params)
j =  r.text
j = json.loads(j)
line = j["challenge"]
line = line[line.index(": ")+2:]
print line

for length in range(len(line), 1, -1):
	finished = False	
	for start in range(0, len(line)-length+1):
		substring = line[start:start+length]
		count = line.count(substring)
		
		if count > 1:
			finished = True
			break
	if finished:
		break

params["answer"] = substring
r = requests.post("https://www.find.foo/api/challenge", data=params)
print r.text
