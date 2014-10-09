#!/usr/bin/env python
#title           :mhb_csvtodb.py
#description     :This will take all csv for a directory and put the data in a database.
#author          :dbrechet
#date            :2014109
#version         :0.1
#usage           :python mhb_csvtodb.py
#notes           :
#python_version  :2.7.6  
#==============================================================================

# Import the modules needed to run the script.
import sys
import csv
import os
from datetime import datetime
from time import mktime
import MySQLdb

def insertFromDict(table, dict):
    """Take dictionary object dict and produce sql for 
    inserting it into the named table"""
    sql = 'INSERT INTO ' + table
    sql += ' ('
    sql += ', '.join(dict)
    sql += ') VALUES ('
    sql += ', '.join(map(dictValuePad, dict))
    sql += ');'
    return sql

def dictValuePad(key):
    return '%(' + str(key) + ')s'

# Open a folder
path = "/Users/brechet/Git-Repo/MOOCHeartBeat/weekly-sessions-files/"
dirs = os.listdir(path)

# This would print all the files and directories
for afile in dirs:
    print afile
    if afile == ".DS_Store":
        continue
        
    sampling = afile[:6]
    session = afile[7:-4]
    
    # Transpose csv
    pathfilein = os.path.join(path, afile)
    pathfileout = os.path.join(path, "tranps-" + afile)
    with open(pathfilein) as f:
        reader = csv.reader(f)
        cols = []
        for row in reader:
            cols.append(row)

    with open(pathfileout, 'wb') as f:
        writer = csv.writer(f)
        for i in range(len(max(cols, key=len))):
            writer.writerow([(c[i] if i<len(c) else '') for c in cols])
    
    #add two columns sampling and session
    pathfileinbis = pathfileout
    pathfileoutbis = os.path.join(path, "col-" + afile)
    with open(pathfileinbis,'r') as csvinput:
        with open(pathfileoutbis, 'wb') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)
            all = []
            row = next(reader)
            row.append('session')
            row.append('sampling')
            row.append('itemunixtime')
            all.append(row)

            for row in reader:
                row.append(session)
                row.append(sampling)
                item = datetime.strptime(row[0], "%Y-%m-%d")
                itemunixtime = mktime(item.timetuple())
                row.append(itemunixtime)
                all.append(row)

            writer.writerows(all)
            
    
    #dictionaire of the csv file.
    dictreader = csv.DictReader(open(pathfileoutbis, "rb"), dialect="excel") # Python 2.x
    
    #db = MySQLdb.connect(host='localhost', user='mhbuser', passwd='mhb23', db='moocheartbeat') 
    #cursor = db.cursor()
    insert_dict = dictreader
    sql = insertFromDict("mhb_coursera", insert_dict)
    print sql
    #cursor.execute(sql, insert_dict)
    
    #for row in dictreader:
    #    print(row)
    
    
    os.remove(pathfileout)