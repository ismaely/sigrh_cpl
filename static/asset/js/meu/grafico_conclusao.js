/**
 * @File   : grafico_selecionado.js
 * @Author : Gunza Ismael (7ilipe@gmail.com)
 * @Link   : 
 * @Date   : 2019-3-7 02:13:03
 */

var total_bolsaInterna= $('#total_bolsaInterna').text();
var total_bolsaExterna = $('#total_bolsaExterna').text();
var total_desistente = $('#total_desistente').text();
var total_aprovados = $('#total_aprovados').text();
var total_reprovado = $('#total_reprovado').text();
var total_conclusao = $('#total_conclusao').text();

    Highcharts.chart('conclusao_container', {
        chart: {
            type: 'pie',
                options3d: {
                enabled: true,
                alpha: 45
        }
        },
        title: {
            text: 'Estatistica de agentes que concluiram a formação'
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
                ['Desistente', Number(total_desistente) ],
                ['Aprovados', Number(total_aprovados) ],
                ['Reprovados', Number(total_reprovado) ]
            ]
        }]

    });


