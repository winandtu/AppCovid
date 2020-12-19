import random
import matplotlib.pyplot as plt
Enfermedades=["Diabetes","Cáncer","Ninguna"]
Antecedente=["Fractura","Transplante de riñon"]

Historia=[]
H=[]
DatosRigor=[]
Sintomas=[]
AltaProbabilidad=[]
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

    #Probabilidad de Covid-19 alta
    print("\n"+"¿Presenta los siguientes síntomas?")
    Ahogo=input("Sensacion de ahogo: ")
    Olfato_Gusto=input("Perdida del sentido del gusto y del olfato: ")
    Dolor_Pecho=input("Dolor o presión en el pecho: ")
    #Probabilidad de Covid-19 baja
    MalestarGarganta=input("Malestar en la garganta: ")
    Tos=input("Tos seca: ")
    Cansancio=input("Cansancio: ")
    Fila2=Ahogo,Olfato_Gusto,Dolor_Pecho,MalestarGarganta,Tos,Cansancio       
    DatosRigor.append(Fila1)
    Sintomas.append(Fila2)
    H.append(Enfermedades[random.randrange(3)])
    H.append(Antecedente[random.randrange(2)])
    Historia.append(H)
    H=[]
    if(Sintomas[c][3]==Sintomas[c][4]==Sintomas[c][5]=="si"
       and (Sintomas[c][0]==Sintomas[c][2]=="si" or Sintomas[c][1]==Sintomas[c][2]=="si" or Sintomas[c][1]==Sintomas[c][0]=="si") and DatosRigor[c][4]>=37,5): 
        AltaProbabilidad.append(Cedula)    
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
    
#Graficas de sintomas y de probabilidad
Graficas=input("¿Desea guardar graficas?")
if(Graficas=="si"):
    AProbabilidad=["Alta probabilidad","Baja probabilidad"]
    sizes=[len(AltaProbabilidad),c-len(AltaProbabilidad)]
    fig1,ax1=plt.subplots()
    _, _, texto=ax1.pie(sizes,labels=AProbabilidad,autopct='%1.1f%%',startangle=90)
    for tex in texto:
        tex.set_color('white')
    ax1.axis('equal')
    plt.title("Probabilidad de presentar la enfermedad")
    plt.savefig('12-Probabilidad.png')
    
    CAhogo=["Con ahogo","Sin ahogo"]
    sizes=[len(AhogoM),c-len(AhogoM)]
    fig1,ax1=plt.subplots()
    _, _, texto=ax1.pie(sizes,labels=CAhogo,autopct='%1.1f%%',startangle=90)
    for tex in texto:
        tex.set_color('white')
    ax1.axis('equal')
    plt.title("Ahogo")
    plt.savefig('13-Ahogo.png')

    CPerdida=["Con pérdida","Sin perdida"]
    sizes=[len(Olfato_GustoM),c-len(Olfato_GustoM)]
    fig1,ax1=plt.subplots()
    _, _, texto=ax1.pie(sizes,labels=CPerdida,autopct='%1.1f%%',startangle=90)
    for tex in texto:
        tex.set_color('white')
    ax1.axis('equal')
    plt.title("Pérdida del olfato y gusto")
    plt.savefig('14-Pérdida del olfato y gusto.png')

    CDolor=["Con dolor","Sin dolor"]
    slices=[len(Dolor_PechoM),c-len(Dolor_PechoM)]
    fig1,ax1=plt.subplots()
    _, _, texto=ax1.pie(sizes,labels=CDolor,autopct='%1.1f%%',startangle=90)
    for tex in texto:
        tex.set_color('white')
    ax1.axis('equal')
    plt.title("Dolor en el pecho")
    plt.savefig('15-Dolor en el pecho.png')

    CMalestar=["Con malestar","Sin malestar"]
    sizes=[len(MalestarGargantaM),c-len(MalestarGargantaM)]
    fig1,ax1=plt.subplots()
    _, _, texto=ax1.pie(sizes,labels=CMalestar,autopct='%1.1f%%',startangle=90)
    for tex in texto:
        tex.set_color('white')
    ax1.axis('equal')
    plt.title("Malestar en la garganta")
    plt.savefig('16-Malestar en la garganta.png')

    CTos=['Con tos','Sin tos']
    sizes=[len(TosM),c-len(TosM)]
    fig1,ax1=plt.subplots()
    _, _, texto=ax1.pie(sizes,labels=CTos,autopct='%1.1f%%',startangle=90)
    for tex in texto:
        tex.set_color('white')
    ax1.axis('equal')
    plt.title("Tos seca")
    plt.savefig('17-Tos seca.png')
    
    CCansancio=["Con cansancio","Sin cansancio"]
    sizes=[len(CansancioM),c-len(CansancioM)]
    fig1,ax1=plt.subplots()
    _, _, texto=ax1.pie(sizes,labels=CCansancio,autopct='%1.1f%%',startangle=90)
    for tex in texto:
        tex.set_color('white')
    ax1.axis('equal')
    plt.title("Cansancio")
    plt.savefig('18-Cansancio.png')
