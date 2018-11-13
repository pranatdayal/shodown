# shodown
Script utilizing Shodan API to query hosts 

Before running install shodan API: 

    easy_install shodan 

Takes in a file called ip.list (see example file) 
and saves the output to shodan_results_all.json. 

Prints IP,Ports,OS,hostname,org and banners for each port to stdout

SHODAN API rate limits to 1 IP per second. No credits are used for this. 

