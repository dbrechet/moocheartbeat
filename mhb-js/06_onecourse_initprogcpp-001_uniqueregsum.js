
        var data = d3.json("mhb-data/06_onecourse_initprogcpp-001_uniqueregsum.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });