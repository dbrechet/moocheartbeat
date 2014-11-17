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

def insertFromDict(table, dicti):
    """Take dictionary object dict and produce sql for 
    inserting it into the named table"""
    sql = "INSERT INTO " + table
    sql += " ("
    sql += ", ".join(dicti)
    sql += ") VALUES ("
    sql += ", ".join(map(dictValuePad, dicti))
    sql += ");"
    return sql

def dictValuePad(key):
    return '%(' + str(key) + ')s'

# Open database connection
db = MySQLdb.connect(host='localhost', user='mhbuser', passwd='mhb23!', db='moocheartbeat')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS `mhb_coursera`")

# Create table as per requirement
sql = """CREATE TABLE IF NOT EXISTS `mhb_coursera` (
            `id` bigint(10) NOT NULL AUTO_INCREMENT,
            `item` date NOT NULL DEFAULT '1970-01-01',
            `assignment_total` int(10) DEFAULT NULL,
            `assignment_unique` int(10) DEFAULT NULL,
            `forum_combined_unique` int(10) DEFAULT NULL,
            `forum_comment_total` int(10) DEFAULT NULL,
            `forum_comment_unique` int(10) DEFAULT NULL,
            `forum_post_total` int(10) DEFAULT NULL,
            `forum_post_unique` int(10) DEFAULT NULL,
            `lecture_combined_total` int(10) DEFAULT NULL,
            `lecture_combined_unique` int(10) DEFAULT NULL,
            `lecture_download_total` int(10) DEFAULT NULL,
            `lecture_download_unique` int(10) DEFAULT NULL,
            `lecture_view_total` int(10) DEFAULT NULL,
            `lecture_view_unique` int(10) DEFAULT NULL,
            `quiz_exam_total` int(10) DEFAULT NULL,
            `quiz_exam_unique` int(10) DEFAULT NULL,
            `quiz_homework_total` int(10) DEFAULT NULL,
            `quiz_homework_unique` int(10) DEFAULT NULL,
            `quiz_quiz_total` int(10) DEFAULT NULL,
            `quiz_quiz_unique` int(10) DEFAULT NULL,
            `quiz_survey_unique` int(10) DEFAULT NULL,
            `quiz_survey_total` int(10) DEFAULT NULL,
            `quiz_video_total` int(10) DEFAULT NULL,
            `quiz_video_unique` int(10) DEFAULT NULL,
            `registrations` int(10) DEFAULT NULL,
            `work_combined_unique` int(10) DEFAULT NULL,
            `session` varchar(50) DEFAULT NULL,
            `sampling` varchar(50) DEFAULT NULL,
            `itemunixtime` int(10) DEFAULT NULL,
            PRIMARY KEY (`id`)
          ) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 """

cursor.execute(sql)

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
    #insert_dict = dictreader
    
    #
    
    for row in dictreader:
        #print(row)
        sql1 = insertFromDict("mhb_coursera", row)
        #print sql1 % row
        cursor.execute(sql1, row)
        
    os.remove(pathfileout)
    os.remove(pathfileoutbis)
# disconnect from server
db.close()
