
//Eliminar nomiação
function eliminar_nomiacao(ids){
  const pk = ids
  const url ='/pessoal_quadro/eliminar_nomiacao/';
  
  const swalWithBootstrapButtons = Swal.mixin({
    confirmButtonClass: 'btn btn-success',
    cancelButtonClass: 'btn btn-danger',
    buttonsStyling: false,
  })
  
  swalWithBootstrapButtons.fire({
    title: 'Tens acerteza ?',
    text: "sera removidos todos os dados!",
    type: 'warning',
    showCancelButton: true,
    confirmButtonText: 'Sim, Eliminar!',
    cancelButtonText: 'Não,  Cancelar!',
    reverseButtons: true
  }).then((result) => {
    if (result.value) {
      swal({
        preConfirm: (ids) => {
          return fetch(url,{
            method: 'POST', 
            headers: {
              'X-CSRFToken': getCookie("csrftoken"),
              'Accept': 'application/json',
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            },
            body: JSON.stringify({'id': pk }),
          })
            .then(response => {
              if (!response.ok) {
                throw new Error(response.statusText)
              }
              return response.json()
            })
            .catch(error => {
              swal.showValidationError(
                `Permisão negada! erro`
              )
            })
        }
      }).then((result) => {
        if (result.value.validade) {
          swalWithBootstrapButtons.fire(
            `Eliminação:`,
            'Dados eliminado com sucesso.',
            'success'
          ),
          setTimeout("location.reload(true);",2000); // 5 segundos
          //window.location.reload();
        } else  {
          swalWithBootstrapButtons.fire(
            'Erro !',
            'Não foi possivel',
            'warning'
          )
        }
      })
    } else if (
      // Read more about handling dismissals
      result.dismiss === Swal.DismissReason.cancel
    ) {
      swalWithBootstrapButtons.fire(
        'Cancelado',
        'Cancelada a operação',
        'error'
      )
    }
  })

}



// Eliminar processo Disciplinar
function eliminar_processoDisciplinar(ids){
  const pk = ids
  const url ='/pessoal_quadro/eliminar_processo_disciplinar/';
  
  const swalWithBootstrapButtons = Swal.mixin({
    confirmButtonClass: 'btn btn-success',
    cancelButtonClass: 'btn btn-danger',
    buttonsStyling: false,
  })
  
  swalWithBootstrapButtons.fire({
    title: 'Tens acerteza ?',
    text: "sera removidos todos os dados!",
    type: 'warning',
    showCancelButton: true,
    confirmButtonText: 'Sim, Eliminar!',
    cancelButtonText: 'Não,  Cancelar!',
    reverseButtons: true
  }).then((result) => {
    if (result.value) {
      swal({
        preConfirm: (ids) => {
          return fetch(url,{
            method: 'POST', 
            headers: {
              'X-CSRFToken': getCookie("csrftoken"),
              'Accept': 'application/json',
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            },
            body: JSON.stringify({'id': pk }),
          })
            .then(response => {
              if (!response.ok) {
                throw new Error(response.statusText)
              }
              return response.json()
            })
            .catch(error => {
              swal.showValidationError(
                `Permisão negada! erro`
              )
            })
        }
      }).then((result) => {
        if (result.value.validade) {
          swalWithBootstrapButtons.fire(
            `Eliminação:`,
            'Dados eliminado com sucesso.',
            'success'
          ),
          setTimeout("location.reload(true);",2000); // 5 segundos
          //window.location.reload();
        } else  {
          swalWithBootstrapButtons.fire(
            'Erro !',
            'Não foi possivel',
            'warning'
          )
        }
      })
    } else if (
      // Read more about handling dismissals
      result.dismiss === Swal.DismissReason.cancel
    ) {
      swalWithBootstrapButtons.fire(
        'Cancelado',
        'Cancelada a operação',
        'error'
      )
    }
  })

}




// FUNÇÃO QUE VAI MANDAR O CODIGO PARA ELIMINAR DESPROMOÇÃO
function remover_despromocao(ids){
  const pk = ids
  const url ='/pessoal_quadro/remover_despromocao/';
  swal({
    title: 'Deseja eliminar os dados?',
    html: '<b>Digita o codigo de Segurança..!</b>',
    input: 'password',
    inputAttributes: {
      maxlength: 9,
      autocapitalize: 'off'
    },
    confirmButtonColor: '#009688',
    cancelButtonColor: '#d33',
    showCancelButton: true,
    confirmButtonText: 'Enviar',
    cancelButtonText: 'Cancelar',
    footer: '<a href>SIGRH-CPL</a>',
    reverseButtons: true,
    preConfirm: (codigo) => {
      return fetch(url,{
        method: 'POST', 
        headers: {
          'X-CSRFToken': getCookie("csrftoken"),
          'Accept': 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        },
        body: JSON.stringify({'codigo': codigo, 'id': pk }),
      })
        .then(response => {
          if (!response.ok) {
            throw new Error(response.statusText)
          }
          return response.json()
        })
        .catch(error => {
          swal.showValidationError(
            `Permisão negada! erro`
          )
        })
    },
    inputValidator: (codigo) => {
      return !codigo && 'campo não pode ser vazio!'
    },
  }).then((result) => {
    if (result.value.validade) {

      swal({
        type: 'success',
        title: 'Removido com sucesso',
        confirmButtonText: 'OK',
        footer: '<a href>SIGRH-CPL</a>',
      }),
      setTimeout("location.reload(true);",2000); // 2 segundos
      //window.location.reload();
    } else  {
      swal({
        type: 'error',
        title: 'Operação cancelada..!',
        html: '<b>Acesso Negado, sem permisão..!</b>',
        footer: '<a href>SIGRH-CPL</a>',
      })
    }
  })

}



// FUNÇÃO QUE VAI MANDAR O CODIGO PARA ELIMINAR A BAIXA
function eliminar_baixas(ids){
  const pk = ids
  const url ='/pessoal_quadro/eliminar_baixa/';
  
  const swalWithBootstrapButtons = Swal.mixin({
    confirmButtonClass: 'btn btn-success',
    cancelButtonClass: 'btn btn-danger',
    buttonsStyling: false,
  })
  
  swalWithBootstrapButtons.fire({
    title: 'Tens acerteza ?',
    text: "sera removidos todos os dados!",
    type: 'warning',
    showCancelButton: true,
    confirmButtonText: 'Sim, Eliminar!',
    cancelButtonText: 'Não,  Cancelar!',
    reverseButtons: true
  }).then((result) => {
    if (result.value) {
      swal({
        preConfirm: (ids) => {
          return fetch(url,{
            method: 'POST', 
            headers: {
              'X-CSRFToken': getCookie("csrftoken"),
              'Accept': 'application/json',
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            },
            body: JSON.stringify({'id': pk }),
          })
            .then(response => {
              if (!response.ok) {
                throw new Error(response.statusText)
              }
              return response.json()
            })
            .catch(error => {
              swal.showValidationError(
                `Permisão negada! erro`
              )
            })
        }
      }).then((result) => {
        if (result.value.validade) {
          swalWithBootstrapButtons.fire(
            `Eliminação:`,
            'Dados eliminado com sucesso.',
            'success'
          ),
          setTimeout("location.reload(true);",2000); // 5 segundos
          //window.location.reload();
        } else  {
          swalWithBootstrapButtons.fire(
            'Erro !',
            'Não foi possivel',
            'warning'
          )
        }
      })
    } else if (
      // Read more about handling dismissals
      result.dismiss === Swal.DismissReason.cancel
    ) {
      swalWithBootstrapButtons.fire(
        'Cancelar',
        'Operação Cancelada',
        'error'
      )
    }
  })

}



// FUNÇÃO QUE VAI MANDAR O CODIGO PARA ELIMINAR A REFORMA ANTICIPADA
function eliminar_reforma_anticipada(ids){
  const pk = ids
  const url ='/pessoal_quadro/eliminar_reforma_anticipada/';
  
  const swalWithBootstrapButtons = Swal.mixin({
    confirmButtonClass: 'btn btn-success',
    cancelButtonClass: 'btn btn-danger',
    buttonsStyling: false,
  })
  
  swalWithBootstrapButtons.fire({
    title: 'Tens acerteza ?',
    text: "sera removidos todos os dados!",
    type: 'warning',
    showCancelButton: true,
    confirmButtonText: 'Sim, Eliminar!',
    cancelButtonText: 'Não,  Cancelar!',
    reverseButtons: true
  }).then((result) => {
    if (result.value) {
      swal({
        preConfirm: (ids) => {
          return fetch(url,{
            method: 'POST', 
            headers: {
              'X-CSRFToken': getCookie("csrftoken"),
              'Accept': 'application/json',
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            },
            body: JSON.stringify({'id': pk }),
          })
            .then(response => {
              if (!response.ok) {
                throw new Error(response.statusText)
              }
              return response.json()
            })
            .catch(error => {
              swal.showValidationError(
                `Permisão negada! erro`
              )
            })
        }
      }).then((result) => {
        if (result.value.validade) {
          swalWithBootstrapButtons.fire(
            `Eliminação:`,
            'Dados eliminado com sucesso.',
            'success'
          ),
          setTimeout("location.reload(true);",2000); // 5 segundos
          //window.location.reload();
        } else  {
          swalWithBootstrapButtons.fire(
            'Erro !',
            'Não foi possivel',
            'warning'
          )
        }
      })
    } else if (
      // Read more about handling dismissals
      result.dismiss === Swal.DismissReason.cancel
    ) {
      swalWithBootstrapButtons.fire(
        'Cancelar',
        'Operação Cancelada',
        'error'
      )
    }
  })

}








function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
