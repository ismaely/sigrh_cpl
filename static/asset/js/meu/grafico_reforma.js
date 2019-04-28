
/**
 * @File   : grafico_reforma.js
 * @Author : Gunza Ismael (7ilipe@gmail.com)
 * @Link   : 
 * @Date   : 2019-3-7 01:30:43
 */


var total_anticipada = $('#total_anticipada').text();
var total_normal = $('#total_normal').text();
var total_reforma = $('#total_reforma').text();
    Highcharts.chart('reforma_container', {
        chart: {
            type: 'pie',
            options3d: {
                enabled: true,
                alpha: 46,
                beta: 0
            }
        },
        title: {
            text: 'Estatistica de agentes na reforma'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                depth: 35,
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                }
            }
        },

        series: [{
            name: 'Percentagem',
            colorByPoint: true,
            data: [{
                name: 'Reforma Normal',
                y: Number(total_normal),
                sliced: true,
                selected: true
            }, {
                name: 'Reforma Anticipada',
                y: Number(total_anticipada),
                sliced: true,
                selected: true
            }, {
                name: 'Total na Reforma',
                y: Number(total_reforma),
                
            }]
        }]

    });


