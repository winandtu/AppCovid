import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#Matrices donde se guardaran los datos

#Funcion de crear  y registrar los pacientes



def AppCoron():
    
    MediaProbabilidad=[]
    AltaProbabilidad=[]
    BajaProbabilidad=[]
    DatosRigor=[]
    Sintomas=[]
    IngresarPaciente="si"

    print("....................................................")
    print("\nBIENVENIDO A LA PRECONSULTA\n")
  
    def Datos_Paciente():
        print("Ingrese los siguientes datos del paciente:\n")
        Nombre=input("Ingrese el nombre:\n>>")
        Cedula=int(input("Ingrese el numero de cedula:\n>>"))
        Sexo=input("Ingrese el sexo (M/F):\n")
        Edad=int(input("Ingrese la edad:\n"))
        Temperatura=int(input("Ingrese la temperatura:\n>>"))
        Fila=[Nombre,Cedula,Sexo,Edad,Temperatura]
        return Fila

    def Preguntas_Diagnostico():
        #Probabilidad de Covid-19 alta
        print('\nPor favor ingrese los siguientes datos del paciente '+'\n'+
            'y responda las preguntas con "si" o "no".')
        Ahogo=input("¿Siente sensacion de ahogo?\n>>")
        Olfato_Gusto=input("¿Ha perdido el sentido del gusto y del olfato?\n>>")
        Dolor_Pecho=input("¿Siente solor o presion en el pecho?\n>>")
        #Probabilidad de Covid-19 baja
        MalestarGarganta=input("¿Presenta malestar en la garganta?\n>>")
        Tos=input("¿Tiene tos seca?\n>>")
        Casancio=input("¿Siente cansancio?\n>>")
        Fila=[Ahogo,Olfato_Gusto,Dolor_Pecho,MalestarGarganta,Tos,Casancio]
        return Fila

    #Ingreso de Datos y Creacion de los Arreglos

    while(IngresarPaciente=="si"):
        DatosRigor.append((Datos_Paciente()))
        Sintomas.append(Preguntas_Diagnostico())
        IngresarPaciente=input("¿Desea Ingresar un nuevo paciente?\n>>")

    for i in range(0,len(Sintomas)): 
        c=0
        for j in range(0,6):        
            if Sintomas[i][j]=="si":
                c+=1   
        if c==6:
            AltaProbabilidad.append(DatosRigor[i])           
        elif c<=3:
            BajaProbabilidad.append(DatosRigor[i])        
        elif c>3 and c<6:
            MediaProbabilidad.append(DatosRigor[i])


    #Estudio estadistico

    #Cantidad de personas por rango de probabilidad

    #CantidadDePersonasAltaProbabilidad=len(AltaProbabilidad)
    #CantidadDePersonasMediaProbabilidad=len(MediaProbabilidad)
    #CantidadDePersonasBajaProbabilidad=len(BajaProbabilidad)


    #### Estudio para alta probabilidad

    #Cantidad de hombres y mujeres

    CantHomAltPro=0
    CantMujAltPro=0  
    for i in range(0,len(AltaProbabilidad)):        
        if AltaProbabilidad[i][2]=="M":            
            CantHomAltPro+=1
        if AltaProbabilidad[i][2]=="F":
            CantMujAltPro+=1

    #Rangos de edades
    EntreCeroYQuinceAños=0
    EntreQuinceYCuarenta=0
    EntreCuarentaySesenta=0
    DeSesentaEnAdelante=0
    for i in range(0,len(AltaProbabilidad)):
        if AltaProbabilidad[i][3]>=0 and AltaProbabilidad[i][3]<=15:
            EntreCeroYQuinceAños+=1
        if AltaProbabilidad[i][3]>15 and AltaProbabilidad[i][3]<=40:
            EntreQuinceYCuarenta+=1
        if AltaProbabilidad[i][3]>40 and AltaProbabilidad[i][3]<=60:
            EntreCuarentaySesenta+=1
        if AltaProbabilidad[i][3]>60:
            DeSesentaEnAdelante+=1

    #### Estudio para media probabilidad

    #Cantidad de hombres y mujeres

    CantHomMedPro=0
    CantMujMedPro=0   
    for i in range(0,len(MediaProbabilidad)):
        if MediaProbabilidad[i][2]=="M":
            CantHomMedPro+=1
        if MediaProbabilidad[i][2]=="F":
            CantMujMedPro+=1

    #Rangos de edades
    EntreCeroYQuinceAñosM=0
    EntreQuinceYCuarentaM=0
    EntreCuarentaySesentaM=0
    DeSesentaEnAdelanteM=0
    for i in range(0,len(MediaProbabilidad)):
        if MediaProbabilidad[i][3]>=0 and MediaProbabilidad[i][3]<=15:
            EntreCeroYQuinceAñosM+=1
        if MediaProbabilidad[i][3]>15 and MediaProbabilidad[i][3]<=40:
            EntreQuinceYCuarentaM+=1
        if MediaProbabilidad[i][3]>40 and MediaProbabilidad[i][3]<=60:
            EntreCuarentaySesentaM+=1
        if MediaProbabilidad[i][3]>60:
            DeSesentaEnAdelanteM+=1

    #### Estudio para baja probabilidad

    #Cantidad de hombres y mujeres

    CantHomBajPro=0
    CantMujBajPro=0
    for i in range(0,len(BajaProbabilidad)):
        if BajaProbabilidad[i][2]=="M":
            CantHomBajPro+=1
        if BajaProbabilidad[i][2]=="F":
            CantMujBajPro+=1

    #Rangos de edades
    EntreCeroYQuinceAñosB=0
    EntreQuinceYCuarentaB=0
    EntreCuarentaySesentaB=0
    DeSesentaEnAdelanteB=0
    for i in range(0,len(BajaProbabilidad)):
        if BajaProbabilidad[i][3]>=0 and BajaProbabilidad[i][3]<=15:
            EntreCeroYQuinceAñosB+=1
        if BajaProbabilidad[i][3]>15 and BajaProbabilidad[i][3]<=40:
            EntreQuinceYCuarentaB+=1
        if BajaProbabilidad[i][3]>40 and BajaProbabilidad[i][3]<=60:
            EntreCuarentaySesentaB+=1
        if BajaProbabilidad[i][3]>60:
            DeSesentaEnAdelanteB+=1

    #Nombres segun Rango De Probabilidad

    print("Los pacientes que tiene una probabilidad alta de  tener Covid-19 son:")
    for i in range(0,len(AltaProbabilidad),1):
        print(AltaProbabilidad[i][0])

    print("Los pacientes que tiene una probabilidad media de  tener Covid-19 son:")
    for i in range(0,len(MediaProbabilidad),1):
        print(MediaProbabilidad[i][0])

    print("Los pacientes que tiene una probabilidad baja de  tener Covid-19 son:")
    for i in range(0,len(BajaProbabilidad),1):
        print(BajaProbabilidad[i][0])

    #Graficas por medio de matplotlib        
    Graficas=input('¿Desea obtener graficas por cada rango de probabilidaes? - (si indica "no" podrá eligir generarlas todas) - ')
    k=input("¿Desea generarlas todas?")
    while Graficas=="si":    
        print("- Según la cantidad de hombres y mujeres"+"\n"+"1. Alta probabilidad"+"\n"+"2. Media probabilidad"+"\n"+"3. Baja probabilidad"+"\n"+
              "- Según el rango de edades"+"\n"+"4. Alta probabilidad"+"\n"+"5. Media probabilidad"+"\n"+"6. Baja probabilidad")
        p=int(input("Marque el número correspondiente: "))
        if(p>=1 and p<=3):
            if(p==1):
                p=0
            elif(p==3):
                p=4
            nme=['1-Alta probabiliad en hombres y mujeres.png','2-Media probabilidad en hombres y mujeres.png','3-Baja probabilidad en hombres y mujeres.png']           
            aho=[CantHomAltPro,CantMujAltPro,CantHomMedPro,CantMujMedPro,CantHomBajPro,CantMujBajPro]
            tlu=['Alta probabiliad en hombres y mujeres','Media probabilidad en hombres y mujeres','Baja probabilidad en hombres y mujeres']
            Legendas=["Hombres","Mujeres"]
            sizes=[aho[p],aho[p+1]]
            fig1,ax1=plt.subplots()
            _, _, texto=ax1.pie(sizes,labels=Legendas,autopct='%1.1f%%',startangle=90)
            for tex in texto:
                tex.set_color('white')
            ax1.axis('equal')
            if(p==2):
                p=1
            elif(p==4):
                p=2
            plt.title(tlu[p])
            plt.savefig(nme[p])        
        else:
            if(p==4):
                p=0
            elif(p==5):
                p=4
            elif(p==6):
                p=8
            nme2=['4-Alta probabilidad entre 0 y 60 años.png','5-Media probabilidad entre 0 y 60 años.png','6-Baja probabilidad entre 0 y 60 años.png']
            aho2=[EntreCeroYQuinceAños,EntreQuinceYCuarenta,EntreCuarentaySesenta,DeSesentaEnAdelante,EntreCeroYQuinceAñosM,EntreQuinceYCuarentaM,EntreCuarentaySesentaM,
                  DeSesentaEnAdelanteM,EntreCeroYQuinceAñosB,EntreQuinceYCuarentaB,EntreCuarentaySesentaB,DeSesentaEnAdelanteB]
            tlu2=['Alta probabilidad entre 0 y 60 años','Media probabilidad entre 0 y 60 años','Baja probabilidad entre 0 y 60 años']
            Legendas=["De 0 a 15","Más de 15 y menor o igual a 40","Más de 40 y menor o igual 60","Más de 60"]
            sizes=[aho2[p],aho2[p+1],aho2[p+2],aho2[p+3]]
            fig1,ax1=plt.subplots()
            _, _, texto=ax1.pie(sizes,labels=Legendas,autopct='%1.1f%%',startangle=90)
            for tex in texto:
                tex.set_color('white')
            ax1.axis('equal')
            if(p==4):
                p=1
            elif(p==8):
                p=2
            plt.title(tlu2[p])
            plt.savefig(nme2[p])
        print("")
        Graficas=input("¿Desea obtener otra grafica? - ")
        print("")
    if(k=="si"):
            for p in range(1,7):   
                if(p>=1 and p<=3):
                    if(p==1):
                        p=0
                    elif(p==3):
                        p=4
                    nme=['1-Alta probabiliad en hombres y mujeres.png','2-Media probabilidad en hombres y mujeres.png','3-Baja probabilidad en hombres y mujeres.png']           
                    aho=[CantHomAltPro,CantMujAltPro,CantHomMedPro,CantMujMedPro,CantHomBajPro,CantMujBajPro]
                    tlu=['Alta probabiliad en hombres y mujeres','Media probabilidad en hombres y mujeres','Baja probabilidad en hombres y mujeres']
                    Legendas=["Hombres","Mujeres"]
                    sizes=[aho[p],aho[p+1]]
                    fig1,ax1=plt.subplots()
                    _, _, texto=ax1.pie(sizes,labels=Legendas,autopct='%1.1f%%',startangle=90)
                    for tex in texto:
                        tex.set_color('white')
                    ax1.axis('equal')
                    if(p==2):
                        p=1
                    elif(p==4):
                        p=2
                    plt.title(tlu[p])
                    plt.savefig(nme[p])        
                else:
                    if(p==4):
                        p=0
                    elif(p==5):
                        p=4
                    elif(p==6):
                        p=8
                    nme2=['4-Alta probabilidad entre 0 y 60 años.png','5-Media probabilidad entre 0 y 60 años.png','6-Baja probabilidad entre 0 y 60 años.png']
                    aho2=[EntreCeroYQuinceAños,EntreQuinceYCuarenta,EntreCuarentaySesenta,DeSesentaEnAdelante,EntreCeroYQuinceAñosM,EntreQuinceYCuarentaM,EntreCuarentaySesentaM,
                          DeSesentaEnAdelanteM,EntreCeroYQuinceAñosB,EntreQuinceYCuarentaB,EntreCuarentaySesentaB,DeSesentaEnAdelanteB]
                    tlu2=['Alta probabilidad entre 0 y 60 años','Media probabilidad entre 0 y 60 años','Baja probabilidad entre 0 y 60 años']
                    Legendas=["De 0 a 15","15< y <=40","40< y <=60","Más de 60"]
                    sizes=[aho2[p],aho2[p+1],aho2[p+2],aho2[p+3]]
                    fig1,ax1=plt.subplots()
                    _, _, texto=ax1.pie(sizes,labels=Legendas,autopct='%1.1f%%',startangle=90)
                    for tex in texto:
                        tex.set_color('white')
                    ax1.axis('equal')
                    if(p==4):
                        p=1
                    elif(p==8):
                        p=2
                    plt.title(tlu2[p])
                    plt.savefig(nme2[p])


#Creación del menu  
def menu():
   
    salir=3
    
    while True:
        archivo= open("Titulo.txt")
        inf= open("info.txt")
        print(archivo.read())

        print("\n1. Iniciar consulta", "\n2. Informacion del programa ", "\n3. Salir")
        op= int(input("Por favor, ingresa tu opción: "))
        #regresa= int(input("¿Desea regresar al menu prinpal?\n"+ "\n1.Si"+ "\n2.No"+"\n>>"))

        if(op==1):
            AppCoron()
            break
        elif(op==2):
            print(inf.read())
            regresa= int(input("¿Desea regresar al menu prinpal?\n"+ "\n1.Si"+ "\n2.No"+"\n>>"))
            if(regresa==1):
                menu()
            else:
                print("\nGRACIAS POR UTILIZAR LA APLICACIÓN")
                break
            break
        elif(op==salir):
            print("\nGRACIAS POR UTILIZAR LA APLICACIÓN")
            break 
    
menu()