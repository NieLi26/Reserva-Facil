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
      // { "data": "position" },
      { "data": "id" },
      { "data": "nombre" },
      { "data": "id" },
    ],
    columnDefs: [
      {
        targets: [1],
        class: "text-center",
        orderable: false,
        render: function (data, type, row) {
          return data;
          // "<b style='color:red'>" + data + "</b>";
        },
      },
      {
        targets: [-1],
        class: "text-center",
        orderable: false,
        render: function (data, type, row) {
          let buttons = '<a href="/erp/habitacion/servicio/update/'+row.id+'/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
          buttons +=  '<a href="/erp/habitacion/servicio/delete/'+row.id+'/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
          return buttons;
        },
      },
    ],
    initComplete: function (settings, json) {},
    // se ejecuta al haber cargado la tabla
  });
});
