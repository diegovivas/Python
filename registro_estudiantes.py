#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

class Estudiante:
    """Clase Estudiante"""
    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            self.Documento = int(args[0])
            self.Nombre1 = str(args[1])
            self.Nombre2 = str(args[2])
            self.Apellido1 = str(args[3])
            self.Apellido2 = str(args[4])
            self.Carrera = str(args[5])
            self.Nota1 = round(float(args[6]),2)
            self.Nota2 = round(float(args[7]),2)
            self.Nota3 = round(float(args[8]),2)
            self.Promedio = round(float(args[9]),2)
            self.Inasistencias = int(args[10])
            self.Semestre = int(args[11])
        else:
            for key in kwargs:
                setattr(self,key, kwargs[key])

    def __str__(self):
        string = str(self.__dict__["Documento"])
        string = string + "\t|\t" + str(self.__dict__["Nombre1"])
        string = string + " " + str(self.__dict__["Nombre2"])
        string = string + "\t|\t" + str(self.__dict__["Apellido1"])
        string = string + " " + str(self.__dict__["Apellido2"])
        string = string + "\t|\t" + str(self.__dict__["Carrera"])
        string = string + "\t|\t" + str(self.__dict__["Semestre"])
        string = string + "\t|\t" + str(self.__dict__["Inasistencias"])
        string = string + "\t|\t" + str(self.__dict__["Promedio"])
        return string
    
class Sistema:
    estudiantes_carrera = {"ingenieria de sistemas":[], "ingenieria mecatronica":[], "ingenieria electronica":[],
                           "ingenieria civil":[], "ingenieria agricola":[], "ingenieria electrica":[]}
    carreras = ("ingenieria de sistemas", "ingenieria mecatronica", "ingenieria electronica",
                           "ingenieria civil", "ingenieria agricola", "ingenieria electrica")
    estudiantesfinal = []
    estudiantes1 = []
    estudiantes2 = []
    estudiantes_tupla = []
    documentos = []
    file1 = "estudiantes.txt"
    file2 = "datos_academicos.txt"

    def imprimir(self, posicion):
        if self.carreras[posicion] in self.estudiantes_carrera:
            print("Documento|\tNombres\t|\tApellidos|\tCarrera|\tSemestre|\tInasistencias\t|\tPromedio")
            for element in sorted(self.estudiantes_carrera[self.carreras[posicion]], key = funcion_ordenar, reverse = True):
                print(element)
            
        
    def ver_estudiantes_por_carrera(self):
        sistema = Sistema()
        comando = str(input('''
        Escoja una carrera:
        A. Ingeniería de Sistemas
        B. Ingeniería Mecatrónica
        C. Ingeniería Electrónica
        D. Ingeniería Civil
        E. Ingeniería Agrícola
        F. Ingeniería Eléctrica
        '''))

        if comando == 'a':
            sistema.imprimir(0)
        elif comando == 'b':
            sistema.imprimir(1)
        elif comando == 'c':
            sistema.imprimir(2)
        elif comando == 'd':
            sistema.imprimir(3)
        elif comando == 'e':
            sistema.imprimir(4)
        elif comando == 'f':
            sistema.imprimir(5)
        else:
            print("Opcion invalida")

    def ver_notas(self):
        matriz = []
        e_matriz = []
        
        lista = []
        try:
            with open(self.file2, "r") as f:
                lista = json.load(f)
        except:
            pass
            
        for element in lista:
            for ele in element.values():
                e_matriz.append(ele["Documento"])
                e_matriz.append(ele["Nota1"])
                e_matriz.append(ele["Nota2"])
                e_matriz.append(ele["Nota3"])
                e_matriz.append(ele["Promedio"])
            matriz.append(e_matriz)
            e_matriz = []
        for element in matriz:
            print(element)
        
    def estudiantes_inasistencias(self):
        numero = int(input("Ingrese el numero de inasistencias: "))
        if numero >= 0:
            print("Documento\tInasistencias")
            
            for elementos in self.estudiantes_tupla:
                if elementos[2] == numero:
                    print("{}\t{}".format(elementos[1], elementos[2]))

    
    def ver_estudiantes_prom_3(self):
        lista_final = []
        for elementos in self.estudiantes_tupla:
            if elementos[0] < 3:
                lista_final.append(elementos)
        print("Nota\tDocumento")
        for elements in sorted(lista_final, reverse=True):
            print("{}\t{}".format(elements[0], elements[1]))

    def ver_estudiantes(self):
        
        otro = []
        otro2 = []
        clavesf = {}
        self.estudiantesfinal = []
        try:
            with open(self.file1, "r") as f:
                otro = json.load(f)
            with open(self.file2, "r") as r:
                otro2 = json.load(r)

        except:
            pass
        
        for x in otro:
            for y in otro2:
                if x.keys() == y.keys():
                    clave = list(x.keys())[0]
                    clavesf = {**x[clave], **y[clave]}
                    estudiante = Estudiante(**clavesf)
                    self.estudiantesfinal.append(estudiante)
        print("Documento\t|\tNombres\t|\tApellidos\t|\tCarrera\t\t|\tSemestre\t|\tInasistencias\t|\tPromedio")            
        for alumno in self.estudiantesfinal:
            print(alumno)
        self.estudiantesfinal = []
            
    def agregar_datos_academicos(self, estudiante):
        final = {}
        nombre = {}
        diccionario_estudiante = estudiante.__dict__
        for clave, valor in diccionario_estudiante.items():
            if clave == "Documento":
                clave_final = valor
                nombre.setdefault(clave, valor)
            elif clave == "Carrera":
                nombre.setdefault(clave, valor)
            elif clave == "Nota1":
                nombre.setdefault(clave, valor)
            elif clave == "Nota2":
                nombre.setdefault(clave, valor)
            elif clave == "Nota3":
                nombre.setdefault(clave, valor)
            elif clave == "Semestre":
                nombre.setdefault(clave, valor)
            elif clave == "Inasistencias":
                nombre.setdefault(clave, valor)
            elif clave == "Promedio":
                nombre.setdefault(clave, valor)
            else:
                pass

            final.setdefault(clave_final, nombre)

        self.estudiantes2.append(final)
        json_agregar = json.dumps(self.estudiantes2)
            
        try:
            with open(self.file2, "w") as file:
                file.write(json_agregar)
        except:
            pass
      
            
    def agregar_estudiante(self):
        sistema = Sistema()
        Documento = str(input('Ingrese Documento: '))
        Nombre1 = str(input('Ingrese Primer Nombre: '))
        Nombre2 = str(input('Ingrese Segundo Nombre: '))
        Apellido1 = str(input('Ingrese Primer Apelllido: '))
        Apellido2 = str(input('Ingrese Segundo Apellido: '))
        Carrera = str(input('Ingrese Carrera: '))
        Nota1 = str(input('Ingrese Nota1: '))
        Nota2 = str(input('Ingrese Nota2: '))
        Nota3 = str(input('Ingrese Nota3: '))
        Promedio = str(input('Ingrese Promedio: '))
        Inasistencias = str(input('Inasistencias: '))
        Semestre = str(input('Semestre: '))

        estudiante = Estudiante(Documento, Nombre1, Nombre2, Apellido1,
                                Apellido2, Carrera, Nota1, Nota2, Nota3,
                                Promedio, Inasistencias, Semestre)
        sistema.agregar_funcion(estudiante)

    def agregar_funcion(self, estudiante):
        Carrera = estudiante.__dict__["Carrera"]
        Documento = estudiante.__dict__["Documento"]
        Inasistencias = estudiante.__dict__["Inasistencias"]
        Promedio = estudiante.__dict__["Promedio"]
        if Carrera.lower() in self.carreras:
            self.estudiantes_carrera[Carrera.lower()].append(estudiante)
        if Documento in self.documentos:
            pass
        else:
            self.documentos.append(Documento)
            self.estudiantesfinal.append(estudiante)
            
            agregar = funcion_agregar(estudiante)
            self.estudiantes1.append(agregar)
            json_agregar = json.dumps(self.estudiantes1)

            tupla = (round(float(Promedio),2), int(Documento), int(Inasistencias))
            (promedio, documento, inasitencias) = tupla
            
            self.estudiantes_tupla.append(tupla)

            try:
                with open(self.file1, "w") as file:
                    file.write(json_agregar)
            except:
                pass
            sistema = Sistema()
            sistema.agregar_datos_academicos(estudiante)

    def iniciar(self):
        otro = []
        otro2 = []
        clavesf = {}
        sistema = Sistema()
        try:
            with open(self.file1, "r") as f:
                otro = json.load(f)
            with open(self.file2, "r") as r:
                otro2 = json.load(r)

        except:
            pass
        
        for x in otro:
            for y in otro2:
                if x.keys() == y.keys():
                    clave = list(x.keys())[0]
                    clavesf = {**x[clave], **y[clave]}
                    estudiante = Estudiante(**clavesf)
                    sistema.agregar_funcion(estudiante)
        


def funcion_ordenar(x):
    promedio = x.__dict__["Promedio"]
    return promedio
def funcion_agregar(estudiante):
    final = {}
    nombre = {}
    diccionario_estudiante = estudiante.__dict__
    for clave, valor in diccionario_estudiante.items():
        if clave == "Documento":
            clave_final = valor
            nombre.setdefault(clave, valor)
        elif clave == "Nombre1":
            nombre.setdefault(clave, valor)
        elif clave == "Nombre2":
            nombre.setdefault(clave, valor)
        elif clave == "Apellido1":
            nombre.setdefault(clave, valor)
        elif clave == "Apellido2":
            nombre.setdefault(clave, valor)
        else:
            pass

    final.setdefault(clave_final, nombre)

    return (final)


def run():
    sistema = Sistema()
    sistema.iniciar()
    while True:
        comando = str(input('''
        **** Sistema registro Estudiantes Ing ****

        1. Ver estudiantes
        2. Agregar estudiante
        3. Ver estudiantes por inasistencias
        4. Ver estudiantes que pierden la asignatura
        5. Ver notas en matriz
        6. Ver estudiantes por carrera ordenados por promedio
        7. Salir

        '''))
        
        if comando == '1':
            sistema.ver_estudiantes()
        elif comando == '2':
            sistema.agregar_estudiante()
        elif comando == '3':
            sistema.estudiantes_inasistencias()
        elif comando == '4':
            sistema.ver_estudiantes_prom_3()
        elif comando == '5':
            sistema.ver_notas()
        elif comando == '6':
            sistema.ver_estudiantes_por_carrera()
        elif comando == '7':
            break
        else:
            print("Entrada inválida. Por favor intente de nuevo")
        

if __name__ == "__main__":
    run()
    
