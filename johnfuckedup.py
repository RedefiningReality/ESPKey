import os
import json

db_ids = 'databases/ids.json'

def read_log(ids, path):
    if os.path.isfile(path):
        lines = open(path, 'r').readlines()
        for line in lines:
            content = line[line.index(' ')+1:]
            if content.endswith('\n'):
                content = content[:-1]
            
            if content == "Starting up!" or content == "Restart requested by user.":
                continue
            
            if content not in ids:
                ids[content] = ""
    return ids

def read_database(path):
    if os.path.isfile(path):
        file = open(path, 'r')
        return json.load(file)
    else:
        return {}

def read_databases():
    ids = read_database(db_ids)
    return ids
    
def write_database(db, path):
    if os.path.isfile(path):
        os.remove(path)
    file = open(path, 'w')
    json.dump(db, file)

def write_databases(ids):
    write_database(ids, db_ids)

def print_database(db):
    count = 0
    valexist = 0
    for key, value in db.items():
        print(key, '-', value)
        if value != '':
            valexist += 1
        count += 1
    return [count, valexist]

log = 'log.txt'

ids = read_databases()

read_log(ids, log)
os.remove(log)

write_databases(ids)