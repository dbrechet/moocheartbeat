
        var data = d3.json("mhb-data/14_onecourse_intro-cpp-fr-001_uniqueregsum_activity_xy.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });