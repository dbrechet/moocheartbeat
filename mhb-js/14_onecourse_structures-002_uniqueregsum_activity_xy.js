
        var data = d3.json("mhb-data/14_onecourse_structures-002_uniqueregsum_activity_xy.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });