
        var data = d3.json("mhb-data/08_onecourse_java-fr-2013-001_uniqueregsum_nostack.json", function(error, data){
        var chart = AmCharts.makeChart("chartdiv", data);
        });