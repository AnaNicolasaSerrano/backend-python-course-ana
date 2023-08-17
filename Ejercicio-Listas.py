"""
Crear un prototipo de un carrito de compras,
que al final haya por lo menos 8 productos dispinibles
"""

print("Carrito de compras\n")

print("""
Productos Disponibles:
    1.- Pan
    2.- Jamón
    3.- Crema
    4.- Mayonesa
    5.- Lechuga
    6.- Jitomate
    7.- Queso
    8.- Cebolla
""")

print(
    "Ingresa una lista con los productos en este formato: [[Cantidad,Producto]]")
print("Por ejemplo: [[1,1],[3,2]] significa 1 Pan y 3 Jamón")

my_shopping_cart = eval(input())

print("\n\nTu carrito es:")
if type(my_shopping_cart) == list:
    if type(my_shopping_cart[0]) == list:
        for element in my_shopping_cart:
            product = ""
            if element[1] == 1:
                product = "Pan"
            if element[1] == 2:
                product = "Jamón"
            if element[1] == 3:
                product = "Crema"
            if element[1] == 4:
                product = "Mayonesa"
            if element[1] == 5:
                product = "Lechuga"
            if element[1] == 6:
                product = "Jitomate"
            if element[1] == 7:
                product = "Queso"
            if element[1] == 8:
                product = "Cebolla"

            print("{} {}".format(element[0], product))
    else:
        print("Formato Incorrecto, debes ingresar una lista de listas")
else:
    print("Formato Incorrecto, debes ingresar una lista de listas")
