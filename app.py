from flask import Flask, render_template, request
from conversiones import *

app = Flask(__name__)


def es_decimal(numero):
    if numero.startswith("-"):
        numero = numero[1:]
    return numero != "" and numero.isdigit()


def es_binario(numero):
    if numero.startswith("-"):
        numero = numero[1:]
    return numero != "" and all(bit in "01" for bit in numero)


def es_hexadecimal(numero):
    if numero.startswith("-"):
        numero = numero[1:]
    numero = numero.upper()
    permitidos = "0123456789ABCDEF"
    return numero != "" and all(caracter in permitidos for caracter in numero)


@app.route("/", methods=["GET", "POST"])
def inicio():

    numero = ""
    conversion = ""

    procedimiento = ""
    resultado = ""

    mensaje = ""
    tipo = ""

    if request.method == "POST":

        numero = request.form["numero"].strip()
        conversion = request.form["conversion"]

        try:

            if conversion == "DecBin":

                if not es_decimal(numero):
                    raise ValueError("El número ingresado no pertenece al sistema decimal.")

                original, procedimiento, convertido = decimal_binario(numero)

                resultado = f"{original}₁₀ = {convertido}₂"

            elif conversion == "DecHex":

                if not es_decimal(numero):
                    raise ValueError("El número ingresado no pertenece al sistema decimal.")

                original, procedimiento, convertido = decimal_hexadecimal(numero)

                resultado = f"{original}₁₀ = {convertido}₁₆"

            elif conversion == "BinDec":

                if not es_binario(numero):
                    raise ValueError("Un número binario solo puede contener 0 y 1.")

                original, procedimiento, convertido = binario_decimal(numero)

                resultado = f"{original}₂ = {convertido}₁₀"

            elif conversion == "HexDec":

                if not es_hexadecimal(numero):
                    raise ValueError("Un número hexadecimal solo puede contener 0-9 y A-F.")

                original, procedimiento, convertido = hexadecimal_decimal(numero)

                resultado = f"{original.upper()}₁₆ = {convertido}₁₀"

            elif conversion == "BinHex":

                if not es_binario(numero):
                    raise ValueError("Un número binario solo puede contener 0 y 1.")

                original, procedimiento, convertido = binario_hexadecimal(numero)

                resultado = f"{original}₂ = {convertido}₁₆"

            elif conversion == "HexBin":

                if not es_hexadecimal(numero):
                    raise ValueError("Un número hexadecimal solo puede contener 0-9 y A-F.")

                original, procedimiento, convertido = hexadecimal_binario(numero)

                resultado = f"{original.upper()}₁₆ = {convertido}₂"

            mensaje = "Conversión realizada correctamente."
            tipo = "success"

        except Exception as e:

            mensaje = str(e)
            tipo = "error"

    return render_template(

        "index.html",

        numero=numero,
        conversion=conversion,
        procedimiento=procedimiento,
        resultado=resultado,
        mensaje=mensaje,
        tipo=tipo

    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
