
    var data = d3.json("mhb-data/01_lecture_view_total-data.json", function(error, data){
    var chart = AmCharts.makeChart("chartdiv", data);
    });