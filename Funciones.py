data = 0
carrito = []


def add_to_carrito(producto):
    carrito.append(producto)


while (0 >= data < 3):
    if data == 0:
        print("""
        --------------------------------
        1- Agrega articulos a tu carrito
        2- Ver carrito
        3- Salir
        --------------------------------
        """)
        data = int(input("Ingresa una opción:  "))
    if data == 1:
        cosa = input("Ingresa un articulo: ")
        add_to_carrito(cosa)
        data = 0
    if data == 2:
        for x in carrito:
            print(x)
        data = 0
