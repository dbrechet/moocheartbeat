
        var data = d3.json("mhb-data/04_onecourse_initprogjava-001_combined.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });