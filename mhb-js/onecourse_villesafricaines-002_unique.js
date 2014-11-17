
        var data = d3.json("../mhb-data/onecourse_villesafricaines-002_unique.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });