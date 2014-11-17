
        var data = d3.json("../mhb-data/onecourse_initprogjava-001_unique.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });