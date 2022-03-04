var tblReserva;

function format(d) {
  console.log(d)
  var html = "<table class='table'>";
  html += "<thead class='thead-dark'>";
  html += "<tr>"
  html += "<th scope='col'>Huesped</th>";
  html += "<th scope='col'>Numero de Documento</th>";
  html += "<th scope='col'>Numero de Habitación</th>";
  html += "<th scope='col'>Tipo de Habitación</th>";
  html += "<th scope='col'>Tarifa de Habitación</th>";
  html += "</tr>";
  html += "</thead>";
  html += "<tbody>";
  html += "<tr>";
  html += "<td>" + d.user.full_name + "</td>";
  html += "<td>" + d.user.numero_documento + "</td>";
  html += "<td>" + d.habitacion.numero_habitacion + "</td>";
  html += "<td>" + d.habitacion.tipo_habitacion.nombre + "</td>";
  html += "<td>" + d.habitacion.tipo_habitacion.tarifa + "</td>";
  html += "</tr>";
  html += "</tbody>";
  return html;
}

$(function () {


  tblReserva = $("#data").DataTable({
    // responsive: true,
    scrollX: true,
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
      {
        "className": 'details-control',
        "orderable": false,
        "data": null,
        "defaultContent": ''
      },
      { "data": "check_in" },
      { "data": "check_out" },
      { "data": "subtotal" },
      { "data": "iva" },
      { "data": "avance" },
      { "data": "total" },
      { "data": "estado_reserva" },
      { "data": "id" }
    ],
    columnDefs: [
      {
        targets: [-5],
        class: "text-center",
        orderable: false,
        render: function (data, type, row) {
          return data+"<b>%</b>" ;
        },
      },
      {
        targets: [-3,-4,-6],
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
          if (data == "alojamiento terminado") {
            return '<span class="badge badge-success">' + data.toUpperCase() + '</span> ';
          } else if (data == "confirmada") {
            return '<span class="badge badge-danger">' + data.toUpperCase() + '</span> ';
          } else if (data == "no ingreso") {
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
          let buttons = '<a href="/erp/recepcion/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
          buttons += '<a href="/erp/recepcion/delete/' + row.id + '/" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a> ';
          // buttons +=  '<a rel="details" class="btn btn-success btn-xs btn-flat"><i class="fas fa-search"></i></a>';
          return buttons;
        },
      },
    ],
    initComplete: function (settings, json) { },
    // se ejecuta al haber cargado la tabla



  });
  //MODAL
  $("#data tbody")
    .on("click", "td.details-control", function () {
      var tr = $(this).closest("tr");
      var row = tblReserva.row(tr);
      if (row.child.isShown()) {
        row.child.hide();
        tr.removeClass("shown");
      } else {
        row.child(format(row.data())).show();
        tr.addClass("shown");
      }
    });


});
