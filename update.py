from espkey import *
import os
from datetime import datetime

log = 'log.txt'
"""
url = "http://192.168.4.1/log.txt"
download(url, log)

url = "http://192.168.4.1/restart"
get(url)
"""

[ids, timestamps] = read_databases()

start_date = input("Enter startup date/time (MM/DD/YYYY HH:MM:SS): ")
start = datetime.strptime(start_date, timestamp_format)
read_log(ids, timestamps, log, start)
os.remove(log)

write_databases(ids, timestamps)