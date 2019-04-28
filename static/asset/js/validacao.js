$(function(){
var nome_pessoal = $('#id_nome');
var nome_pai = $('#id_nome_pai');
var nome_mae = $('#id_nome_mae');
var data_nascimento = $('#id_data_nascimento');
var genero = $('#id_genero');
var bi = $('#id_bi');
var residencia = $('#id_residencia');
var casa_numero = $('#id_casa_numero');
var telefone = $('#id_telefone');
var email = $('#id_email');
var numero_contribuite = $('#id_numero_contribuite');
var numero_caixa_social = $('#id_numero_caixa_social');
var numero_agente = $('#id_numero_agente');
var nivel_academico = $('#id_nivel_academico');
var curso = $('#id_curso');
var patente = $('#id_patente');
var numero_agente = $('#id_numero_agente');
var nip = $('#id_nip');
var data_igresso = $('#id_data_igresso');
var funcao = $('#id_funcao');
var bi_agente = $('.bi_agente');
var datas = $('#id_data'); // vai validar todas data para não ter ano maior
var formacao_bi_idade = $('.formacao_bi_idade');
var caracter_nao = /[\(\)\<\>\,\?\´\;\:\\\/\"\[\]]/;
var nao_aceite = /[\(\)\<\>\&\;\*\#/\|\[\@\]\´\(\"\$\{\|\|\+\?\'\%\^\}\@\!\=\£\\]/;
var regex_data = /^\d{1,2}\/\d{1,2}\/\d{4}$/;
var regex_nip = new RegExp("^[a-zA-Z]{1}\[0-9]{7}$"); // expressao que vai validar o NIP-> apenas uma letra e sete numero
var regex_bi_agente = new  RegExp("^[0-9]{9}\[a-zA-Z]{2}\[0-9]{3}$");
var regex_numero_agente = RegExp('^[0-9]');
var data_atual = new Date();


var vetor_provincia = ["Luanda", "Bengo", "Benguela","Bié","Cabinda","Cunene","Huambo","Huila","Cuando Cubango",
"Cuanza norte","Cuanza sul","Lunda Norte","Lunda sul","Malange", "Moxico","Namibe","Uige","Zaire"];
var mascara_bi = ["999999999LA999", "999999999BO999","999999999BA999","999999999BE999", "999999999CA999", "999999999CE999", "999999999HO999",
"999999999HA999", "999999999CC999", "999999999CN999", "999999999CS999", "999999999LN999", "999999999LS999", "999999999ME999", "999999999MO999",
"999999999NA999","999999999UE999", "999999999ZE999"];

var mascara_nif = ["999999999LA9999", "999999999BO9999","999999999BA9999","999999999BE9999", "999999999CA9999", "999999999CE9999", "999999999HO9999",
"999999999HA9999", "999999999CC9999", "999999999CN9999", "999999999CS9999", "999999999LN9999", "999999999LS9999", "999999999ME9999", "999999999MO9999",
"999999999NA9999","999999999UE9999", "999999999ZE9999"];



/** Mascara por default*/
$("input.bi_mask").mask("999999999LA999");
$("input.nif_mask").mask("999999999LA9999");


//campos desativados por default
$('#id_curso').attr("disabled","disabled");




// funçoes qunado click ou passa o mau
nome_pessoal.blur(validar_nome);
nome_pai.blur(validar_nomePai);
nome_mae.blur(validar_nomeMae);
email.change(validar_email);
residencia.keyup(validar_residencia);
casa_numero.blur(validar_numeroCasa);
data_nascimento.change(validar_dataNascimento);

numero_caixa_social.blur(validar_numero_caixa_social);
curso.keyup(validar_curso);
funcao.blur(validar_funcao);
datas.blur(validar_datas_gerais);
//formacao_bi_idade.blur(validar_bi_consultarIdade);

data_igresso.keyup(validar_data_igresso);
bi_agente.keyup(validar_bi_numeroAgente);
//nip.keyup(validar_nip);
telefone.keyup(validar_telefone);



// função que chamar para alterar a mascar do BI quando escolher provincia
$('#id_provincia').click(validar_provinciaBi);
$('#id_nivel_academico').click(validar_nivelAcademico);


if($('#id_nivel_academico').val() != '8ªClasse'){
    $('#id_curso').removeAttr('disabled');
    return true;
}





//$('#id_nip').click(validar_nip);


// validr o nome completo apenas letras
nome_pessoal.bind("keydown", function (evento) {
    var keycode = evento.which;
    var isStandard = (keycode > 47 && keycode < 58);
    var isOther = (",8,46,37,38,39,40,".indexOf("," + keycode + ",") > -1);
    if (!isStandard || isOther) {
        return true;
    } else {
        return false;
    }
});

//validar o nome do pai apenas letra
nome_pai.bind("keydown", function (evento) {
    var keycode = evento.which;
    var isStandard = (keycode > 47 && keycode < 58);
    var isOther = (",8,46,37,38,39,40,".indexOf("," + keycode + ",") > -1);
    if (!isStandard || isOther) {

        return true;
    } else {

        return false;
    }
});

//validar o nome da mae apenas letras
nome_mae.bind("keydown", function (evento) {
    var keycode = evento.which;
    var isStandard = (keycode > 47 && keycode < 58);
    var isOther = (",8,46,37,38,39,40,".indexOf("," + keycode + ",") > -1);
    if (!isStandard || isOther) {

        return true;
    } else {

        return false;
    }
});

// permitir apenas entra numero no curso
curso.bind("keydown", function (evento) {
    var keycode = evento.which;
    var isStandard = (keycode > 47 && keycode < 58);
    var isOther = (",8,46,37,38,39,40,".indexOf("," + keycode + ",") > -1);
    if (!isStandard || isOther) {

        return true;
    } else {

        return false;
    }
});



//validar apenas numero da caixa Social
numero_caixa_social.bind("keydown", function (evento) {
       var keycode = evento.which;
       var isStandard = (keycode > 47 && keycode < 58);
       var isOther = (",8,46,37,38,39,40,".indexOf("," + keycode + ",") > -1);
       if (isStandard || isOther) {
           return true;
       } else {
           return false;
       }
});


// para validar a entrada so d nummero
nip.bind("keydown", function (evento) {
    var keycode = evento.which;
    var isStandard = (keycode > 47 && keycode < 58);
    var isOther = (",8,46,37,38,39,40,".indexOf("," + keycode + ",") > -1);
    if (isStandard || isOther) {
        return true;
    } else {
        return false;
    }
});

// validar apenas entrada de numero para agente
numero_agente.bind("keydown", function (evento) {
      var keycode = evento.which;
      var isStandard = (keycode > 47 && keycode < 58);
      var isOther = (",8,46,37,38,39,40,".indexOf("," + keycode + ",") > -1);
      if (isStandard || isOther) {
          return true;
      } else {
          return false;
      }
});




function validar_datas_gerais(){
    var ano_data, dia, mes, idade, vetor_data, ano_atual;
    ano_atual = data_atual.getFullYear();

    if (datas.val() != ' '){

        if(regex_data.test($('#id_data').val())){
            vetor_data = datas.val().split("/");
            dia = parseInt(vetor_data[0], 10);
            mes = parseInt(vetor_data[1], 10);
            ano_data = parseInt(vetor_data[2], 10);

            if(dia > 32 || mes > 12 || ano_data == ano_atual || ano_data > ano_atual || ano_data < 1850){
                $('#id_data').parent().children("span").text("A Data não é valida").show();
                datas.focus();
                return false;
            }

            else{
                $("#id_data").parent().children("span").text("").hide();
                return true;
            }

        }

    }
    else{
        $("#id_data").parent().children("span").text("").hide();
        return false;
    }

}


// validar o nome completo para não entra  apenas uma letra
function validar_nome(){
    if($.trim($('#id_nome').val()).length < 5 ){
        $('#id_nome').parent().children("span").text("O Nome Não e valido").show();
        nome_pessoal.focus();
        return false;
    }
    else{
        $("#id_nome").parent().children("span").text("").hide();
        return true;

    }
}

// validar o nome completo do pai para não entra  apenas uma letra
function validar_nomePai(){

    if($.trim($('#id_nome_pai').val()).length < 5 ){
        $('#id_nome_pai').parent().children("span").text("O Nome Não e valido").show();

        nome_pai.focus();
        return false;
    }

    else{
        $("#id_nome_pai").parent().children("span").text("").hide();
        return true;

    }
}

// validar o nome completo da mae oara para não entra  apenas uma letra
function validar_nomeMae(){
    if($.trim($('#id_nome_mae').val()).length < 5 ){
        $('#id_nome_mae').parent().children("span").text("O Nome Não e valido").show();
        nome_mae.focus();
        return false;
    }
    else{
        $("#id_nome_mae").parent().children("span").text("").hide();
        return true;

    }
}



// validar o email
function validar_email(){
    var regex =  new RegExp(/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/);
    var valor = email.val()
    if(email.val() != ''){
        if(!regex.test(email.val()) || valor.match(caracter_nao)){
            $('#id_email').parent().children("span").text("O E-mail não é valido").show();
            return false;
        }
        else{
            $("#id_email").parent().children("span").text("").hide();
            return true;
        }
    }
    else{
        $("#id_email").parent().children("span").text("").hide();
        return true;
    }
}



// validar o numero da casa
function validar_numeroCasa(){

    if(casa_numero.val() != ''){

        if(casa_numero.val() === ' ' || casa_numero.val().length < 2 || casa_numero.val().match(nao_aceite)){
            $('#id_casa_numero').parent().children("span").text("o numero da casa não é valido").show();
            return false;
        }else{
            $("#id_casa_numero").parent().children("span").text("").hide();
            return true;
        }
    }
    else{
        $("#id_casa_numero").parent().children("span").text("").hide();
        return true;
    }

}

// validar a residencia
function validar_residencia(){
     var valor = residencia.val();
    if(residencia.val().length == 0 ||  valor.match(nao_aceite) || residencia.val().length < 5 || residencia.val() === '' || /^\s+$/.test(residencia.val())){
        $('#id_residencia').parent().children("span").text("A residencia não é valida").show();
        return false;
    }
    else{
        $("#id_residencia").parent().children("span").text("").hide();
        return true;
    }
}


// função que seleciona a provincia e atrbui a sigla da provincia no campo de BI
function validar_provinciaBi(){
    for (var i = 0; i < vetor_provincia.length; i++) {
        if ($('#id_provincia').val() == vetor_provincia[i]) {
              $("input.bi_mask").mask(mascara_bi[i]);
              $("input.nif_mask").mask(mascara_nif[i]);
              break;
            return true;
        }

    }

}

// validar data de nascimento
function validar_dataNascimento(){
    var ano_data, dia, mes, idade, vetor_data, ano_atual;
    ano_atual = data_atual.getFullYear();

    if (data_nascimento.val() != ''){

        if(regex_data.test(data_nascimento.val())){
            vetor_data = data_nascimento.val().split("/");
            dia = parseInt(vetor_data[0], 10);
            mes = parseInt(vetor_data[1], 10);
            ano_data = parseInt(vetor_data[2], 10);
            idade = ano_atual - ano_data;
            if( ano_data == ano_atual || ano_data > ano_atual || ano_data < 1550 || idade <= 17 ){
                $('#id_data_nascimento').parent().children("span").text("A Data não é valida. Menor d idade.").show();
                //data_nascimento.focus();
                return false;
            }
            else{
              
                    $("#id_data_nascimento").parent().children("span").text("").hide();
                    return true;
                
            }
        }

    }else{
        data_nascimento.focus();
        return false;
    }
}

// validar data de igresso na policia
function validar_data_igresso(){
    var ano_data, dia, mes, idade, vetor_data, ano_atual, vetor_dataNasci, anoNasci, ano_maior;
    ano_atual = data_atual.getFullYear();
    vetor_dataNasci = data_nascimento.val().split("/");
    anoNasci = parseInt(vetor_dataNasci[2], 10);

    if (data_igresso.val() != ' '){
        if(regex_data.test(data_igresso.val())){
            vetor_data = data_igresso.val().split("/");
            dia = parseInt(vetor_data[0], 10);
            mes = parseInt(vetor_data[1], 10);
            ano_data = parseInt(vetor_data[2], 10);
            idade = ano_atual - ano_data;
            if(dia > 32 || mes > 12 || ano_data > ano_atual || ano_data < 1600){
                $('#id_data_igresso').parent().children("span").text("A Data de igresso não é valida..").show();
                data_igresso.focus();
                return false;
             }
             if (idade < 15) {
                $('#id_data_igresso').parent().children("span").text("É Menor de idade, não é permitido").show();
                data_igresso.focus();
                return false;
            }
            else{
                if(ano_data == vetor_dataNasci){
                    $('#id_data_igresso').parent().children("span").text("A data de igresso não pode ser igual a data de nascimento").show();
                    data_igresso.focus();
                    return false;
                }else{
                    $("#id_data_igresso").parent().children("span").text("").hide();
                    return true;
                }
            }
        }

    }else{
        data_igresso.focus();
        return false;
    }
}

// validar numero da caixa social
function validar_numero_caixa_social(){
    if (numero_caixa_social.val() != '') {
        if (numero_caixa_social.val().length > 3) {
            $("#id_numero_caixa_social").parent().children("span").text("").hide();
            return true;
        }
        else {
            $('#id_numero_caixa_social').parent().children("span").text("O numero não é valido").show();
            nome_mae.focus();
            return false;
        }
    }
    else {
        $("#id_numero_caixa_social").parent().children("span").text("").hide();
        return true;
    }

}

// validar o nivel_academico e o curso
function validar_nivelAcademico(){
 if ($('#id_nivel_academico').val() == '8ªClasse') {
     $('#id_curso').val(" ");
     $('#id_curso').attr("disabled","disabled");
     return true;
 }
 else {
     $('#id_curso').removeAttr('disabled');
     return true;
 }

}



// validar o curso para não aceita valor menor que 5
function validar_curso(){
    if ($('#id_curso').val().length > 5 ) {
        $("#id_curso").parent().children("span").text("").hide();
        return true;
    }
    else {
        $('#id_curso').parent().children("span").text("Não é valido").show();
        //curso.focus();
        return false;
    }
}



// validar a função para não entra simbolos
function validar_funcao(){
    var valor = funcao.val();
    if ($('#id_funcao').val() != '') {
        if(valor.match(nao_aceite) || funcao.val().length < 5 ){
            $('#id_funcao').parent().children("span").text("A Função do agente não é valida").show();
            return false;
        }
        else{
            $("#id_funcao").parent().children("span").text("").hide();
            return true;
        }
    }
    else{
        $("#id_funcao").parent().children("span").text("").hide();
        return true;
    }

}

/** function validar_nip(){
    if (nip.val() != ''){
        if(!regex_nip.test(nip.val())){
            $('#id_nip').parent().children("span").text("O nip não é valido").show();
            return false;
        }
        else{
            $("#id_nip").parent().children("span").text("").hide();
            return true;
        }
    }
    else{
        $("#id_nip").parent().children("span").text("").hide();
        return true;
    }
}  */



//FUNÇÃO QUE VAI VALIDAR BI E NUMERO DO AGENTE
function validar_bi_numeroAgente(){
    if($('.bi_agente').val().length == 14){

        if(!regex_bi_agente.test($('.bi_agente').val())){
            $('.bi_agente').parent().children("span").text("O Bi não é valido").show();
            return false;
         }
         else{
            $(".bi_agente").parent().children("span").text("").hide();
            return true;
        }
  }
}

function validar_telefone(){
    var telef = $('#id_telefone').val().charAt(7);
    if (telef != '2' && telef != '9') {
        $('#bi_telefone').parent().children("span").text("O campo telefone deve começar com número 9 ou 2 apenas").show();
            return false;
    }
    else{
        $("#bi_telefone").parent().children("span").text("").hide();
        return true;
    }


 }




})
