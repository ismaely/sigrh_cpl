/**
 * @File   : graficos.js
 * @Author : Gunza Ismael (7ilipe@gmail.com)
 * @Link   : 
 * @Date   : 2019-3-5 00:01:39
 */



var total_transfe = $('#total_transfe').text();
var total_troca = $('#total_troca').text();
    Highcharts.chart('trans_container', {
        chart: {
            type: 'pie',
            options3d: {
                enabled: true,
                alpha: 45,
                beta: 0
            }
        },
        title: {
            text: 'Estatistica de Transferência e Troca'
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
                name: 'Transferência',
                y: Number(total_transfe),
                sliced: true,
                selected: true
            }, {
                name: 'Trocas',
                y: Number(total_troca),
                sliced: true,
                selected: true
            }, {
                name: 'Agentes',
                y: 10.85
            }]
        }]

    });


