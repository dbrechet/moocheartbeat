
        var data = d3.json("mhb-data/02_onecourse_structures-003_unique.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });