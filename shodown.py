import shodan
import json
import time
from datetime import datetime

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
    # API rate limit of 1 request/second
    time.sleep(1)


with open('shodan_results_all.json','w') as all_info:
    json.dump(results,all_info,indent=4)


for entry in results:

    entries = results[entry]
    ip = "IP : {}".format(entries['ip_str'])
    ports = "Ports : {}".format(entries['ports'])
    hostnames = "Hostnames : {}".format(entries['hostnames'])
    os = "OS : {}".format(entries['os'])
    org = "Org: {}".format(entries['org'])

    items = entries['data']

    print ip,ports,hostnames,os,org
    for item in items:
        print("Port: {}\nBanner: {}".format(item['port'], item['data']))
    print "\n"

print("for more info check shodan_results_all.json file")
