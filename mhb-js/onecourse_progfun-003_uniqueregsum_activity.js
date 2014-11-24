
        var data = d3.json("../mhb-data/onecourse_progfun-003_uniqueregsum_activity.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });