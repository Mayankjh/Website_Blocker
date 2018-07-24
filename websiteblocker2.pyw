# Run this script as root
 
import time
from datetime import datetime as dt
 
# change hosts path according to your OS
hosts_temp =r"D:\Python Training\Day 7\website blocker\hosts\hosts"
hosts_path =r"C:\Windows\System32\drivers\etc\hosts"
# localhost's IP
redirect = "127.0.0.1"
 
# websites That you want to block
website_list =["www.facebook.com","google.com","https://google.com","facebook.com","dub119.mail.live.com","www.dub119.mail.live.com","www.gmail.com","gmail.com"]
 
while True:
 
    # time of your work
    if dt(dt.now().year, dt.now().month, dt.now().day,9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    # mapping hostnames to your localhost IP address
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
 
            # removing hostnmes from host file
            file.truncate()
 
        print("Fun hours...")
    time.sleep(5)