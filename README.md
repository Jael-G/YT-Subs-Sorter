# Youtube Subscribers Sorter

Python script that exctracts all the channels indicated in a dictionary, and then sorts them from highest sub count to lowest sub count using the prettytable module. The script uses a Youtube Data API

# Libraries

The only library used that does not come with Python is prettytable. However, if when running the script prettytable is not installed, the script will install it before continuing to run

# Preview

![Alt Text](https://github.com/Jael-G/YT-Subs-Sorter/blob/main/Preview.png)

# Installation
Clone repository:

```
git clone https://github.com/Jael-G/YT-Subs-Sorter
```

Go into de repository file:
```
cd YT-Subs-Sorter
```


# Instructions
1) Change the ```API_KEY = "USER API KEY"``` to your own Youtube Data API key
2) Add all the channel names and channel IDs to the ``` channel_ids = { 'CHANNEL NAME' : 'CHANNEL ID'}``` dictionary
3) Run the script: ```python SubsSorter.py```. May vary depending the OS and Python version

