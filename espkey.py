import requests
import os
from datetime import datetime
import json

timestamp_format = '%m/%d/%Y %H:%M:%S'

db_ids = 'databases/ids.json'
db_timestamps = 'databases/timestamps.json'

def get(url):
    return requests.get(url)

def download(url, path):
    response = get(url)
    open(path, 'wb').write(response.content)

def read_log(ids, timestamps, path, start_date):
    if os.path.isfile(path):
        start_time = start_date.timestamp()*1000.0
        init_time = 0
        
        lines = open(path, 'r').readlines()
        for line in lines:
            timestamp = line[:line.index(' ')]
            content = line[line.index(' ')+1:]
            if content.endswith('\n'):
                content = content[:-1]
            
            if content == "Starting up!" or content == "Restart requested by user.":
                init_time = start_time - int(timestamp)
                continue
            
            timestamp_raw = datetime.fromtimestamp((init_time+int(timestamp)+500.0)/1000.0)
            timestamp_formatted = timestamp_raw.strftime(timestamp_format)
            if content not in ids:
                ids[content] = ""
            timestamps[timestamp_formatted] = content
    return [ids, timestamps]

def read_database(path):
    if os.path.isfile(path):
        file = open(path, 'r')
        return json.load(file)
    else:
        return {}

def read_databases():
    ids = read_database(db_ids)
    timestamps = read_database(db_timestamps)
    return [ids, timestamps]
    
def write_database(db, path):
    if os.path.isfile(path):
        os.remove(path)
    file = open(path, 'w')
    json.dump(db, file)

def write_databases(ids, timestamps):
    write_database(ids, db_ids)
    write_database(timestamps, db_timestamps)

def print_database(db):
    count = 0
    valexist = 0
    for key, value in db.items():
        print(key, '-', value)
        if value != '':
            valexist += 1
        count += 1
    return [count, valexist]

def print_timestamps(ids, timestamps):
    count = 0
    valexist = 0
    for key, value in timestamps.items():
        print(key, ':', value, end='')
        if value in ids and ids[value] != '':
            print(" (" + ids[value] + ")")
            valexist += 1
        else:
            print()
        count += 1
    return [count, valexist]

def add_name(ids, timestamps, timestamp, name):
    ids[timestamps[timestamp]] = name