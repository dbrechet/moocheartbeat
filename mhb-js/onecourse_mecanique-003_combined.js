
        var data = d3.json("../mhb-data/onecourse_mecanique-003_combined.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });