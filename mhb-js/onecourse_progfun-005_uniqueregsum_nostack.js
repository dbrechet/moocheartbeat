
        var data = d3.json("../mhb-data/onecourse_progfun-005_uniqueregsum_nostack.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });