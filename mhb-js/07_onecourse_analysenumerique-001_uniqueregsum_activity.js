
        var data = d3.json("mhb-data/07_onecourse_analysenumerique-001_uniqueregsum_activity.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });