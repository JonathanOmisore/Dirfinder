import requests
from scanner import scan
def main():
    url = input("Enter the website url \n")
    dirs = input("enter directories, comma seperated \n")
    agent = ""
    listdirs =  dirs.split(",")
    askagent = input("Add a custom user agent? (Y/N) \n")
    if askagent == "Y" or "y":
        inputagent = input ("Enter user agent")
        agent = inputagent
        
    scan(url, listdirs, agent)
    
    
    

if __name__ == "__main__":
    main()
