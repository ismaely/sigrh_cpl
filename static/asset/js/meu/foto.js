$(document).ready(function(){
    

    $(".preview_snapshot").on("click", function(){
        Webcam.attach('#camera_civel');
        document.getElementById('pre_take_buttons').style.display = 'none';
        document.getElementById('salvar_foto').style.display = '';
    });

    $(".cancel_preview").on("click", function(){
        Webcam.unfreeze();
        // swap buttons back
        document.getElementById('salvar_foto').style.display = '';
        document.getElementById('post_take_buttons').style.display = 'none';
    });
    
    $(".save_photo").on("click", function(){
        Webcam.snap(function(data_uri) {
            // display results in page
            //document.getElementById('id_foto_civil').value = data_uri;
            document.getElementById('fotoCivel').innerHTML =
                '' +
                '<img src="' + data_uri + '"/>';

            // swap buttons back
            //document.getElementById('pre_take_buttons').style.display = '';
            document.getElementById('salva1').value = data_uri;
            document.getElementById('post_take_buttons').style.display = '';
            document.getElementById('salvar_foto').style.display = 'none';
        });
    });

    



    $(".chama_camera").on("click", function(){
        Webcam.attach('#camera_fardada');
        //Webcam.freeze();
        
        document.getElementById('inicia_camera').style.display = 'none';
        document.getElementById('salvarFoto').style.display = '';
    });
    
    $(".cancela_foto").on("click", function(){
        Webcam.unfreeze();

        // swap buttons back
        document.getElementById('salvarFoto').style.display = '';
        document.getElementById('cancelar_novo').style.display = 'none';
    });


    $(".salva_fardado").on("click", function(){
        Webcam.snap(function(data_uri) {
            // display results in page
        document.getElementById('fotoFardado').innerHTML =
                '' +
                '<img src="' + data_uri + '"/>';

            // swap buttons back
            //document.getElementById('pre_take_buttons').style.display = '';
        document.getElementById('salva2').value = data_uri;
        document.getElementById('cancelar_novo').style.display = '';
        document.getElementById('salvarFoto').style.display = 'none';
        });
    });

   

});