$(document).ready(function() {
    $('#example').DataTable({
        language: {
            searchPlaceholder: 'Filtrar Dados',
            sSearch: '',
            sLengthMenu: 'Limites _MENU_',
            sLength: 'dataTables_length',
            oPaginate: {
                sFirst: '<i class="icon-backward"></i>',
                sPrevious: '<i class="icon-backward"></i>',
                sNext: '<i class="icon-forward"></i>',
                sLast: '<i class="icon-backward"></i>'
        }
        }
    });
    $('.dataTables_length select').addClass('browser-default');
});
