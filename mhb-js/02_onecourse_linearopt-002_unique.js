
        var data = d3.json("mhb-data/02_onecourse_linearopt-002_unique.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });