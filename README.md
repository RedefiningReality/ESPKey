# ESPKey
Python scripts for easily importing ESPKey logs and storing them to json databases for further modification. I'll write a more comprehensive README later, but for now, here's what we've got:

### The Idea
Here's the idea: You want to collect a bunch of IDs from your dorm building's front desk RFID scanner - joking obviously ;), I'd totally never do something that devious... not in a million years... Anyway, you have an ESPKey installed on an RFID reader that uses the Wiegand protocol. Optionally, you also have a screen you can see that displays some information about users when they scan in including the date/time of the scan in and the scanner's name. The ESPKey logs themselves are messy to read and don't have an actual date/time timestamp (just seconds since startup). I wrote a script (update.py) that will import a log file and use its information to create two separate JSON databases, one with scan information (timestamp and ID number) and another with valid ID information (valid ID numbers and corresponding names that you will then provide). To get the actual date/time for the timestamp, you must provide the time for the *first* scan that was caught in the log. You'd get this by looking at the screen or scanning in right after starting the ESPKey and noting the time. If you fuck up and forget to do that, obviously you can't add to your scan information database since it includes timestamps, but you can still collect valid IDs and add to your database of valid ID information. In this case, use johnfuckedup.py because you fucked up and your name is now John. You manually add corresponding names to specific ID numbers with alias.py. It will prompt for the timestamp of a known scan followed by the name of the user who scanned in. This should be displayed on the screen as previously mentioned. If you want to prettily print the names of users and their corresponding ID numbers or list times that those users scanned in, that's what print.py is for. If all this sounds confusing, just look at the Usage section below.

### Files
- [espkey.py](espkey.py) - library to be imported by other scripts
- [update.py](update.py) - used to update both databases
- [johnfuckedup.py](johnfuckedup.py) - used to update only the database of valid IDs (not the database of scan times)
- [alias.py](alias.py) - used to associate a name with an ID given a known scan time and the name of the person who scanned in
- [print.py](print.py) - prints out the JSON databases

### Usage

#### Save IDs and Scan Times
Note: requires knowing date and time of first scan after startup
1. Save ESPKey log to `log.txt` and place it in the same directory as update.py
2. Run `python3 update.py`
3. Enter the date and time of the first scan after startup

#### Associate person's name with an ID
Note: requires knowing the date and time of a scan that is in the database and the name of the person who scanned in
1. Run `python3 print.py`
2. Enter 2 to print timestamps and ID scans
3. Check date and time of known scan and see if you find one that's close (within 1-2 seconds) listed
   - For step 5, *use the date and time of the scan found by running print.py* -> it might be off from the actual time of the scan by 1 or 2 seconds
4. Run `alias.py`
5. Enter the date and time of the scan found in step three
6. Enter the name of the person you'd like to associate with this ID

#### Save IDs only
1. Save ESPKey log to `log.txt` and place it in the same directory as johnfuckedup.py
2. Run `python3 johnfuckedup.py`
