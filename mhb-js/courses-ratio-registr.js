
        var data = d3.json("../mhb-data/courses-ratio-registr.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });