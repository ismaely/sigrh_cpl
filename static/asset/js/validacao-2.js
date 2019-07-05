$(function (){

var origem_primeiro = $('#id_origem_primeiro');
var destino_primeiro = $('#id_destino_primeiro');
var bi1 = $('#id_bi1');
var bi2 = $('#id_bi2');
var numero_guia = $('#id_numero_guia');
var tipoValidez = $('.tipoValidez');
var falecimento =  $('.falecimento');



$('#id_origem_segundo').attr("disabled","disabled");
$('#id_destino_segundo').attr("disabled","disabled");
$('#id_pais').attr("disabled","disabled");

$('#id_origem_primeiro').click(validar_origem_primeiro);
$('#id_destino_primeiro').click(validar_destino_primeiro);
$('#id_motivo_baixa').click(motivo_baixa_esclha);
$('#id_razao_posse').click(validar_bolsaEstudo);


//validar baixa
if ($('#id_motivo_baixa').val() == "Invalidez") {
    document.getElementById('tipoValidez').style.display = '';
    return true;
}
else{
    return false;
}

// validar formação bolsa
if($('#id_razao_posse').val() != 'Bolsa Interna'){
    $('#id_pais').removeAttr('disabled');
    return true;
}

// para validar a entrada so d nummero
bi1.bind("keydown", function (evento) {
    var keycode = evento.which;
    var isStandard = (keycode > 47 && keycode < 58);
    var isOther = (",8,46,37,38,39,40,".indexOf("," + keycode + ",") > -1);
    if (isStandard || isOther) {
        return true;
    } else {
        return false;
    }
});

// para validar a entrada so d numero troca
bi2.bind("keydown", function (evento) {
    var keycode = evento.which;
    var isStandard = (keycode > 47 && keycode < 58);
    var isOther = (",8,46,37,38,39,40,".indexOf("," + keycode + ",") > -1);
    if (isStandard || isOther) {
        return true;
    } else {
        return false;
    }
});

// transferencia recber so numero
numero_guia.bind("keydown", function (evento) {
    var keycode = evento.which;
    var isStandard = (keycode > 47 && keycode < 58);
    var isOther = (",8,46,37,38,39,40,".indexOf("," + keycode + ",") > -1);
    if (isStandard || isOther) {
        return true;
    } else {
        return false;
    }
});

 

function validar_bolsaEstudo(){
    if ($('#id_razao_posse').val() == 'Bolsa Interna') {
        $('#id_pais').val(" ");
        $('#id_pais').attr("disabled","disabled");
        $('#id_instituicao').removeAttr('disabled');
        return true;
    }
    else {
        $('#id_instituicao').val(" ");
        $('#id_instituicao').attr("disabled","disabled");
        $('#id_pais').removeAttr('disabled');
        return true;
    }
   
}


function motivo_baixa_esclha(){
    if ($('#id_motivo_baixa').val() == "Invalidez") {
        document.getElementById('tipoValidez').style.display = '';
        document.getElementById('falecimento').style.display = 'none';
        return true;
    }
    if ($('#id_motivo_baixa').val() == "Falecimento") {
        document.getElementById('tipoValidez').style.display = 'none';
        document.getElementById('falecimento').style.display = '';
        return true;
    }
    else{
        document.getElementById('tipoValidez').style.display = 'none';
        document.getElementById('falecimento').style.display = 'none';
        return false;
    }
   
 }



//validar orgão de origem 
function validar_origem_primeiro(){
    if ($('#id_origem_primeiro').val() != ' ') {
        //$('#id_destino_segundo').val($('#id_origem_primeiro').val());
        document.getElementById('id_destino_segundo').value = $('#id_origem_primeiro').val()
        //$('#id_destino_segundo').attr($('#id_origem_primeiro').val());
        return true;
    }
   
 }

 //validar orgão de destino 
function validar_destino_primeiro(){
    if ($('#id_destino_primeiro').val() != ' ') {
       // $('#id_origem_segundo').val($('#id_destino_primeiro').val());
        document.getElementById('id_origem_segundo').value = $('#id_destino_primeiro').val()
        //$('#id_origem_segundo').attr($('#id_destino_primeiro').val());
        //$('#id_curso').attr("disabled","disabled");
        return true;
    }
   
 }


})
