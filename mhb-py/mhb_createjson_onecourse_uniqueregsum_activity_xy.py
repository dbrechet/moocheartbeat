#!/usr/bin/env python
#title           :mhb_createjson_onecourse_uniqueregsum_activity_xy.py
#description     :This will make a query to the database and create a json file to store the data. The data is all interaction in one session.
#author          :dbrechet
#date            :20141014
#version         :0.1
#usage           :python mhb_createjson_onecourse_uniqueregsum_activity_xy.py
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

# Open database connection
db = MySQLdb.connect(host='localhost', user='mhbuser', passwd='mhb23!', db='moocheartbeat')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Search diffrenent sessions
sql_session = """SELECT session 
                 FROM mhb_coursera 
                 WHERE 1 
                 GROUP BY session ORDER BY session ASC"""

cursor.execute(sql_session)
rows_session = cursor.fetchall()
datadict = []

for row_session in rows_session:
    data_session = row_session[0]
    print data_session
    

    # Create dict structure of the json file.
    data_dict_name =[]
    data_dict_value = []
    # general info 
    data_dict_name.append("type")
    data_dict_value.append("xy") #"xy" "serial"
    data_dict_name.append("theme")
    data_dict_value.append("none")
    data_dict_name.append("pathToImages")
    data_dict_value.append("http://www.amcharts.com/lib/3/images/")
    #data_dict_name.append("mouseWheelZoomEnabled")
    #data_dict_value.append("true")
    #data_dict_name.append("plotAreaBorderAlpha")
    #data_dict_value.append(0)
    data_dict_name.append("marginTop")
    data_dict_value.append(10)
    data_dict_name.append("marginLeft")
    data_dict_value.append(0)
    data_dict_name.append("marginBottom")
    data_dict_value.append(0)
    #data_dict_name.append("categoryField")
    #data_dict_value.append("item")

    #"chartScrollbar"
    item_chartScrollbar_name = []
    item_chartScrollbar_value = []
    #item_chartScrollbar_name.append("autoGridCount")
    #item_chartScrollbar_value.append("true")
    #item_chartScrollbar_name.append("graph")
    #item_chartScrollbar_value.append("g_reg")
    #item_chartScrollbar_name.append("scrollbarHeight")
    #item_chartScrollbar_value.append(40)
    
    dict_chartScrollbar = dict(zip(item_chartScrollbar_name, item_chartScrollbar_value))
    data_dict_name.append("chartScrollbar")
    data_dict_value.append(dict_chartScrollbar)

    #"chartCursor"
    item_chartCursor_name = []
    item_chartCursor_value = []
    #item_chartCursor_name.append("cursorAlpha")
    #item_chartCursor_value.append(0)
    #item_chartCursor_name.append("cursorPosition")
    #item_chartCursor_value.append("mouse")
    
    dict_chartCursor = dict(zip(item_chartCursor_name, item_chartCursor_value))
    data_dict_name.append("chartCursor")
    data_dict_value.append(dict_chartCursor)

    #"categoryAxis"
    item_categoryAxis_name = []
    item_categoryAxis_value = []
    #item_categoryAxis_name.append("startOnAxis")
    #item_categoryAxis_value.append("true")
    #item_categoryAxis_name.append("axisColor")
    #item_categoryAxis_value.append("#DADADA")
    #item_categoryAxis_name.append("gridAlpha")
    #item_categoryAxis_value.append(0.07)
    #item_categoryAxis_name.append("parseDates")
    #item_categoryAxis_value.append("true")
    #item_categoryAxis_name.append("twoLineMode")
    #item_categoryAxis_value.append("true")
    #item_categoryAxis_name.append("minPeriod")
    #item_categoryAxis_value.append("7DD")
    
    dict_categoryAxis = dict(zip(item_categoryAxis_name, item_categoryAxis_value))
    #data_dict_name.append("categoryAxis")
    #data_dict_value.append(dict_categoryAxis)
    
    #legend
    item_name = []
    item_value = []
    item_name.append("equalWidths")
    item_value.append("false")
    item_name.append("periodValueText")
    item_value.append("total: [[value.sum]]")
    item_name.append("position")
    item_value.append("left")
    item_name.append("valueAlign")
    item_value.append("left")
    item_name.append("valueWidth")
    item_value.append(100)
    
    legend_dict = dict(zip(item_name, item_value))
    #data_dict_name.append("legend")
    #data_dict_value.append(legend_dict)

    # dataProvider
    #sql_item = """SELECT item, registrations, assignment_unique, forum_combined_unique, forum_comment_unique, forum_post_unique,
    #                  lecture_combined_unique, lecture_download_unique, lecture_view_unique, quiz_exam_unique, quiz_homework_unique,
    #                  quiz_quiz_unique, quiz_survey_unique, quiz_video_unique, work_combined_unique
    #                  FROM mhb_coursera 
    #                  WHERE session='"""+data_session+"' ORDER BY item ASC"
    sql_item = """SELECT item, registrations, assignment_unique + forum_comment_unique + forum_post_unique + 
                        lecture_download_unique + lecture_view_unique + quiz_exam_unique + quiz_homework_unique + 
                      quiz_quiz_unique + quiz_survey_unique + quiz_video_unique + work_combined_unique as activity
                      FROM mhb_coursera 
                      WHERE session='"""+data_session+"' ORDER BY item ASC"

    cursor.execute(sql_item)
    rows = cursor.fetchall()
    columns = list( [d[0].decode('utf8') for d in cursor.description] )
    #columns.append("activity_rel")
    columns = tuple(columns)
    datadict = []
    regs = 0 
    for row in rows:
        row = list(row)
        row[0] = mktime(row[0].timetuple())
        regs = regs + row[1]
        row[1] = regs
        diff_ract = regs-row[2]
        ract = regs - diff_ract
        regact = regs - ract
        #row.append(regact)
        rcnt = len(row) 
        cnt = rcnt -1
        while (cnt > 0):
            row[cnt]= int(row[cnt])
            cnt = cnt - 1
        row = tuple(row)
        datadict.append(dict(zip(columns, row)))    
    data_dict_name.append("dataProvider")
    data_dict_value.append(datadict)
    
    #valueAxes
    list_va = []
    item_va_name = []
    item_va_value = []
    #item_va_name.append("stackType")
    #item_va_value.append("regular")
    #item_va_name.append("gridAlpha")
    #item_va_value.append(0.07)
    item_va_name.append("axisAlpha")
    item_va_value.append(0)
    item_va_name.append("position")
    item_va_value.append("left")
    #item_va_name.append("title")
    #item_va_value.append(data_session)
    va_dict = dict(zip(item_va_name, item_va_value))
    list_va.append(va_dict)
    data_dict_name.append("valueAxes")
    data_dict_value.append(list_va)

    #"graphs"
    dict_graphs =[]
    #sql_sessions = "SELECT distinct(session) FROM mhb_coursera WHERE 1"
    #cursor.execute(sql_sessions)
    #rows_sessions = cursor.fetchall()
    #for row_ses in columns:
    #    if row_ses != "item":
    item_graph_name = []
    item_graph_value = []
    #        if row_ses == "registrations":
    #            item_graph_name.append("id")
    #            item_graph_value.append("g_reg")
    item_graph_name.append("balloonText")
    item_graph_value.append("x:<b>[[item]]</b> y:<b>[[registrations]]</b><br>value:<b>[[activity]]</b>")
    item_graph_name.append("bullet")
    item_graph_value.append("bubble")
    item_graph_name.append("lineAlpha")
    item_graph_value.append(0)
    item_graph_name.append("valueField")
    item_graph_value.append("activity")
    item_graph_name.append("xField")
    item_graph_value.append("item")
    item_graph_name.append("yField")
    item_graph_value.append("registrations")
    item_graph_name.append("fillAlphas")
    item_graph_value.append(0)
    item_graph_name.append("bulletBorderAlpha")
    item_graph_value.append(0.2)
    item_graph_name.append("maxBulletSize")
    item_graph_value.append(80)        
    #        item_graph_name.append("balloonText")
    #        item_graph_value.append("<span style='font-size:10px; color:#000000;'><b>[[title]]: [[value]]</b></span>")
    #        item_graph_name.append("fillAlphas")
    #        item_graph_value.append(0.6)
    #        item_graph_name.append("lineAlpha")
    #        item_graph_value.append(0.4)
    #        item_graph_name.append("type")
    #        item_graph_value.append("column")
            #item_graph_name.append("lineThickness")
            #item_graph_value.append(2)
            #item_graph_name.append("bullet")
            #item_graph_value.append("round")
    #        item_graph_name.append("clustered")
    #        item_graph_value.append("false")
    #        item_graph_name.append("stackable")
    #        item_graph_value.append("false")
    #        item_graph_name.append("title")
    #        item_graph_value.append(row_ses)
    #        item_graph_name.append("valueField")
    #        item_graph_value.append(row_ses)
    dict_graph = dict(zip(item_graph_name,item_graph_value))
    dict_graphs.append(dict_graph)
    data_dict_name.append("graphs")
    data_dict_value.append(dict_graphs)

    data_dict = dict(zip(data_dict_name, data_dict_value))
    #print json.dumps(data_dict, sort_keys=True, indent=4, separators=(',', ': '))
    
    # create the json file.
    datafilename = '../mhb-data/onecourse_'+data_session+'_uniqueregsum_activity_xy.json'
    with io.open(datafilename, 'w', encoding='utf-8') as fd:
        fd.write(unicode(json.dumps(data_dict, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)))
    
    # create the js file.
    jsfilename ='../mhb-js/onecourse_'+data_session+'_uniqueregsum_activity_xy.js'
    jsmessage = """
        var data = d3.json("../mhb-data/onecourse_"""+data_session+"""_uniqueregsum_activity_xy.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });"""
    with io.open(jsfilename, 'w', encoding='utf-8') as fj:
        fj.write(unicode(jsmessage))
    
    # create the html file. 
    htmlfilename = '../test-onecourse_'+data_session+'_uniqueregsum_activity_xy.html'
    htmlmessage = """
    <!DOCTYPE html>
    <html>
	   <head>
            <title>uniqueregsum_activity_xy """+data_session+""" | amCharts</title>
            <meta name="description" content="chart created using amCharts" />

            <!-- amCharts javascript sources -->
            <script type="text/javascript" src="mhb-libscripts/amcharts.js"></script>
            <script type="text/javascript" src="mhb-libscripts/xy.js"></script>
            <script type="text/javascript" src="mhb-libscripts/none.js"></script>
            <script type="text/javascript" src="mhb-libscripts/d3.min.js"></script>

            <!-- amCharts javascript code -->
            <script type="text/javascript" src="mhb-js/onecourse_"""+data_session+"""_uniqueregsum_activity_xy.js"></script>
            <link rel="stylesheet" type="text/css" href="mhb-css/registration-chartered.css" media="screen" />
        </head>
	   <body>
		  <div id="chartdiv"></div>
	   </body>
       </html>
    """
    
    with io.open(htmlfilename, 'w', encoding='utf-8') as fh:
        fh.write(unicode(htmlmessage))

# disconnect from db server
db.close()