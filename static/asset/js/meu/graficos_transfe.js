/**
 * @File   : graficos.js
 * @Author : Gunza Ismael (7ilipe@gmail.com)
 * @Link   : 
 * @Date   : 2019-3-5 00:01:39
 */



var masculino = $('#total_transfe_masculino').text();
var femenino = $('#total_transfe_femenino').text();
var total = $('#total_transferencia').text();
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
       
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                depth: 35,
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>:{point.y} ({point.percentage:.1f} %)',
                },
                showInLegend: true
                
            }
        },

        series: [{
            name: 'Percentagem',
            colorByPoint: true,
            data: [
                {
                name: 'Masculino',
                y: Number(masculino),
                sliced: true,
                selected: true
                },
                {
                name: 'Femenino',
                y: Number(femenino),
                sliced: true,
                selected: true
                }
               
            ]
        }]

    });


