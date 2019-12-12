#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

class Estudiante:
    """Clase Estudiante"""
    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            self.Documento = args[0]
            self.Nombre1 = args[1]
            self.Nombre2 = args[2]
            self.Apellido1 = args[3]
            self.Apellido2 = args[4]
            self.Carrera = args[5]
            self.Nota1 = args[6]
            self.Nota2 = args[7]
            self.Nota3 = args[8]
            self.Promedio = args[9]
            self.Inasistencias = args[10]
            self.Semestre = args[11]
        else:
            print(kwargs)

class Sistema:
    estudiantes = []
    estudiantes_tupla = []
    documentos = []
    file1 = "estudiantes.txt"
    file2 = "datos_academicos.txt"
    
    def agregar_estudiante(self):

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

        if Documento in self.documentos:
            pass
        else:
            self.documentos.append(Documento)
            self.estudiantes.append(estudiante.__dict__)

        diccio = {"1":self.estudiantes}
        jdic = json.dumps(diccio)
        print(type(jdic))
        with open(self.file1, "w") as file:
            file.write(jdic)
            print("yes")

def run():
    sistema = Sistema()
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
            pass
        elif comando == '2':
            sistema.agregar_estudiante()
        elif comando == '3':
            pass
        elif comando == '4':
            pass
        elif comando == '5':
            pass
        elif comando == '6':
            pass
        elif comando == '7':
            break
        else:
            print("Entrada inválida. Por favor intente de nuevo")
        

if __name__ == "__main__":
    run()
    
