#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Producto:
    def __init__(self,nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Sistema:

    total_ventas = 0

    def __init__(self):
        self._helados = []
        self._coberturas = []

    def agregar_producto(self):
        comando = str(input('''
        Tipo de producto (1 o 2)
        1. Helado
        2. Cobertura
        q. Salir
        '''))
        if comando == '1' or comando == '2':
            nombre = input(str("Ingrese el nombre del producto (Ejemplo: Galletas, M&Ms, etc.): "))
            precio = input(str("Ingrese el valor de la porcion: "))
            cantidad = input(str("Ingrese el numero de porciones disponibles: "))
            producto = Producto(nombre, int(precio), int(cantidad))
            if comando == '1':
                self._helados.append(producto)
            elif comando == '2':
                self._coberturas.append(producto)
                
        elif comando == 'q':
            pass
        else:
            print("Entrada inválida. Por favor intente de nuevo")

    def imprimir_inventario(self):
        print("INVENTARIO\n")
        print("Helados")
        for indice, producto in enumerate(self._helados):
            print("{}) ".format(indice + 1), end="")
            self.imprimir_producto(producto)
        print()
        print("Coberturas")
        for indice, producto in enumerate(self._coberturas):
            print("{}) ".format(indice + 1), end="")
            self.imprimir_producto(producto)

    def imprimir_producto(self, producto):
        print("{}      {}  {}".format(producto.nombre, producto.precio, producto.cantidad))
            

    def agregar_al_inventario(self):
        comando = str(input('''
        Tipo de producto (1 o 2)
        1. Helado
        2. Cobertura
        q. Salir
        '''))
        if comando == "1":
            self.seleccionar_producto(self._helados)
        elif comando == "2":
            self.seleccionar_producto(self._coberturas)
        elif comando == "q":
            pass
        else:
            print("Entrada inválida. Por favor intente de nuevo")
    
    def seleccionar_producto(self, lista):
        print("Seleccione un Producto")
        for indice, producto in enumerate(lista):
            print("{}) ".format(indice + 1), end="")
            self.imprimir_producto(producto)
        comando = input("")
        print("Usted Selecciono:")
        print("{}) ". format(comando), end="")
        self.imprimir_producto(lista[int(comando) - 1])
        comando2 = str(input("Ingrese la cantidad de porciones a registrar: "))
        lista[int(comando) - 1].cantidad += int(comando2)

    def comprar(self):
        if len(self._helados) == 0:
            print("No hay productos disponibles en el inventario")
        else:
            print("Nueva venta:\nEscoja un sabor:")
            for idx, sabor in enumerate(self._helados):
                print("{}) ".format(idx + 1), end="")
                self.imprimir_producto(sabor)
            comando = input("")
            print("Usted Selecciono:")
            print("{}) ".format(comando), end="")
            self.imprimir_producto(self._helados[int(comando) - 1])
            comando2 = str(input("Cuantas porciones?:\n"))
            self._helados[int(comando) - 1].cantidad -= int(comando2)
            precio_actual = int(comando2) * self._helados[int(comando) - 1].precio
            comando3 = str(input("Desea cobertura? (s/n):\n"))
            if comando3 == 's':
                print("Escoja la cobertura")
                for idx, cobertura in enumerate(self._coberturas):
                    print("{}) ".format(idx + 1), end="")
                    self.imprimir_producto(cobertura)
                comando4 = input("")
                print("Usted Selecciono:")
                print("{}) ".format(comando4), end="")
                self.imprimir_producto(self._coberturas[int(comando4) - 1])
                self._coberturas[int(comando4) - 1].cantidad -= 1
                precio_actual += self._coberturas[int(comando4) - 1].precio
            elif comando3 == "n":
                pass
            else:
                print("Entrada inválida. Por favor intente de nuevo")
            self.total_ventas += precio_actual
            print("Total a pagar:  {}".format(precio_actual))

    def ventas_del_dia(self):
        print("Total ventas del dia: {}".format(self.total_ventas))
                
def run():
    sistema = Sistema()

    while True:
        comando = str(input('''
        *****Administración de Heladeria*****

        Seleccione una opción (1 - 5) o q para salir
        1. Comprar
        2. Agregar un nuevo producto
        3. Ver inventario
        4. Agregar al inventario
        5. Total de ventas del día
        q: Salir
        '''))

        if comando == '1':
            sistema.comprar()
        elif comando == '2':
            sistema.agregar_producto()
        elif comando == '3':
            sistema.imprimir_inventario()
        elif comando == '4':
            sistema.agregar_al_inventario()
        elif comando == '5':
            sistema.ventas_del_dia()
        elif comando == 'q':
            break
        else:
            print("Entrada inválida. Por favor intente de nuevo")

if __name__ == "__main__":
    run()
