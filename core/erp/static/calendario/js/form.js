$(function () {
    /* ############### EVENTO CALENDARIO ################*/
    $("#check_in, #check_out").datetimepicker({
        format: "YYYY-MM-DD",
        locale: "es",
        minDate: moment().format("YYYY-MM-DD"),
    });

    const input_check_in = $("#check_in")
    input_check_in.datetimepicker("date", input_check_in.val());

    const input_check_out = $("#check_out")
    input_check_out.datetimepicker("date", input_check_out.val());
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
        if (id) {
            $.ajax({
                url: window.location.pathname,
                type: "POST",
                data: {
                    action: "complete",
                    id: id
                },
                dataType: "json",
                headers: {
                    'X-CSRFToken': csrftoken
                }
            }).done(function (data) {
                if (!data.hasOwnProperty("error")) {
                    let subtotal = data.tipo_habitacion.tarifa;
                    // $("input[name='subtotal']").val(subtotal);
                    let iva = $("input[name='iva']").val();
                    let avance = $("input[name='avance']").val();
                    let entrada = moment($('#check_in').val())
                    let salida = moment($('#check_out').val())
                    let diferencia = salida.diff(entrada, 'days')
                    if (diferencia > 0) {
                        $("input[name='subtotal']").val((subtotal * diferencia) - avance);
                        $("input[name='total']").val(((subtotal + (subtotal * iva)) * diferencia) - avance);
                    } else {
                        $("input[name='subtotal']").val(subtotal - avance);
                        $("input[name='total']").val(subtotal + (subtotal * iva) - avance);
                    }
                    return false;
                }
                message_error(data.error);
            });
        }
        console.log(id)

    };


    $("#check_out").on("change.datetimepicker", () => {
        calculate_reception();
    })

    $("#check_in").on("change.datetimepicker", (e) => {
        element = e.target // target es para indicar especificamente la etiqueta donde hago alución
        $("#check_out").datetimepicker('minDate', element.value); // matener fecha minima respecto ah check_in

        calculate_reception();
    })


    $("input[name='avance']")
        .on("keyup", function () {
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
            headers: {
                'X-CSRFToken': csrftoken
            },
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
