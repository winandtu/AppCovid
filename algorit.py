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
        DatosRigor.append((Datos_Paciente()))
        DiagnosticoPrevio.append(Preguntas_Diagnostico())

def main():
    print(DatosRigor)
    print(DiagnosticoPrevio)
main()