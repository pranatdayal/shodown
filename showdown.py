import shodan
import sys
import json

apikey = "<apikey>"
api = shodan.Shodan(apikey)

hosts_file = open('ip.list','r')

hosts=[]
results={}
for host in hosts_file:
    hosts.append(host.strip())

for i in hosts:
    try:
        info = api.host(i)
        results[i] = info
    except shodan.APIError,e:
        print("Error:{}".format(e))

with open('shodan_results_all.json','w') as all_info:
    json.dump(results,all_info,indent=4)



