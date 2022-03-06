$(function () {
  $("#data").DataTable({
    responsive: true,
    autoWidth: false,
    destroy: true,
    deferRender: true,
    ajax: {
      url: window.location.pathname,
      type: "POST",
      data: {
        action: "searchdata",
      }, // parametros
      dataSrc: "",
    },
    columns: [
      { "data": "id" },
      { "data": "nombre" },
      { "data": "activo" },
      { "data": "id" },
    ],
    columnDefs: [
      {
        targets: [-2],
        class: "text-center",
        orderable: false,
        render: function (data, type, row) {
          if (data == true) {
            return '<span class="badge badge-success"> Activo </span> ';
          } else {
            return '<span class="badge badge-danger"> Inactivo </span> ';
          }
        },
      },
      {
        targets: [-1],
        class: "text-center",
        orderable: false,
        render: function (data, type, row) {
          let buttons = '<a href="/erp/habitacion/piso/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
          buttons += '<a href="/erp/habitacion/piso/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
          return buttons;
        },
      },
    ],
    initComplete: function (settings, json) { },
    // se ejecuta al haber cargado la tabla
  });
});
