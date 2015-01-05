
        var data = d3.json("mhb-data/03_onecourse_java-fr-2013-001_total.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });