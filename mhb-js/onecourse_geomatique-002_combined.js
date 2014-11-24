
        var data = d3.json("../mhb-data/onecourse_geomatique-002_combined.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });