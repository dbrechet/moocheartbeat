var data = d3.json("registration-data.json", function(error, data){
var chart = AmCharts.makeChart("chartdiv", data);
});