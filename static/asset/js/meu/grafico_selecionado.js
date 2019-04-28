/**
 * @File   : grafico_selecionado.js
 * @Author : Gunza Ismael (7ilipe@gmail.com)
 * @Link   : 
 * @Date   : 2019-3-7 02:13:03
 */

var total_bolsaInterna= $('#total_bolsaInterna').text();
var total_bolsaExterna = $('#total_bolsaExterna').text();
var total_masculino = $('#total_masculino').text();
var total_femenino = $('#total_femenino').text();
var total_selecionado = $('#total_selecionado').text();
    Highcharts.chart('selecionado_container', {
        chart: {
            type: 'pie',
                options3d: {
                enabled: true,
                alpha: 45
        }
        },
        title: {
            text: 'Estatistica de agentes selecionados para formação'
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
                ['Bolsa Externa', Number(total_bolsaExterna) ],
                ['Bolsa Interna', Number(total_bolsaInterna) ],
                ['Agentes Selecionados', Number(total_selecionado)],
                
            ]
        }]

    });


