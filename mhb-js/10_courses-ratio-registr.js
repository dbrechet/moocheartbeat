
        var data = d3.json("mhb-data/10_courses-ratio-registr.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });