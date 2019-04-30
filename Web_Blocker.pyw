# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:05:01 2019

@author: khaled.yacoubi
"""

#%reset -f
#%clear

# Import libraries
import time
from datetime import datetime as dt

hosts_temp_path = "hosts"
hosts_path  = ""+"hosts"
redirect = "127.0.0.1"
website_list = ["facebook.com","www.facebook.com",'fuq.com','www.fuq.com']

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,0) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,9):
        print("Working Hours, Stop Playing !!!")
        with open(hosts_temp_path,'r+') as file:
            hosts_file = file.read()
            for website in website_list:
                if website in hosts_file:
                    pass
                else:
                    file.write("\n"+"#"+7*" "+redirect+7*" "+website)
    else:
        print('Fun hours, you can do whatever you want!!')
        with open(hosts_temp_path,"r+") as file:
            hosts_file = file.readlines()
            file.seek(0)
            for line in hosts_file:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)