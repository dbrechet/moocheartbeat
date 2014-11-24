
        var data = d3.json("../mhb-data/onecourse_structures-001_combined.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });