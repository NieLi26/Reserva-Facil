$(function () {

  $("#data").DataTable({
    // responsive: true,
    scrollX: true,
    autoWidth: false,
    destroy: true,
    deferRender: true,
    ajax: {
      url: window.location.pathname,
      type: "POST",
      data: {
        "action": "searchdata",
      }, // parametros
      dataSrc: "",
      headers: {
        'X-CSRFToken': csrftoken
      }
    },
    columns: [
      { "data": "id" },
      { "data": "reserva.user.full_name" },
      { "data": "reserva.habitacion.numero_habitacion" },
      { "data": "total" },
      { "data": "avance" },
      { "data": "resto" },
      { "data": "estado_pago" },
      { "data": "id" }
    ],
    columnDefs: [
      {
        targets: [-2],
        class: "text-center",
        orderable: false,
        render: function (data, type, row) {
          if (data == "pendiente") {
            return '<span class="badge badge-warning">' + data.toUpperCase() + '</span> ';
          } else if (data == "cancelado") {
            return '<span class="badge badge-success">' + data.toUpperCase() + '</span> ';
          } else {
            return '<span class="badge badge-danger">' + data.toUpperCase() + '</span> ';
          }

        },
      },
      {
        targets: [-1],
        class: "text-center",
        orderable: false,
        render: function (data, type, row) {
          let buttons = '<a href="/erp/reserva/pago/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
          buttons += '<a href="/erp/reserva/pago/delete/' + row.id + '/" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a> ';
          // buttons +=  '<a rel="details" class="btn btn-success btn-xs btn-flat"><i class="fas fa-search"></i></a>';
          return buttons;
        },
      },
    ],
    initComplete: function (settings, json) { },
    // se ejecuta al haber cargado la tabla
  });


});
