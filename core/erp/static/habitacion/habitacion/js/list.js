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
      { "data": "numero_habitacion" },
      { "data": "tipo_habitacion.nombre" },
      { "data": "piso.nombre" },
      { "data": "desc" },
      { "data": "servicio_habitacion.nombre" },
      { "data": "tipo_habitacion.tarifa" },
      { "data": "estado_habitacion" },
      { "data": "id" }
    ],
    columnDefs: [
      {
        targets: [0],
        class: "text-center",
        orderable: false,
        render: function (data, type, row) {
          return data;
        },
      },
      {
        targets: [-3],
        class: "text-center",
        orderable: false,
        render: function (data, type, row) {
          return "<b>$</b>" + data;
        },
      },
      {
        targets: [-2],
        class: "text-center",
        orderable: false,
        render: function (data, type, row) {
          if (data == "disponible") {
            return '<span class="badge badge-success">' + data.toUpperCase() + '</span> ';
          } else if (data == "ocupada") {
            return '<span class="badge badge-danger">' + data.toUpperCase() + '</span> ';
          } else if (data == "limpieza") {
            return '<span class="badge badge-primary">' + data.toUpperCase() + '</span> ';
          } else {
            return '<span class="badge badge-warning">' + data.toUpperCase() + '</span> ';
          }

        },
      },
      {
        targets: [-1],
        class: "text-center",
        orderable: false,
        render: function (data, type, row) {
          let buttons = '<a href="/erp/habitacion/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
          buttons += '<a href="/erp/habitacion/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
          return buttons;
        },
      },
    ],
    initComplete: function (settings, json) { },
    // se ejecuta al haber cargado la tabla
  });
});


