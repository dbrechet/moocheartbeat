
        var data = d3.json("mhb-data/04_onecourse_linearopt-002_combined.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });