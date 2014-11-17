var data = d3.json("../mhb-data/registration-data.json", function(error, data){
var chart = AmCharts.makeChart("chartdiv", data);
});