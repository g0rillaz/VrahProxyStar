import dryscrape

import re

url = 'http://spys.one/free-proxy-list/FR/'



#get html with javascript
session = dryscrape.Session()
session.visit(url)
response = session.body()


#capture ip:
IP = re.findall(r'[0-9]+(?:\.[0-9]+){3}(?=<script)',response)

#capture port:
port = re.findall(r'(?<=:</font>)(.*?)(?=\<)',response)

#join IP with ports
IP_with_ports = []
for i in range(len(IP)):
    IP_with_ports.append(IP[i] + ":" + port[i])