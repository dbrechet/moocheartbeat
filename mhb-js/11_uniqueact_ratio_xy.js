
    var data = d3.json("mhb-data/11_uniqueact_ratio_xy.json", function(error, data){
    var chart = AmCharts.makeChart("chartdiv", data);
    });