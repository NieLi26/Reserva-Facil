// function message_error (obj) {

// }

let message_error = (obj) => {
  let html = "";
  if (typeof obj === "object") {
    html = "<ul style='text-align: left'>";
    $.each(obj, function (key, value) {
      //   html += "<li>" + key + ":" + value + "</li>";
      html += `<li> ${key}: ${value} </li>`;
    });
    html += "</ul>";
  } else {
    html = `<p> ${obj} </p>`;
    // html = "<p>" + obj + "</p>";
  }
  Swal.fire({
    title: "Error!",
    html: html,
    icon: "error",
  });
};

function submit_with_ajax(url, title, content, parameters, callback) {
  $.confirm({
    theme: "material",
    title: title,
    icon: "fa fa-info",
    content: content,
    columnClass: "small",
    typeAnimated: true,
    cancelButtonClass: "btn-primary",
    draggable: true,
    dragWindowBorder: false,
    buttons: {
      info: {
        text: "Si",
        btnClass: "btn-primary",
        action: function () {
          $.ajax({
            // url: "{% url 'erp:region_create' %}",
            url: url, //window.location.pathname
            type: "POST",
            data: parameters,
            dataType: "json",
            processData: false,
            contentType: false,
          })
            .done(function (data) {
              if (!data.hasOwnProperty("error")) {
                callback(data);
                // location.href = "{{ list_url }}";
                return false;
              }
              message_error(data.error);
            })
            .fail(function (jqXHR, textStatus, errorThrown) {
              alert(textStatus + ": " + errorThrown);
              // alert("error");
            })
            .always(function (data) {
              
            });
        },
      },
      danger: {
        text: "No",
        btnClass: "btn-red",
        action: function () {},
      },
    },
  });
}

function alert_action(title, content, callback) {
  $.confirm({
    theme: "material",
    title: title,
    icon: "fa fa-info",
    content: content,
    columnClass: "small",
    typeAnimated: true,
    cancelButtonClass: "btn-primary",
    draggable: true,
    dragWindowBorder: false,
    buttons: {
      info: {
        text: "Si",
        btnClass: "btn-primary",
        action: function () {
          callback();
        },
      },
      danger: {
        text: "No",
        btnClass: "btn-red",
        action: function () {},
      },
    },
  });
}
