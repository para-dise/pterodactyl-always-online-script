import requests
import time

headers = {
        "Authorization": "Bearer YOUR_API_TOKEN",
        "Content-Type": "application/json",
        "Accept": "Application/vnd.pterodactyl.v1+json"
}
servers = ["0aa00000", "0aa00aaa"] # a list of server IDs, eg 6cd06969
baseurl = "https://panel.your.host" #configure this to be a pterodactyl base url. eg "https://panel.freemc.host" don't include a slash at the end

while True:
    for server in servers:
        r = requests.post('{}/api/client/servers/{}/power'.format(baseurl, server), json={"signal": "start"}, headers=headers)
        if r.text == "":
            print("\33[33m[Notice] \33[37m> \33[32mServer successfully started.")
        else:
            print("\33[33m[Notice] \33[37m> \33[31mGot a different response. [%s] with [%s]" % (r.status_code, r.text))
    time.sleep(120)
