document.addEventListener("DOMContentLoaded", function () {

    const input = document.getElementById("numero");
    const select = document.getElementById("conversion");
    const mensaje = document.querySelector(".success, .error");

    // Placeholders dinámicos según el tipo de conversión seleccionado
    const placeholders = {
        DecBin: "Ej: -25 o 25",
        DecHex: "Ej: -255 o 255",
        BinDec: "Ej: -1101 o 1101",
        HexDec: "Ej: -1F o 1F",
        BinHex: "Ej: -1101 o 1101",
        HexBin: "Ej: -1F o 1F"
    };

    function actualizarPlaceholder() {
        if (select && input) {
            input.placeholder = placeholders[select.value] || "Ingrese un número";
        }
    }

    if (select) {
        actualizarPlaceholder();
        select.addEventListener("change", actualizarPlaceholder);
    }

    // Foco automático en el campo de número al cargar la página
    if (input) {
        input.focus();
    }

    // Ocultar automáticamente el mensaje de éxito/error después de unos segundos
    if (mensaje) {
        setTimeout(function () {
            mensaje.style.transition = "opacity 0.6s ease";
            mensaje.style.opacity = "0";
            setTimeout(function () {
                mensaje.style.display = "none";
            }, 600);
        }, 4000);
    }

    // Permitir enviar el formulario con la tecla Enter estando en el input
    if (input) {
        input.addEventListener("keydown", function (evento) {
            if (evento.key === "Enter") {
                evento.target.closest("form").submit();
            }
        });
    }

});
