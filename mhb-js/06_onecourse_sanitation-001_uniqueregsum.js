
        var data = d3.json("mhb-data/06_onecourse_sanitation-001_uniqueregsum.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });