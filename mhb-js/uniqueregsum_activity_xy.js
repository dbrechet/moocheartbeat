
    var data = d3.json("mhb-data/uniqueregsum_activity_xy.json", function(error, data){
    var chart = AmCharts.makeChart("chartdiv", data);
    function formatCategory (value, formatedValue, categoryAxis){
        dt = new Date(value*1000);
        y = dt.getFullYear();
        m = dt.getMonth();
        d = dt.getDate();
        ndt = dt.toISOString();
        ndt = ndt.substr(0,10);
        return ndt;
    }
    });
    
    