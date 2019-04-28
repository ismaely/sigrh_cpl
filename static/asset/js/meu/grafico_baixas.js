
/**
 * @File   : grafico_baixas.js
 * @Author : Gunza Ismael (7ilipe@gmail.com)
 * @Link   : 
 * @Date   : 2019-3-7 00:53:35
 */

var total_Reforma = $('#total_Reforma').text();
var total_Demissao = $('#total_Demissao').text();
var total_Transferencia = $('#total_Transferencia').text();
var total_Falecimento = $('#total_Falecimento').text();
var total_Dificiencia = $('#total_Dificiencia').text();
var total_Invalidez = $('#total_Invalidez').text();
var total_Outro = $('#total_Outro').text();
var total_baixas = $('#total_baixas').text();


Highcharts.chart('baixa_container', {
    chart: {
        type: 'cylinder',
        options3d: {
            enabled: true,
            alpha: 15,
            beta: 15,
            depth: 50, 
            viewDistance: 30
        }
        },
    title: {
        text: 'Estatística das Baixas Registadas'
    },
    xAxis: {
        categories: ['Reforma', 'Demissão', 'Transferencia', 'Falecimento', 'Dificiencia', 'Invalidez','Outras'],
        labels: {
            skew3d: true,
            style: {
                fontSize: '14px'
            }
        }
    },
    
    plotOptions: {
        series: {
            depth: 25,
            colorByPoint: true
        }
        
    },
   
    series: [{
        name: 'Percentagem',
        showInLegend: false,
        
        data: [{
            name: 'Reforma',
            y: Number(total_Reforma )
        }, {
            name: 'Demissão',
            y: Number(total_Demissao)
        }, {
            name: 'Transferencia',
            y: Number(total_Transferencia)
        },
        {
            name: 'Falecimento',
            y: Number(total_Falecimento)
        },
        {
            name: 'Dificiencia',
            y: Number(total_Dificiencia)
        },
        {
            name: 'Invalidez',
            y: Number(total_Invalidez)
        },
        {
            name: 'Outras',
            y: Number(total_Outro)
        }
        
    ]
    }]

 });

