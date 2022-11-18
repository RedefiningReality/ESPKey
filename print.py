from espkey import *

to_print = input("Enter database to print:\n1 => IDs and Names\n2 => Timestamps and ID Scans\n")
id_name = to_print == '1'

[ids, timestamps] = read_databases()

if id_name:
    [count, known] = print_database(ids)
    print()
    print("Total number of IDs:", count)
    print("Number of known IDs:", known)
else:
    [count, known] = print_timestamps(ids, timestamps)
    print()
    print("Total number of scan-ins:", count)
    print("Number of scan-ins from known ID:", known)