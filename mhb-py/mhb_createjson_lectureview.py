#!/usr/bin/env python
#title           :mhb_createjson_lectureview.py
#description     :This will make a query to the database and create a json file to store the data. The data is lecture_view_total.
#author          :dbrechet
#date            :20141014
#version         :0.1
#usage           :python mhb_createjson_lectureview.py
#notes           :
#python_version  :2.7.6  
#==============================================================================

# Import the modules needed to run the script.
import sys
import os
import MySQLdb
import io
import json
from datetime import datetime
from time import mktime
from array import *

# Create dict structure of the json file.
data_dict_name =[]
data_dict_value = []
# genneral info 
data_dict_name.append("type")
data_dict_value.append("serial")
data_dict_name.append("theme")
data_dict_value.append("none")
data_dict_name.append("pathToImages")
data_dict_value.append("http://www.amcharts.com/lib/3/images/")

#legend
item_name = []
item_value = []
item_name.append("equalWidths")
item_value.append("false")
item_name.append("periodValueText")
item_value.append("total: [[value.sum]]")
item_name.append("position")
item_value.append("top")
item_name.append("valueAlign")
item_value.append("left")
item_name.append("valueWidth")
item_value.append(100)
legend_dict = dict(zip(item_name, item_value))
data_dict_name.append("legend")
data_dict_value.append(legend_dict)

# dataProvider
# Open database connection
db = MySQLdb.connect(host='localhost', user='mhbuser', passwd='mhb23!', db='moocheartbeat')

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql_item = """SELECT item 
                 FROM mhb_coursera 
                 WHERE 1 
                 GROUP BY item ORDER BY item ASC"""

cursor.execute(sql_item)
rows = cursor.fetchall()
datadict = []
for row in rows:
    data_item = row[0].isoformat()
    
    sql_session = "SELECT session, lecture_view_total FROM mhb_coursera WHERE item = '" + data_item + "' ORDER BY session ASC"
    cursor.execute(sql_session)
    rows_session = cursor.fetchall()
    sessions = []
    regs = []
    sessions.append ('item')
    regs.append (data_item)
    for row_s in rows_session:
        sessions.append(row_s[0])
        regs.append (int(row_s[1]))
    sess_dict = dict(zip(sessions, regs))
    datadict.append(sess_dict)
                  
data_dict_name.append("dataProvider")
data_dict_value.append(datadict)

#valueAxes
list_va = []
item_va_name = []
item_va_value = []
item_va_name.append("stackType")
item_va_value.append("regular")
item_va_name.append("gridAlpha")
item_va_value.append(0.07)
item_va_name.append("position")
item_va_value.append("left")
item_va_name.append("title")
item_va_value.append("Lecture view Total")
va_dict = dict(zip(item_va_name, item_va_value))
list_va.append(va_dict)
data_dict_name.append("valueAxes")
data_dict_value.append(list_va)

#"graphs"
dict_graphs =[]
sql_sessions = "SELECT distinct(session) FROM mhb_coursera WHERE 1"
cursor.execute(sql_sessions)
rows_sessions = cursor.fetchall()
for row_ses in rows_sessions:
    item_graph_name = []
    item_graph_value = []
    item_graph_name.append("balloonText")
    item_graph_value.append("<span style='font-size:10px; color:#000000;'><b>[[title]]: [[value]]</b></span>")
    item_graph_name.append("fillAlphas")
    item_graph_value.append(0.6)
    item_graph_name.append("lineAlpha")
    item_graph_value.append(0.4)
    item_graph_name.append("title")
    item_graph_value.append(row_ses[0])
    item_graph_name.append("valueField")
    item_graph_value.append(row_ses[0])
    dict_graph = dict(zip(item_graph_name,item_graph_value))
    dict_graphs.append(dict_graph)
data_dict_name.append("graphs")
data_dict_value.append(dict_graphs)

data_dict_name.append("plotAreaBorderAlpha")
data_dict_value.append(0)
data_dict_name.append("marginTop")
data_dict_value.append(10)
data_dict_name.append("marginLeft")
data_dict_value.append(0)
data_dict_name.append("marginBottom")
data_dict_value.append(0)

#"chartScrollbar"
item_chartScrollbar_name = []
item_chartScrollbar_value = []
dict_chartScrollbar = dict(zip(item_chartScrollbar_name, item_chartScrollbar_value))
data_dict_name.append("chartScrollbar")
data_dict_value.append(dict_chartScrollbar)

#"chartCursor"
item_chartCursor_name = ["cursorAlpha"]
item_chartCursor_value = [0]
dict_chartCursor = dict(zip(item_chartCursor_name, item_chartCursor_value))
data_dict_name.append("chartCursor")
data_dict_value.append(dict_chartCursor)

data_dict_name.append("categoryField")
data_dict_value.append("item")

#"categoryAxis"
item_categoryAxis_name = []
item_categoryAxis_value = []
item_categoryAxis_name.append("startOnAxis")
item_categoryAxis_value.append("true")
item_categoryAxis_name.append("axisColor")
item_categoryAxis_value.append("#DADADA")
item_categoryAxis_name.append("gridAlpha")
item_categoryAxis_value.append(0.07)
dict_categoryAxis = dict(zip(item_categoryAxis_name, item_categoryAxis_value))
data_dict_name.append("categoryAxis")
data_dict_value.append(dict_categoryAxis)

data_dict = dict(zip(data_dict_name, data_dict_value))
#print json.dumps(data_dict, sort_keys=True, indent=4, separators=(',', ': '))
with io.open('lecture_view_total-data.json', 'w', encoding='utf-8') as f:
    f.write(unicode(json.dumps(data_dict, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)))

                  
#data_dict_name.append()
#data_dict_value.append()
# disconnect from server
db.close()