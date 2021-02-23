import requests
import json
import sys
import os
import subprocess

try:
    import prettytable
    os.system('clear')
except:
    print("[*]PrettyTable module not found\n[*]Trying to install it...\n")
    python = sys.executable
    try:
        subprocess.check_call([python, '-m', 'pip', 'install', 'prettytable'], stdout=subprocess.DEVNULL)
        import prettytable
        input("Installed succesfully! Press enter to continue...")
        os.system('clear')
    except:
        print("Could not be installed...Exiting Program...")
        quit()


intro = """
   _____       _                   _ _                  _____            _            
  / ____|     | |                 (_) |                / ____|          | |           
 | (___  _   _| |__  ___  ___ _ __ _| |__   ___ _ __  | (___   ___  _ __| |_ ___ _ __ 
  \___ \| | | | '_ \/ __|/ __| '__| | '_ \ / _ \ '__|  \___ \ / _ \| '__| __/ _ \ '__|
  ____) | |_| | |_) \__ \ (__| |  | | |_) |  __/ |     ____) | (_) | |  | ||  __/ |   
 |_____/ \__,_|_.__/|___/\___|_|  |_|_.__/ \___|_|    |_____/ \___/|_|   \__\___|_|   
                                by Jael Gonzalez                                                                                      
                                                      
[*]Script that extracts the amount of subscribers of all the channels listed
[*]The data is organized in a table from highest sub count to lower sub count

[!]For the script to work you need a Youtube API KEY
"""
print(intro+'\n')
API_Key = "USER API KEY" ###API KEY
headers={
    'Accept-Language': 'en-US,en;q=0.5'
}

###DICTIONARY OF ALL THE CHANNELS 
channel_ids = {
'CHANNEL NAME': 'CHANNEL ID'
}


subs_dictonary={}

#Extracting data
for channel_name, channel_id in channel_ids.items():
    subscribers = requests.get(f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={API_Key}').json()['items'][0]['statistics']['subscriberCount']
    subs_dictonary[channel_name]=int(subscribers)


sorted_list = sorted(subs_dictonary.items(), key=lambda x: x[1])
sorted_list.reverse()

#Creating pretty table to sort data
table = prettytable.PrettyTable()
table.field_names = ['Rank', 'Name', ' Subscribers']
print("\nSubscriber count [Highest to lowest]\n")

count=1
for channel_name, subs in sorted_list:
    table.add_row([f'#{count}', channel_name, subs])
    count+=1
print(table)
print("Exiting Program...")