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
            var value = $("select[name='habitacion']").val()
            // console.clear();
            // console.log($(this).val());
            if (value |= null) {
                calculate_reception();
            }

        })
        .val(0.19);

    /* ############### CALCULAR Y CARGAR DATOS ################*/
    const calculate_reception = function () {
        var id = $("select[name='habitacion']").val();
        console.log(id)
        $.ajax({
            url: window.location.pathname,
            type: "POST",
            data: {
                action: "complete",
                id: id
            },
            dataType: "json",
            // processData: false, //no las usa pq no envia archivos
            // contentType: false,
        }).done(function (data) {
            if (!data.hasOwnProperty("error")) {
                // filter(debo poner la posicion pq me trae una lista)
                // $("input[name='subtotal']").val(data[0].room_type.tariff);
                // get(para traer un objecto, se debe pasar en dict)
                let subtotal = data.tipo_habitacion.tarifa;
                $("input[name='subtotal']").val(subtotal);
                let iva = $("input[name='iva']").val();
                $("input[name='ivacalc']").val(subtotal * iva);
                let avance = $("input[name='avance']").val();
                $("input[name='total']").val(subtotal + (subtotal * iva) - avance);
                // $("select[name='room']").val(data.id);
                return false;
            }
            message_error(data.error);
        });
    };

    // calculate_reception();

    // $("input[name='advance']")
    //   .change(function () {
    //     calculate_reception();
    //   });

    $("input[name='avance']")
        .on("change keyup", function () {
            calculate_reception();
        });

    $("select[name='habitacion']")
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
                    action: "search_guest",
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

    // $(".btnAddGuest").on("click", function () {
    //   $("#myModalGuest").modal("show"); // usamos la funcion modal y el evento "show" para mostrar
    // });

    /* ############### EVENT TRIGGER MODAL HIDE ################*/

    $("#myModalReserva").on("hidden.bs.modal", function (event) {
        $('#frmReserva').trigger('reset') // ejecutamos llamamos al metodo trigger y ejecutamos el evento reset, para limpiar el formulario
        $("input[name='iva']").val(0.19);
        $('select[name="user"]').empty()
    });

    /* ############### SUBMIT BOOKING ################*/

    $("#frmReserva").on("submit", function (e) {
        e.preventDefault();
        var parameters = new FormData(this); // con el "this" llenamos el FormData a partir del fomulario al que apunto, lo cual crea una array de elementos
        parameters.append("action", "create_reserva"); // creamos una acción para que llegue a mi vista
        submit_with_ajax(
            window.location.pathname,
            "Notificación",
            "¿Estas seguro de crear la siguiente reserva?",
            parameters,
            function (response) {
                console.log(response)
                $("#myModalReserva").modal("hide"); // para que el modal se oculte
                location.reload();
                // $("#calendar").fullCalendar('refetchEvents')
            }
        );
    });



});
