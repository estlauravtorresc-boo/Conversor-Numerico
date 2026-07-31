def decimal_binario(numero):
    numero_original = int(numero)
    negativo = numero_original < 0#variable booleana
    numero = abs(numero_original)#toma el valor absoluto

    if numero == 0:
        return numero_original, "No se requieren divisiones.", "0"

    procedimiento = ""#variables vacias string para que muestren despues el resultado al final
    binario = ""

    while numero > 0:

        residuo = numero % 2
        cociente = numero // 2
        procedimiento += f"{numero} ÷ 2 = {cociente}    Residuo = {residuo}\n"
        binario = str(residuo) + binario#cpnstruye de der a izq(abajo a arriba)
        numero = cociente#actualiza el valor del numero
        #cuando llegue a 0 el bucle se detiene 

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
            digito = equivalencias[residuo]#busca la letra correspondiente en el diccionario
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
    numero_original = binario#como string por que es cadena 1101
    negativo = binario.startswith("-")#este revisa si el texto inica con -
    binario_abs = binario[1:] if negativo else binario#quita el simbolo y empieza a operar desde la posicion 1 en adelante
    decimal = 0#va acumulando el resultado
    potencia = len(binario_abs) - 1#pone las potencias de derecha a izq

    procedimiento = ""

    for bit in binario_abs:
        valor = int(bit) * (2 ** potencia)
        procedimiento += f"{bit} × 2^{potencia} = {valor}\n"
        decimal += valor#se suma el valor acumulado
        potencia -= 1#se resta por que cada posicion a la der vale la mitad de la anterior 

    if negativo:
        procedimiento += "\nEl número es negativo, se antepone el signo (-) al resultado final.\n"
        decimal = -decimal

    return numero_original, procedimiento, str(decimal)#por que esperan que el resultado sea de tipo string y no int


def hexadecimal_decimal(hexadecimal):
    numero_original = hexadecimal.upper()#convierte todo a mayusculas
    negativo = numero_original.startswith("-")#detecta el signo y separa de el resto 
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
        if digito.isdigit():#revisa si el caracter es un numero 0-9
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

    resultado_decimal = binario_decimal(binario)
    decimal = resultado_decimal[2]

    resultado_hexadecimal = decimal_hexadecimal(decimal)
    procedimiento = resultado_hexadecimal[1]
    hexadecimal = resultado_hexadecimal[2]

    return binario, procedimiento, hexadecimal


def hexadecimal_binario(hexadecimal):

    resultado_decimal = hexadecimal_decimal(hexadecimal)
    decimal = resultado_decimal[2]

    resultado_binario = decimal_binario(decimal)
    procedimiento = resultado_binario[1]
    binario = resultado_binario[2]

    return hexadecimal.upper(), procedimiento, binario


def binario_grey(binario):
    numero_original = binario
    procedimiento = ""
    grey = ""
    primer_bit = binario[0]
    grey += primer_bit

    procedimiento += f"Primer bit: se copia igual → {primer_bit}\n"

    for i in range(1, len(binario)):
        bit_actual = binario[i]
        bit_anterior = binario[i - 1]
        if bit_actual == bit_anterior:
            xor = "0"
        else:
            xor = "1"
        procedimiento += f"{bit_anterior} XOR {bit_actual} = {xor}\n"
        grey += xor

    return numero_original, procedimiento, grey



def grey_binario(grey):
    numero_original = grey
    procedimiento = ""
    binario = ""
    primer_bit = grey[0]
    binario += primer_bit

    procedimiento += f"Primer bit: se copia igual → {primer_bit}\n"

    for i in range(1, len(grey)):
        bit_grey = grey[i]
        bit_binario_anterior = binario[i - 1]
        if bit_grey == bit_binario_anterior:
            xor = "0"
        else:
            xor = "1"
        procedimiento += f"{bit_binario_anterior} XOR {bit_grey} = {xor}\n"
        binario += xor

    return numero_original, procedimiento, binario
