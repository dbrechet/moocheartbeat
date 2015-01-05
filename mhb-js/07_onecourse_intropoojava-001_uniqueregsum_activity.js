
        var data = d3.json("mhb-data/07_onecourse_intropoojava-001_uniqueregsum_activity.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });