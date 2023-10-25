class Producto:
    def __init__(self, id, nombre, descripcion, costo, cantidad, margen_de_venta):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.margen_de_venta = margen_de_venta
        self.precio_de_venta = None

    def calcular_precio_venta(self):
        if self.margen_de_venta > 0:
            self.precio_de_venta = self.costo / (1 - self.margen_de_venta)
        else:
            print("El margen de venta debe ser mayor que 0 para calcular el precio de venta.")

    def registrar_producto(self, productos):
        self.calcular_precio_venta()
        productos[self.id] = {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'costo': self.costo,
            'cantidad': self.cantidad,
            'precio_de_venta': self.precio_de_venta
        }

    @staticmethod
    def imprimir_listado(productos):
        for producto_id, producto in productos.items():
            print(f"ID: {producto_id}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Costo: {producto['costo']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Precio de Venta: {producto['precio_de_venta']}")
            print("\n")


# Ejemplo de uso
productos = {}
producto1 = Producto(1, "Producto1", "Descripción1", 50, 10, 0.2)
producto2 = Producto(2, "Producto2", "Descripción2", 30, 5, 0.15)

producto1.registrar_producto(productos)
producto2.registrar_producto(productos)

Producto.imprimir_listado(productos)