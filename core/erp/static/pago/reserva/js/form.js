$(function () {
  $(".select2").select2({
    theme: "bootstrap4",
    language: "es",
  });

  // cargar y calcular datos
  function calculate_payment() {
    $.ajax({
      url: window.location.pathname,
      type: "POST",
      data: {
        action: "complete",
      },
      dataType: "json",
      headers: {
        'X-CSRFToken': csrftoken
      }
    }).done(function (data) {
      if (!data.hasOwnProperty("error")) {
        // filter(debo poner la posicion pq me trae una lista)
        // $("input[name='subtotal']").val(data[0].room_type.tariff);
        // get(para traer un objecto, se debe pasar en dict)
        $("input[name='total']").val((data.total));
        $("input[name='avance']").val((data.avance));
        $("input[name='resto']").val((data.total - data.avance));
        $("select[name='reserva']").val(data.id);
        return false;
      }
      message_error(data.error);
    });
  };

  calculate_payment();

});

