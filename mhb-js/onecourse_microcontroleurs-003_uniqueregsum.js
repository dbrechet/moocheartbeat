
        var data = d3.json("../mhb-data/onecourse_microcontroleurs-003_uniqueregsum.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });