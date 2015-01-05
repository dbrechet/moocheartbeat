
        var data = d3.json("mhb-data/05_courses-ratio.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });