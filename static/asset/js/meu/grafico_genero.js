/**
 * @File   : grafico_genero.js
 * @Author : Gunza Ismael (7ilipe@gmail.com)
 * @Link   : 
 * @Date   : 2019-3-7 15:05:46
 */

var total_masculino = $('#total_masculino').text();
var total_femenino = $('#total_femenino').text();
var total_selecionado = $('#total_selecionado').text();
    Highcharts.chart('genero_container', {
        chart: {
            type: 'pie',
                options3d: {
                enabled: true,
                alpha: 45
        }
        },
        title: {
            text: 'Estatistica por genero de agentes selecionados'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                innerSize: 100,
                depth: 45,
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
                ['Genero Masculino', Number(total_masculino) ],
                ['Genero Femenino', Number(total_femenino) ],
                ['Agentes Selecionados', Number(total_selecionado)],
                
            ]
        }]

    });


