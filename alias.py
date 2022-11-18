from espkey import *

[ids, timestamps] = read_databases()

cont = True
while cont:
    timestamp = input("Enter the timestamp for scan-in (MM/DD/YYYY HH:MM:SS): ")
    name = input("Enter the name of the person who scanned in: ")
    add_name(ids, timestamps, timestamp, name)
    
    cont = input("Continue? [y/n] ") == 'y'

write_databases(ids, timestamps)