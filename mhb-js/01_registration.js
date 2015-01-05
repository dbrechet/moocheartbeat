
    var data = d3.json("mhb-data/01_registration-data.json", function(error, data){
    var chart = AmCharts.makeChart("chartdiv", data);
    });