
        var data = d3.json("../mhb-data/onecourse_intro-java-fr-001_uniqueregsum_activity_xy.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });