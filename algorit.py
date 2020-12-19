import numpy as np
DatosRigor=[]
DiagnosticoPrevio=[]
IngresarPaciente="si"
#contador=0
#def Datos_Paciente():
 #   Nombre=input("Ingrese el nombre del paciente:\n")
 #   Cedula=int(input("Ingrese el numero de cedula:\n"))
    #Sexo=input("Ingrese el sexo del paciente:\n")
    #Edad=int(input("Ingrese la edad del paciente:\n"))
    #Temperatura=int(input("Ingrese la temperatura del paciente:\n"))
    #Fila=[Nombre,Cedula,Sexo,Edad,Temperatura]
  #  Fila=[Nombre, Cedula]
   # return Fila

def Preguntas_Diagnostico():
    #texto=""
    #Probabilidad de Covid-19 alta
    Ahogo=input("¿Siente sensacion de ahogo?")
    Olfato_Gusto=input("¿Ha perdido el sentido del gusto y del olfato?")
    Dolor_Pecho=input("¿Siente dolor o presion en el pecho?")
    #doloPecho=("¿Siente dolor o presion en el pecho?", Dolor_Pecho)
    #Probabilidad de Covid-19 baja
    MalestarGarganta=input("¿Presenta malestar en la garganta?")
    Tos=input("¿Tiene tos seca?")
    Casancio=input("¿Siente cansancio?")
    #texto+= "Sensacion de ahogo: "+Ahogo+ "\n Perdida del gusto y el olfato: "+Olfato_Gusto
    Fila=[Ahogo,Olfato_Gusto,Dolor_Pecho,MalestarGarganta,Tos,Casancio]
    #Fila= [texto]
    return Fila
    
while (IngresarPaciente!="no"):
    print("BIENVENIDO A LA PRECONSULTA")
    print("POR FAVOR RESPONDA A LAS PREGUNTAS CON SI O NO EN MINUSCULAS")
    IngresarPaciente=input("¿Desea ingresar un nuevo paciente si o no?\n>>")
    if(IngresarPaciente=="si"):
        #DatosRigor.append((Datos_Paciente()))
        DiagnosticoPrevio.append(Preguntas_Diagnostico())


def prioridad(DiagnosticoPrevio):
    contador=0
    #for i in range (0,6,1):
     #print(DiagnosticoPrevio[0][i])
    
        if(DiagnosticoPrevio[0][0]=="si" and DiagnosticoPrevio[0][1]=="si" and DiagnosticoPrevio[0][2]=="si" ):
           print("Tiene alta probabilidad de covid")
        #else:
         #   print("Tiene baja probabilidad de covid")


    #for i in range (0, 6, 1): 
     #   print(i,DiagnosticoPrevio[0][i])
            #y= "Alta probabilidad de covid"
            #print(y)
            #print(contador)

def main():
    prioridad(DiagnosticoPrevio)

main()







#print(DiagnosticoPrevio)
#print(DiagnosticoPrevio[0][2])