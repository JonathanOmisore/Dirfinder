import requests
def scan(url, dirs, agent):
    existingdirectories = []
    notexistingdirectories = []
    headers = {'user-agent': agent}
    for directory in dirs:
        websiteurl = url + "/" + directory
        r = requests.get(websiteurl, headers=headers)
        if(r.status_code != 404):
            existingdirectories.append(websiteurl + (" (Status code: " + str(r.status_code) + ")"))
        if(r.status_code == 404):
            notexistingdirectories.append(websiteurl)
    if existingdirectories:
        print("==========Discovered Directories=========== \n")
        for existingdirectory in existingdirectories:
            print(existingdirectory + "\n")
    if notexistingdirectories:
        print ("==========Notexistant Directories (404) =========== \n")
        for notexistingdirectory in notexistingdirectories:
            print(notexistingdirectory + " \n")
