
        var data = d3.json("../mhb-data/onecourse_structures-003_uniqueregsum_activity_xy.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });