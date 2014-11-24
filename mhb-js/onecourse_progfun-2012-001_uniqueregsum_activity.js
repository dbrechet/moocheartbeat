
        var data = d3.json("../mhb-data/onecourse_progfun-2012-001_uniqueregsum_activity.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });