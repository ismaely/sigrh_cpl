/**
 * @File   : transferencia.js
 * @Author : Gunza Ismael (7ilipe@gmail.com)
 * @Link   : 
 * @Date   : 2018-10-17 13:59:14
 */

// função que vai solicitar o codigo de segurança pra remover pedido de transferencia
function remover_pedido_transferencia(ids){
    const pk = ids
    const url ='/transferencia/remover_pedido_transferencia/';
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
          'Cancelado a operação',
          'error'
        )
      }
    })

};



//função que vai solicitar para aprovar o pedido
function aprovar_transferencia(ids){
    const pk = ids
    const url ='/transferencia/aprovar_transferencia/';
    swal({
        title: 'Deseja remover o pedido?',
        html: 
        ' <label class="black-text"> <h6><b>Digita o codigo se segurança</b></h6> </label>'+
        '<input type="password" id="swal-input1" class="swal2-input black-text">' +
        ' <label class="black-text"> <h6><b>Digita o Dispacho</b></h6> </label>'+
        '<input id="swal-input2" class="swal2-input black-text">',
        
        confirmButtonColor: '#009688',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Enviar',
        cancelButtonText: 'Cancelar',
        showCancelButton: true,
        footer: '<a href>SIGRH-CPL</a>',
        showLoaderOnConfirm: true,
        preConfirm: () => {
          return fetch(url,{
            method: 'POST', 
            headers: {
              'X-CSRFToken': getCookie("csrftoken"),
              'Accept': 'application/json',
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            },
            body: JSON.stringify({'codigo': document.getElementById('swal-input1').value, 
            'dispacho': document.getElementById('swal-input2').value, 'id': pk }),
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
        allowOutsideClick: () => !swal.isLoading()
      }).then((result) => {
        if (result.value.validade) {
          swal({
            type: 'success',
            title: 'Transferencia aprovada com sucesso',
            confirmButtonText: 'OK',
            footer: '<a href>SIGRH-CPL</a>',
          }),
          setTimeout("location.reload(true);",2000); 
        }
        else{
          swal({
            type: 'error',
            title: 'Operação cancelada..!',
            html: '<b>Acesso Negado, sem permisão..!</b>',
            footer: '<a href>SIGRH-CPL</a>',
          })
            //console.log(result.value.msg)
        }
      });

};


// zona para eleminar documento 
function eliminar_documento(ids){
  const pk = ids
  const url ='/documentacao/eliminar_documento/';
  swal({
      title: 'Deseja remover arquivo?',
      html: '<b>Digita o codigo de Segurança..!</b>',
      input: 'password',
      inputAttributes: {
        maxlength: 9,
        autocapitalize: 'off'
      },
      confirmButtonColor: '#009688',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Enviar',
      cancelButtonText: 'Cancelar',
      showCancelButton: true,
      footer: '<a href>SIGRH-CPL</a>',
      showLoaderOnConfirm: true,
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
      inputValidator: (login) => {
        return !login && 'campo não pode ser vazio!'
      },
      allowOutsideClick: () => !swal.isLoading()
    }).then((result) => {
      if (result.value.validade) {
        swal({
          type: 'success',
          title: 'Removido com sucesso',
          confirmButtonText: 'OK',
          footer: '<a href>SIGRH-CPL</a>',
        }),
        setTimeout("location.reload(true);",2000); 
      }
      else{
        swal({
          type: 'error',
          title: 'Operação cancelada..!',
          html: '<b>Acesso Negado, sem permisão..!</b>',
          footer: '<a href>SIGRH-CPL</a>',
        })
      }
    });

};


// zona relacionado a formação

function remover_conclusao(ids){
  const pk = ids
  const url ='/formacao/remover_conclusao/';
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
        'Cancelado a operação',
        'error'
      )
    }
  })

};



// função que vai pedir o codigo para eliminar o agente na lista de selecionado
function remover_agente_selecionado(ids){
const pk = ids
const url ='/formacao/remover_agente_selecionado/';
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
      'Cancelado a operação',
      'error'
    )
  }
})

};




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
  