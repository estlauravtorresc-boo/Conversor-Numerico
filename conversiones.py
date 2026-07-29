def decimal_binario(numero):

    numero_original = int(numero)

    negativo = numero_original < 0
    numero = abs(numero_original)

    if numero == 0:
        return numero_original, "No se requieren divisiones.", "0"

    procedimiento = ""
    binario = ""

    while numero > 0:

        residuo = numero % 2
        cociente = numero // 2

        procedimiento += f"{numero} ÷ 2 = {cociente}    Residuo = {residuo}\n"

        binario = str(residuo) + binario

        numero = cociente

    if negativo:
        procedimiento += "\nEl número es negativo, se antepone el signo (-) al resultado final.\n"
        binario = "-" + binario

    return numero_original, procedimiento, binario


def decimal_hexadecimal(numero):

    numero_original = int(numero)

    negativo = numero_original < 0
    numero = abs(numero_original)

    equivalencias = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }

    procedimiento = ""
    hexadecimal = ""

    if numero == 0:
        return numero_original, "No se requieren divisiones.", "0"

    while numero > 0:

        residuo = numero % 16
        cociente = numero // 16

        if residuo >= 10:
            digito = equivalencias[residuo]
        else:
            digito = str(residuo)

        procedimiento += f"{numero} ÷ 16 = {cociente}    Residuo = {digito}\n"

        hexadecimal = digito + hexadecimal

        numero = cociente

    if negativo:
        procedimiento += "\nEl número es negativo, se antepone el signo (-) al resultado final.\n"
        hexadecimal = "-" + hexadecimal

    return numero_original, procedimiento, hexadecimal



def binario_decimal(binario):

    numero_original = binario

    negativo = binario.startswith("-")
    binario_abs = binario[1:] if negativo else binario

    decimal = 0
    potencia = len(binario_abs) - 1

    procedimiento = ""

    for bit in binario_abs:

        valor = int(bit) * (2 ** potencia)

        procedimiento += f"{bit} × 2^{potencia} = {valor}\n"

        decimal += valor

        potencia -= 1

    if negativo:
        procedimiento += "\nEl número es negativo, se antepone el signo (-) al resultado final.\n"
        decimal = -decimal

    return numero_original, procedimiento, str(decimal)



def hexadecimal_decimal(hexadecimal):

    numero_original = hexadecimal.upper()

    negativo = numero_original.startswith("-")
    hexadecimal_abs = numero_original[1:] if negativo else numero_original

    valores = {
        "A":10,
        "B":11,
        "C":12,
        "D":13,
        "E":14,
        "F":15
    }

    decimal = 0
    potencia = len(hexadecimal_abs)-1

    procedimiento = ""

    for digito in hexadecimal_abs:

        if digito.isdigit():
            valor = int(digito)
        else:
            valor = valores[digito]

        resultado = valor * (16 ** potencia)

        procedimiento += f"{digito} × 16^{potencia} = {resultado}\n"

        decimal += resultado

        potencia -= 1

    if negativo:
        procedimiento += "\nEl número es negativo, se antepone el signo (-) al resultado final.\n"
        decimal = -decimal

    return numero_original, procedimiento, str(decimal)



def binario_hexadecimal(binario):

    _, _, decimal = binario_decimal(binario)

    _, procedimiento, hexadecimal = decimal_hexadecimal(decimal)

    return binario, procedimiento, hexadecimal



def hexadecimal_binario(hexadecimal):

    _, _, decimal = hexadecimal_decimal(hexadecimal)

    _, procedimiento, binario = decimal_binario(decimal)

    return hexadecimal.upper(), procedimiento, binario
