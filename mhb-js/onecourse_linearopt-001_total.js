
        var data = d3.json("../mhb-data/onecourse_linearopt-001_total.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });