class Producto:
    def __init__(self, nombre, precio, cantidad, color, talla):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.color = color
        self.talla = talla

    def stock(self):
        print(f"Hay {self.cantidad} de {self.nombre}  ")

    def caracteristicas(self):
        print(
            f"El producto {self.nombre} es de color: {self.color} y talla: {self.talla}")


class Categoria:
    productos = []

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)


chamarra = Producto("Chamarra", 600, 2, "Cafe", "L")
pantalon = Producto("Pantalon", 120, 3, "Azul", "M")
camisa = Producto("Camisa", 200, 7, "Rojo", "S")

print(chamarra.nombre)
