"""Calculadora"""
OP = 0
TIPO_DATO = 0
RESULTADO = 0

try:
    print("""Calculadora
    Selecciona la operación que deceas realizar:
    1 - Suma
    2 - Resta
    3 - Multiplicación
    4 - División
    5 - Potencia
    """)
    while 1:
        if 0 < OP < 6:
            print(OP)
            break
        else:
            print("Ingresa una operacion correcta")
            OP = int(input("Operación a realizar: "))

    print("""Como deceas ingresar tus datos:
        1 - en lista
        2 - en set
        3 - en diccionario 
    """)
    while 1:
        if 0 < TIPO_DATO < 4:
            print(TIPO_DATO)
            break
        else:
            print("Ingresa un valor de dato correcto")
            TIPO_DATO = int(input("Tipo de dato que ingresaras: "))
except TypeError:
    print("Entrada invalida, solo acepta numeros")
except ValueError:
    print("Entrada invalida, solo acepta numeros")

lista_datos = list(
    input("Ingresa 5 numeros seguidos de una espacio: ").split())
print(len(lista_datos))

try:
    for i in range(5):
        lista_datos[i] = int(lista_datos[i])

    print(lista_datos)
except TypeError:
    print("Entrada invalida o tamñano invalido en la entrada")

if OP == 1:
    for i in lista_datos:
        RESULTADO += i
elif OP == 2:
    for i in lista_datos:
        i -= RESULTADO
elif OP == 3:
    for i in lista_datos:
        RESULTADO /= i
elif OP == 4:
    for i in lista_datos:
        RESULTADO *= i
elif OP == 5:
    for i in lista_datos:
        RESULTADO **= i

print(f"el resultado de tu operacion es: {RESULTADO}")
