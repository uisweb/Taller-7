//Funcion para obtener la cookie con el nombre dado
const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        let cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
};

// Funcion para validar campos form
const checkInputsForm = () => {
    const nombre = $("#nombre").val();
    const descripcion = $("#descripcion").val();
    if (nombre === "" || descripcion === "") {
        $("#btn-submit").attr("disabled", true);
    } else {
        $("#btn-submit").attr("disabled", false);
    }
};

// Eventos para validar campos form
$("#modalBody").on({
    keyup: checkInputsForm,
    change: checkInputsForm,
});

// Funcion para personalizar form
const customizeForm = (formFetch, urlForm, modalTitle, nameBtnSubmit) => {
    $("#modalBody").empty();
    $("#modalBody").append(formFetch);
    $("#form").attr("action", urlForm);
    $("#modalTitle").text(modalTitle);
    $("#btn-submit").text(nameBtnSubmit);
    $(".errorlist").remove();
    $("#btn-submit").attr("disabled", true);
    $("#modalFormContainer").modal("show");
};

// Funcion para hacer peticiones
const getFormFetch = async(url) => {
    const formFetch = await fetch(url, {
            method: "GET",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
            credentials: "same-origin",
        })
        .then((response) => response.text())
        .then((data) => data);
    return formFetch;
}

// CREAR DOCUMENTO
const btnCreate = async(url, modalTitle, nameBtnSubmit) => {
    customizeForm(await getFormFetch(`${url}/`), `${url}/`, modalTitle, nameBtnSubmit);
};

// ACTUALIZAR DOCUMENTO
const btnUpdate = async(id, url, modalTitle, nameBtnSubmit) => {
    customizeForm(await getFormFetch(`${url}/${id}/`), `${url}/${id}/`, modalTitle, nameBtnSubmit);
};

// BORRAR DOCUMENTO
const btnDelete = (id, url) => {
    Swal.fire({
        title: "¿Estás seguro?",
        text: "Esta acción no se puede revertir",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Borrar",
        cancelButtonText: "Cancelar",
    }).then((result) => {
        if (result.value) {
            fetch(`${url}/${id}/`, {
                    method: "POST",
                    headers: {
                        "X-CSRFToken": getCookie("csrftoken"),
                    },
                    credentials: "same-origin",
                })
                .then((response) => {
                    if (response.ok) {
                        Swal.fire("Borrado!", "El registro ha sido borrado", "success");
                        location.reload();
                    } else {
                        Swal.fire("Error!", "No se ha podido borrar el registro", "error");
                    }
                })
        }
    })
};
