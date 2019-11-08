
/**
 * @File   : grafico_reforma.js
 * @Author : Gunza Ismael (7ilipe@gmail.com)
 * @Link   : 
 * @Date   : 2019-3-7 01:30:43
 */


var total_anticipada = $('#total_anticipada').text();
var total_Incapacidade = $('#total_Incapacidade').text();
var total_acidente = $('#total_acidente').text();
var total_dificiencia = $('#total_dificiencia').text();
var total_outro = $('#total_outro').text();
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
            data: [
                {
                name: 'Incapacidade',
                y: Number(total_Incapacidade),
                sliced: true,
                selected: true
            }, {
                name: 'Acidente',
                y: Number(total_acidente),
                sliced: true,
                selected: true
            },
             {
                name: 'Dificiencia',
                y: Number(total_dificiencia),
                sliced: true,
                selected: true
            },
             {
                name: 'Outros',
                y: Number(total_outro),
                sliced: true,
                selected: true
            }
        ]
        }]

    });


