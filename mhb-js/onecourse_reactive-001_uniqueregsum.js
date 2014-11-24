
        var data = d3.json("../mhb-data/onecourse_reactive-001_uniqueregsum.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });