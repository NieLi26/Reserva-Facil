$(function () {
  /* ############### EVENTO SELECT2 ################*/
  $(".select2").select2({
    theme: "bootstrap4",
    language: "es",
  });

  /* ############### EVENTO CALENDARIO ################*/
  $("#check_in").datetimepicker({
    format: "YYYY-MM-DD",
    // format: "YYYY-MM-DD, h:mm a",
    date: moment().format("YYYY-MM-DD"),
    locale: "es",
    minDate: moment().format("YYYY-MM-DD"),
  });

  $("#check_out").datetimepicker({
    format: "YYYY-MM-DD",
    date: moment().format("YYYY-MM-DD"),
    locale: "es",
    minDate: moment().format("YYYY-MM-DD"),
  });

  // var input_datejoined = $('input[name="check_in"]');

  // input_datejoined.datetimepicker({
  //   useCurrent: false,
  //   format: "YYYY-MM-DD",
  //   locale: "es",
  //   keepOpen: false,
  // });

  // input_datejoined.datetimepicker("date", input_datejoined.val());

  /* ############### EVENTO AUMENTAR, DECRECER VALOR ################*/

  $("input[name='iva']")
    .TouchSpin({
      min: 0,
      max: 100,
      step: 0.01,
      decimals: 2,
      boostat: 5,
      maxboostedstep: 10,
      postfix: "%",
    })
    .on("change", function () {
      // console.clear();
      // console.log($(this).val());
      calculate_reception();
    })
    .val(0.19);

  /* ############### CALCULAR Y CARGAR DATOS ################*/
  function calculate_reception() {
    $.ajax({
      url: window.location.pathname,
      type: "POST",
      data: {
        action: "complete",
      },
      dataType: "json",
    }).done(function (data) {
      if (!data.hasOwnProperty("error")) {
        let subtotal = data.tipo_habitacion.tarifa;
        $("input[name='subtotal']").val(subtotal);
        let iva = $("input[name='iva']").val();
        $("input[name='ivacalc']").val(Math.round(subtotal * iva));
        let avance = $("input[name='avance']").val();
        $("input[name='total']").val(subtotal + (subtotal * iva) - avance);
        $("select[name='habitacion']").val(data.id);
        return false;
      }
      message_error(data.error);
    });
  };

  calculate_reception();


  $("input[name='avance']")
    .on("change", function () {
      calculate_reception();
    });

  /* ----------------------------------------------------------------------------------------------------------------------------------------------------------*/
  /* ------------------------------------------------------------------------- AGREGAR HUESPED ----------------------------------------------------------------*/
  /* ----------------------------------------------------------------------------------------------------------------------------------------------------------*/
  /* ############### SEARCH GUEST ################*/

  $('select[name="user"]').select2({
    theme: "bootstrap4",
    language: "es",
    allowClear: true,
    ajax: {
      delay: 250,
      type: "POST",
      url: window.location.pathname,
      data: function (params) {
        var queryParameters = {
          term: params.term,
          action: "search_user",
        };
        return queryParameters;
      },
      processResults: function (data) {
        return {
          results: data,
        };
      },
    },
    placeholder: "Ingrese una descripción",
    minimumInputLength: 1,
  });

  /* ############### EVENT CLICK ADD GUEST ################*/

  $(".btnAddUser").on("click", function () {
    $("#myModalUser").modal("show"); // usamos la funcion modal y el evento "show" para mostrar
  });

  /* ############### EVENT TRIGGER MODAL HIDE ################*/

  $("#myModalUser").on("hidden.bs.modal", function (event) {
    $('#frmUser').trigger('reset') // ejecutamos llamamos al metodo trigger y ejecutamos el evento reset, para limpiar el formulario
  });

  /* ############### SUBMIT USER ################*/

  $("#frmUser").on("submit", function (e) {
    e.preventDefault();
    var parameters = new FormData(this); // con el "this" llenamos el FormData a partir del fomulario al que apunto, lo cual crea una array de elementos
    parameters.append("action", "create_user"); // creamos una acción para que llegue a mi vista
    submit_with_ajax(
      window.location.pathname,
      "Notificación",
      "¿Estas seguro de crear al siguiente huesped?",
      parameters,
      function (response) {
        console.log(response)
        // para cargar en el select al huesped recien creado, llega la data de response(callback) y puedo llamar a la key full_name del metodo toJSON(model to dict)
        var newOption = new Option(response.full_name, response.id, false, true);
        $("select[name='user']").append(newOption).trigger("change");
        $("#myModalUser").modal("hide"); // para que el modal se oculte
      }
    );
  });

});
