
        var data = d3.json("../mhb-data/onecourse_intropoojava-001_uniqueregsum_nostack.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });