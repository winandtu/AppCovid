import numpy as np
import matplotlib.pyplot as plt


IngresarPaciente="si"
c=0
class Persona:
    def __init__(self, nombre, cedula, sexo, edad, temperatura):
        self.nombre= nombre
        self.cedula= cedula
        self.sexo= sexo
        self.edad= edad
        self.temperatura= temperatura
    
    def __str__(self):
        return 'Nombre: {} \nCedula: {} \nSexo: {} \nEdad: {} \nTemperatura: {}'.format(self.nombre, self.cedula,self.sexo, self.edad, self.temperatura)

Nombre=input("\n"+"Nombre: ")
Cedula=int(input("Número de cedula: "))
Sexo=input("Sexo (M o F): ")
Edad=int(input("Edad: "))
Temperatura=int(input("Temperatura: "))

Danilo= Persona(Nombre, Cedula, Sexo, Edad, Temperatura)
print(Danilo.nombre)

#edward= Persona("fsdfsd", "4654", "dddd", "15", "35")
#print(edward)