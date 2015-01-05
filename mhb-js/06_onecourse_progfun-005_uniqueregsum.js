
        var data = d3.json("mhb-data/06_onecourse_progfun-005_uniqueregsum.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });