DatosRigor=[]
DiagnosticoPrevio=[]
IngresarPaciente="si"

def Datos_Paciente():
    Nombre=input("Ingrese el nombre del paciente:\n")
    Cedula=int(input("Ingrese el numero de cedula:\n"))
    Sexo=input("Ingrese el sexo del paciente:\n")
    Edad=int(input("Ingrese la edad del paciente:\n"))
    Temperatura=int(input("Ingrese la temperatura del paciente:\n"))
    Fila=[Nombre,Cedula,Sexo,Edad,Temperatura]
    return Fila
def Preguntas_Diagnostico():
    #Probabilidad de Covid-19 alta
    Ahogo=input("¿Siente sensacion de ahogo?")
    Olfato_Gusto=input("¿Ha perdido el sentido del gusto y del olfato?")
    Dolor_Pecho=("¿Siente solor o presion en el pecho?")
    #Probabilidad de Covid-19 baja
    MalestarGarganta=input("¿Presenta malestar en la garganta?")
    Tos=input("¿Tiene tos seca?")
    Casancio=input("¿Siente cansancio?")
    Fila=[Ahogo,Olfato_Gusto,Dolor_Pecho,MalestarGarganta,Tos,Casancio]
    return Fila
    
while (IngresarPaciente!="salir"):
    print("BIENVENIDO A LA PRECONSULTA")
    PRINT("POR FAVOR RESPONDA A LAS PREGUNTAS CON SI O NO EN MINUSCULAS")
    IngresarPaciente=input("¿Desea ingresar un nuevo paciente si o no?\n>>")
    if(IngresarPaciente=="si"):
        DatosRigor.append((Datos_Paciente()))
        DiagnosticoPrevio.append(Preguntas_Diagnostico())