
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DatosRigor=[]
Sintomas=[]
AltaProbabilidad=[]
bajaProbabilidad=[]
mediaProbabilidad=[]
nombrPersonas=[]
AhogoM=[]
Olfato_GustoM=[]
Dolor_PechoM=[]
MalestarGargantaM=[]
TosM=[]
CansancioM=[]
IngresarPaciente="si"
c=0

print("BIENVENIDO A LA PRECONSULTA")
print('Por favor ingrese los siguientes datos del paciente '+'\n'+
      'y responda las preguntas con "si" o "no".')

while(IngresarPaciente=="si"):
    Nombre=input("\n"+"Nombre: ")
    Cedula=int(input("Número de cedula: "))
    Sexo=input("Sexo (M o F): ")
    Edad=int(input("Edad: "))
    Temperatura=int(input("Temperatura: "))
    Fila1=Nombre,Cedula,Sexo,Edad,Temperatura
    PersonNom= [Nombre]
    #Probabilidad de Covid-19 alta
    print("\n"+"¿Presenta los siguientes síntomas?")
    Ahogo=input("Sensacion de ahogo: ")
    Olfato_Gusto=input("Perdida del sentido del gusto y del olfato: ")
    Dolor_Pecho=input("Dolor o presión en el pecho: ")
    #Probabilidad de Covid-19 baja
    MalestarGarganta=input("Malestar en la garganta: ")
    Tos=input("Tos seca: ")
    Cansancio=input("Cansancio: ")
    Fila2=[Ahogo,Olfato_Gusto,Dolor_Pecho,MalestarGarganta,Tos,Cansancio]       
    DatosRigor.append(Fila1)
    Sintomas.append(Fila2)
    nombrPersonas.append(PersonNom)

    #Aqui categoriza 
    if(Sintomas[c][0]==Sintomas[c][1]==Sintomas[c][2]=="si" or Sintomas[c][0]==Sintomas[c][1]==Sintomas[c][2]== Sintomas[c][3]==Sintomas[c][4]==Sintomas[c][5]=="si"):
        
        AltaProbabilidad.append(Nombre)
    elif(Sintomas[c][3]==Sintomas[c][4]==Sintomas[c][5]=="si" or Sintomas[c][0]==Sintomas[c][1]==Sintomas[c][2]== Sintomas[c][3]==Sintomas[c][4]==Sintomas[c][5]=="no"):
        bajaProbabilidad.append(Nombre)
    else:
        mediaProbabilidad.append(Nombre)
    c=c+1 

    if(Ahogo=="si"):
        AhogoM.append(Ahogo)
    if(Olfato_Gusto=="si"):
        Olfato_GustoM.append(Olfato_Gusto)
    if(Dolor_Pecho=="si"):
        Dolor_PechoM.append(Dolor_Pecho)
    if(MalestarGarganta=="si"):
        MalestarGargantaM.append(MalestarGarganta)
    if(Tos=="si"):
        TosM.append(Tos)
    if(Cansancio=="si"):
        CansancioM.append(Cansancio)
    IngresarPaciente=input("\n"+"¿Desea registrar a otro paciente? - ")


def getAlta(AltaProbabilidad):

    
    personas= {'  Nombres':AltaProbabilidad  }
    df= pd.DataFrame(data= personas)

    print("Personas con Alta probabilidad de contagio")
    print("------------------------------------------------")
    print(df)
    print("------------------------------------------------")

def getBaja(bajaProbabilidad):

    personas= {'  Nombres':bajaProbabilidad }
    df= pd.DataFrame(data= personas)
    
    print("Personas con Baja probabilidad de contagio")
    print("------------------------------------------------")
    print(df)
    print("------------------------------------------------")
    
def getMedia(mediaProbabilidad):

    personas= {'  Nombres':mediaProbabilidad }
    df= pd.DataFrame(data= personas)

    print("Personas con Media probabilidad de contagio")
    print("------------------------------------------------")
    print(df)
    print("------------------------------------------------")


def OpProbabilidad(AltaProbabilidad, mediaProbabilidad, bajaProbabilidad  ):
    print("Que probabilidades de contagio desea conocer?")
    print("\n1. Probabilidad Alta"+"\n2. Probabilidad Media"+"\n3. Probabilidad Baja\n")
    op= int(input("Ingresa tu opción: "))

    if(op==1):
        getAlta(AltaProbabilidad)
    elif(op==2):
        getMedia(mediaProbabilidad)
    elif(op==3):
        getBaja(bajaProbabilidad)
    else:
        print("Opcion invalida")
    op2=input("Desea realizar nueva consulta de las probabilidades? si/no: ")

    if(op2=="si"):
        OpProbabilidad(AltaProbabilidad, mediaProbabilidad, bajaProbabilidad  )
    else:
        print("Gracias por su consulta")

def main():

    OpProbabilidad(AltaProbabilidad, mediaProbabilidad, bajaProbabilidad  )

main()

#personas= {'Nombres':AltaProbabilidad }
#df= pd.DataFrame(data= personas)
#print(df)
#print(Sintomas)
#print(Sintomas)