#MENU de opciones para uso de listas, tuplas, diccionarios
#apliacione a diversos ejercicios
#definicion de METODOS (funcione o procedimentos)

import Modulo1
import numpy as np
import statistics as stat
import matplotlib.pyplot as plt
import pandas as pd


def imprimir(texto,listax):
    for indice, i in enumerate(listax):
        print("El elemento", indice,"de",texto,"es:",i)
#####
def Fserie1(numero):
    Rpta=0
    x=3; i=1
    while(x<=numero):
        Rpta = Rpta + (x-1)/(x)
        print("Iteracion",i,":M=",Rpta)
        x=x+1
        i=i+1
    return Rpta
#####
def calcular_venta(p_compra, g_porcentaje):
    
    p_venta = p_compra * (1 + g_porcentaje / 100)
    return p_venta

def Busqueda_Lienal(listax,valor):
    Rpta=-1 # no se pone 0 porque es una posicion valida, -1 indica que no se envontro el valor 
    pos=0
    for z in listax:
        if z == valor:
            Rpta=pos
            return Rpta #cuando se encuentra el valor y termina el metodo 
        pos=pos+1
    return Rpta # cuando no se encuentra el valor 
###################
def Busqueda_Binaria(lista,elemento):
    izq=0
    der = len(lista) -1
    print("LONGITUD=",len(lista))
    while izq <= der:
        medio =int((izq+der)/2)
        print("DEBUG: ","izq: ",izq,"der: ",der,"medio: ",medio)
        if lista[medio]==elemento:
            return medio
        else:
            if lista[medio]>elemento:
                der=medio-1
            else:
                izq = medio+1
    return(-1)
######################
#definiiocn de variables
op = 0 #op(designa la opcion elegida en el menu)
###variables para caso 1
pA=0; pB=0; pC=0; pT=0; total=0; k=0; A=0; B=0; C=0
###variables para caso 2
a=0; b=0 ;  c=0  ; D=0; x1Real=0; x2Real=0  ;x1Imag=0j ; x2Imag=0j

###varaibles para caso 7
ListaGlobal=["MATEMATICA APLICADA","SJL","1ro",7.5]

ListaGlobal1=["ingles","comunicacion","metodoligas",3,6]


while(op!=40):

    print("\n\nMENU DE OPCIONES")
    print("[1]PROBLEMA DE PRORRATEO DE GASTOS")
    print("[2]SOLUCION DE ECUACION CUADRATICA")
    print("[3] USO DE LISTAS")
    print("[4]USO DE TUPLAS")
    print("[5]USO DE DICCIONARIO")
    print("[6]USO DE FOR")
    print("[7]USO DE FOR con listas, tuplas etc")
    print("[8]verificador de numero primos")
    print("[9]USO DE FOR con metodos")
    print("[10]USO DE WHILE para resolver una serie ")
    print("[11]Dados un valor de N que ubduca el dominador final. Halle M")
    print("[12]problema de compra y venta mediante metdo (Funcion)")
    print("[13]ORDENACION DE LISTAS")
    print("[14]CONVERSION DE CADENA A LISTA Y VICIVERSA")
    print("[15]")
    print("[16]")
    print("[17]")
    print("[17]USO DE map para convertir una lista en sus cuadrado mediante MODULO1.py")
    print("[28]grafocp de funciones valor absoluto")
    print("[32]")
    print("[40]SALIR")

    op= float(input("ingrese opcion"))

    match op:
        case 1:
            print("[1]problema de prorrateo de gastos")
            total=float(input("ingrese el valor total"))
            pA=float(input("ingrese el fatoc de proporcion de A:"))
            pB=float(input("ingrese el fatoc de proporcion de B:"))
            pC=float(input("ingrese el fatoc de proporcion de C:"))
            pT=(pA+pB+pC)
            k=total/pT #alculo de factor de proporcionalidad
            A=pA*k; B=pB*k; C=pC*k #asignacion del prorratear
            print("el socio A recibe:",A)
            print("el socio B recibe:",B)
            print("el socio C recibe:",C)

        case 2:

            a= float(input("Ingrese valor de a:") )
            b= float(input("Ingrese valor de b:") )
            c= float(input("Ingrese valor de c:") )
            D= b**2 - 4*a*c

            if D>=0:
                print("La solucion es real")     
                x1Real=(-b + D**(1/2) )/(2*a)
                x2Real=(-b - D**(1/2) )/(2*a)
                print("x1= {:.2f}".format(x1Real))
                print("x2= {:.2f}".format(x2Real))
            else:
                print("La solucion es compleja")      
                x1Imag=(-b + D**(1/2) )/(2*a)
                x2Imag=(-b - D**(1/2) )/(2*a)
                print("x1= {:.2f}".format(x1Imag))
                print("x2= {:.2f}".format(x2Imag))
            print("FIN DEL PROGAMA")    
        
        case 3:
            print("[3]USO DE LISTAS")
            print("lista de notas de los primeros 3 entregables")
            LNotas=[13,15,17]
            print("lisat de notas:",LNotas) 
            nota4=int(input("ingrese nota de entregable 4"))
            LNotas.append(nota4) # se añadio nota4 como nuevo elemento de lista
            print("lista de notas:",LNotas)
            print("numero de elementos de la lista=",len(LNotas))
            print("numero de veces de notas 15=",LNotas.count(23))
        
        
        
        
        case 3.1:
            print("uso del comando copy y clear")
            LCursos = ['mate','comu','ingles'] # lista de cursos
            LInst = ['Cibertec','Senati','Idat','Certus',] # lista de institutos academicos
            LAlum = ['Sebas','Alejandor','Johan'] # alumnos de cibertec
            LProfe =['Jhon Bravo']
            print("listas para la tarea:",LAlum,LCursos,LInst,LProfe)
            
            
            print("lista de cursos:",LCursos)
            c = LCursos.copy() #lista copiada
            print("antes de clear")
            print("LCursos",LCursos)
            print("c:",c)
            
            print("UTILIZANDO EL METODO CLEAR")
            c.clear() #limpia la lista seleccionada
            print("despues de clear")
            print("LCursos",LCursos)
            print("c:",c)
            
            print("UTILIZANDO EL METODO EXTEND") 
            print("lista de alumnos:",LCursos)
            institucion_profe = ['Jhon Bravo'] 
            LCursos.extend(institucion_profe) #se utiliza para agregar varios elementos a una lista
            print("lista actualizada:",LCursos)
            
            print("UTILIZANDO EL METODO INDEX")
            print("lista de institutos:",LInst) 
            posicion = LInst.index('Certus') #se usa para encontrar la posicion de un elemento
            print("lista con el elemento selecionado:",posicion)
            
            print("UTILIZANDO EL METODO INSERT")
            print("lista de alumnos de certus:",LAlum)
            LAlum.insert(3,'Hairo') # se utiliza para agregar un elemento mas a la lista 
            print("lista con un integrante mas:",LAlum)
            
            print("UTILIZANDO EL METODO POP")
            print("lista con el metedo pop:",LInst)
            LInst.pop(1) # elemina de la lisa en oreden de numeracion 0.1.2.3...ETC
            print("lista actulizada:",LInst)
            
            print("UTILIZANDO EL METEDO REMOVE")
            print("lista de instituciones academicas:",LInst)
            LInst.remove('Idat') # elimina de la lista el elemento seleccionado 
            print("lista actulizada:",LInst)
            
            print("UTILIZANDO EL METEDO REVERSE")
            print("lista de alumnos de certus:",LAlum)
            LAlum.reverse() # revierte la lista del ultimo al primero
            print("lista aplicando reverse:",LAlum)
            
            print("UTILIZANDO EL METODO SORT")
            print("lista de alumnos de certus:",LAlum)
            LAlum.sort() #ordena la lista en orden alfabetico y numerico
            print("lista ordenada aplicando sort:",LAlum)
            
            
        case 4:
            print("[4]USO DE TUPLAS")
            persona=("Sebastian","Argentina","Bs As",35)
            LAlum = ("Sebas","Alejandor","Johan") # alumnos de cibertec
            marcas=("hyundai","toyota","ford")
            print("tupla:",persona)
            print("longitud:",len(persona))
            print("posicion de elementos Peru:",persona.index("Argentina"))
            print("#veces que aparece Lima=", persona.count("Buenos Aires"))
            
            print("LISTA DE TUPLAS")
            print("."*20)
            print("tuplas1:",LAlum)
            print("tupla2:",marcas)
            tupla=(LAlum,marcas)
            print("lista de tuplas combinadas:",tupla)

        case 5:
            print("[5] USO DE DICCIONARIO")
            MisDatos={
                        "nombre":"Hairo",
                        "apellido":"Tarmeño",
                        "ocupacion":"alumno",
                        "edad":23,
                        "honestidad":True,
                        "estatura":1.70,
                        "padres":("Geraldine","Wyllian")
                }
            print("diccionario de mis datos personales:\n",MisDatos)    

        case 6:
            print("[6] USO DE FOR")
            suma = 0
            print("suma de los primeros numeros naturales:\n")
            num=int(input("Ingrese cantidad de numeros"))# 1+2+3+4...+num
            for i in range(num):
              i = i+1 #para aumentar una unidad mas ya que comienza de 0
              suma = suma+i
            sumafinal = suma
            print("la suma de los primeros",num,"naturales=",sumafinal)

            print("la suma de numeros naturales consecutivos entre num1 y num2:\n")
            num1=int(input("ingrese numero inicial:"))
            num2=int(input("ingrese numer final:"))
            for i in range(num1, num2 + 1):
                suma= suma+i
            print("la suma total es  =",suma)

        case 7:
            print("[7] USo de for con listas, tuplas etc")
            print("Reporte de elements de la lista")
            indice = 0
            for i in ListaGlobal: # i es la variable que toma el control de la lista 
                print("Elemento nro",indice,"=",i)
                indice = indice+1
            
            print("\nReporte de elementos de la lista mediante for con enumerate")
            for inidice, i in enumerate(ListaGlobal):
                print("Elemento nro",indice,"=",i)
        case 8:
            print("[8]verificador de numero primos")
            print("numero primos")
            primos = 2, 3, 5, 7, 11, 13, 17, 19, 23
            print("91 sera primo cuando sea")
            for i in range(2,9+1):
                if (91%i) == 0: # Comprueba si 91 es divisible por i
                    print(i, "divide a 91")
                    break
                else:
                    print(i, "no divide a 91")
                    



        case 9:
            print("[9]USO DE FOR con metodos")
            print("salida de listaglobal1 mediante metodo(procedimiento) inprimir:\n")
            imprimir("Lista de datos",ListaGlobal1)
            print("fin del metodo_")


  
        case 10:
            print("[10]USO DE WHILE para resolver una serie ")
            print("Dados un valor de N que ubduca el dominador final. Halle M ")
            print(" M=2/3 + 3/4 + 4/5 +...")
            print("Ejem N=6--> 2/3 + 3/4 + 4/5 + 5/6 ")
            print("\nEjem: N=4--> 2/3 + 3/4")
            N = int( input("ingrese el valor fr dominador final N:"))

            M=0 ; x=3 ; i=1
            while(x<=N):
              M = M+(x+1)/(x)
              print("\nIteracion",i,":M=",M)
              x=x+1
              i=i+1

            print("\nmfinal=", round(M,2))
        
        case 11:
            print("Dados un valor de N que ubduca el dominador final. Halle M ")
            print(" M=2/3 + 3/4 + 4/5 +...")
            print("Ejem N=6--> 2/3 + 3/4 + 4/5 + 5/6 ")
            print("\nEjem: N=4--> 2/3 + 3/4")
            N = int( input("ingrese el valor fr dominador final N:"))
            M=0
            M=Fserie1(N)
            
            print("\nmfinal=", round(M,2))
        
        
        
        case 12:
            print("[12]problema de compra y venta mediante metodo funcio")
            print("Dado un precio de compar y venta una ganancai en %. Halle el precio de venta")
            p_compra = float(input("Ingrese el precio de compra: "))
            g_porcentaje = float(input("Ingrese la ganancia en %: "))
            p_venta = calcular_venta(p_compra, g_porcentaje)
            ###formula de precio de  
            print("El precio de venta es:",round(p_venta))

        case 13:
            print("[13]ORDENACION DE LISTAS")
            ListaNotas=[14,16,10,13]
            print("Lista de notas INICICAL:\n")
            print(ListaNotas)
            ListaOrdenada=sorted(ListaNotas)
            print("\nlista de notas ordenada en una nueva lista\n")
            imprimir("Notas ordenada",ListaOrdenada)
            print("\nLista de notas ordenada e lista INICIAL:\n")
            ListaNotas.sort()
            imprimir("Lista inicial ordenada,",ListaNotas)





        case 14:
            print
            oracion=str(input("Ingrese una oracion:"))
            caracter=str(input("ingrese el caracter delimitador de la lista:"))
            Lista3=oracion.split(caracter) 
            print("\ncadena original:",oracion)
            print("\nlistagenerada:",Lista3)
            print("\n[14]conversion de lista a cadena\n")
            caracter=str(input("Ingrese el caracter delimitador de la oracion"))
            cadena2=caracter.join(Lista3)
            print("\nCadena generada:",cadena2)         
        

        case 15:
            print("[15]BUSQUEDA SECUENCIAL O LINEAL EN LISTA")
            ListaNotas=[14,16,10,13,12,20,18]
            nota=int(input("ingrese la nota a buscar"))
            posicion = Busqueda_Lienal(ListaNotas,nota)
            if(posicion!=-1):
                print("la nota buscada:", nota,"es la nota de nro",posicion)
            else:
                print("la nota buscada:",nota,"no se encuentra en la Lista de notas")

        case 16:
            print("[]")
            print()
            lista=input("ingrese una lista ordenada separada por comas:")
            lista=lista.split(",")
            lista=list(map(int,lista)) # map realiza una operrcion de la lista a cada elemento de la lista 
            # list es un metodo que convierte el contenido a una lista
            #usar tuple()para convertir a tupla
            print("Lista ordenada:",lista)
            
            lista !=[[]]
            x= int(input("ingrese el valor buscando:"))
            resultado = Busqueda_Binaria(lista,x)
            print("El valor buscado esta en la posicion:",resultado)
            
           
            
        case 17:
            print("[17]")
            ListaNotas = [8,12,15,13]
            valor=15
            print("\nBUSQUEDA CON INDEX")
            print("ListaNotas:",ListaNotas)
            posicion=Busqueda_con_index(ListaNotas,valor)
            print("elemento ")

            print("metodo de busqueda con index")
            def Busqueda_con_index(lista,elemento):
                if elemento in lista:
                    return (lista.index(elemento))
                else:
                    return(-1)
                                   
        case 18:
            print("[18]")       
            # conjunto de numeros
            numeros=[3,6,9,12]
            lista = list(map(Modulo1.potencia,numeros))
            print("Lista de cuadrados",lista)
        

        case 19:
            vector1= np.array([1,2,3])
            vector2= np.array([3,4,-5])
            print("\nvector1=",vector1)
            print("\nvector2=",vector2)

            matriz1=np.array( [ [1,2] , [3,4]  ])
            matriz2=np.array( [ [3,0] , [1,5]  ])
            print("\nMatriz1=\n",matriz1)
            print("\nMatriz2=\n",matriz2)

            print("OPERACIONES ARITMETICAS CON MATRICES")
            print("vector1 - 2:", vector1 -2)
            print("vector1 *1/2:",vector2 *(1/2))
            print("Matriz1 + 5:",matriz1 +5)
            print("Matriz1 *2:",matriz1 *2)
            print("raiz(matriz):", np.sqrt(matriz1))
            print("matriz1 +matriz2:",matriz1 + matriz2)
            print("matriz1 * matriz2:",matriz1 * matriz2) #multiplicacion escalar 
            print("[matriz] * [matriz2]:",np.dot(matriz1,matriz2)) #multiplicacion matricial 
        
        case 20:
            numeros = [20, 18, 13, 14, 17]
            lista_ordenada = Modulo1.ordenar_lista(numeros)

            print("Lista original:", numeros)
            print("Lista ordenada:", lista_ordenada)
            
            
        case 21:
            print("\n[21]Dado un array unidimensional hallar su media aritmética usando modulo1.py")
            #array unidimensional
            mi_array = np.array([10, 20, 30, 40, 50])

            # Usar la función de modulo1.py para calcular la media
            media_aritmetica = Modulo1.calcular_media_array(mi_array)

            print(f"El array unidimensional es: {mi_array}")
            print(f"La media aritmética del array es: {media_aritmetica}")
        
        case 22:
            print






        case 23:
            print("[23]Uso de matrices especiales")
            print("\nGenerar un array con valores automaticos")

            print("matriz1 de ceros:\n", np.zeros((2,3)))
            print("matriz1 de unos:\n",np.ones((4,2)))
            print("vector desde 0 a 1 de en 2:\n", np.arange(0,10,2))
            print("vector desde 0 a 1 separado en 5 partes:\n", np.linspace(0,1,5))
            print("definir en vector de los numeros consecutivos que aumenten de 3 en 3 desde 9 hasta 21 inclusive.",
                  "luego sumarlo con otro vector que contiene 5 elementos particionados  del rango [4 a 6]",
                  "mostrar lo 3 vectores")
            
            print("vectores des 9 a 21 de en 3:\n", np.arange(9,22,3))
            vector_a= list ((9,22,3))
            print("vectores separado en 5 elementos del rango [4 a 6]:", np.linspace(0,4,6))
            vector_b= list ((4,6,5))

            print("suma de vectores") 
            vector_a = np.arange(9,22,3)
            vector_b = np.linspace(4,6,5)

            RPTA = vector_a + vector_b

            print("resulatado final")
            print("Vector A",vector_a)
            print("Vector B", vector_b)
            print("RPTA:", RPTA)

        case 24:
            print("[]")
            vector_a= np.array([1,2,3,6,9,13,14,18,20,20])
            print("ARRAY:",vector_a)
            media=np.mean(vector_a) ;print("\nmedia=",media)
            mediana=np.median(vector_a) ; print("\nmediana=",mediana)
            #moda= np.(vector_a) ; print("\nmoda="mod)
            desv=np.std(vector_a) ; print("\nDesviacion estandar=",desv)
            percentil20=np.percentile(vector_a,20) ; print ("\nPrecentil20=",percentil20)
            varianza=np.var(vector_a) ; print("Varianza=",varianza)
            print("¿cual es la nota maxima del primer 60(%) de alunmo1?", np.percentile(vector_a,60))
            print("¿cual es la nota maxiam del primer 50(%) del alumno?",np.percentile(vector_a,50))
        
        case 25:
            print("[25]Arreglo de 100 numeros alaeatorios entre 0 y 1 y hacer operaciones")
            arreglo = np.random.rand(100)
            print( "Array original",arreglo)
            print("Array redeondeado",np.round(arreglo,2))
            vector_a = np.random.randint(1,20,10)
            print("vector_a:",vector_a)
            print("vecto1 de forma ordenda de 10 en 10:\n")

            for i,valor in enumerate(vector_a):
                print([i],"=",valor)
                if (i% 10==0):
                    print("\n")

            #Hallar la media, medaina, desviacon, moda, la nota del quinto suerior
            print("media=",np.mean(vector_a))
            print("mediana=",np.median(vector_a))
            print("desviacion estandar=",np.round(np.std(vector_a)))
            print("moda=", stat.mode(vector_a))
            print("nota media de quinto superior:", np.percentile(vector_a,80))



        case 26:
            print("[26]Matriz de 16 numeros aleatorios enteros y hacer operaciones")
            matrizAl =np.random.randint(1,10,(4,4))# guarada 16 valores en una matriz de 4x4
            print("Matriz:",matrizAl)
            print("identificar el mayor de cada columna")
            mayor_por_columna = np.amax(matrizAl, axis=0)
            print("mayor de cada columna:", mayor_por_columna)
            
        case 27:
            print("[27]Uso de matplotlib. grafico de funciones matematicas")
            print("\ grafico den funcion seno(x)")
            print("\ngrafica funcon seno\n")
            x = np.linspace(-20,20,10000)
            y = np.sin(x) #y es un array que contiene el seno delos valores de x
            plt.plot(x,y,label= 'seno', color="green")# genero la grafica internmente
            plt.title("graafico de sen(x)")
            plt.xlabel("eje x")
            plt.ylabel("eje y")
            plt.legend()
            plt.grid(True)
            plt.show()
        
        case 28:
            print("[28]uso de matplotlib. grafico de funciones valor absoluto en [-10,20]")
            x = np.linspace(-10,20,100)
            y = np.abs(x) #y es un array que contiene el seno delos valores de x
            plt.plot(x,y,label= 'seno', color="green")# genera la grafica internamente
            #plt.scatter(x,y, color='red',s=10) #puntos de la funcion, s= tamaño del punto 
            plt.title("graafico de sen(x)")
            plt.xlabel("eje x")
            plt.ylabel("eje y")
            plt.scatter(x,y, color='black',s=10)
            plt.axhline(5,color='green')
            plt.axvline(3,color='blue')
            plt.legend()
            plt.grid(True)
            plt.show()
        
        case 29:
            print("[29]uso de matplotlib. grafico de varias funciones en un solo plano")
            x = np.linspace(0, 2*np.pi,100)
            plt.plot(x, np.sin(x), label='seno')
            plt.plot(x, np.cos(x), label='coseno')
            plt.title("seno y coseno")
            plt.xlabel("Angulo [rad]")
            plt.ylabel("valor")
            plt.legend()
            plt.grid(True)
            plt.show()
        
        case 30:
            print()
            plt.plot([1,6,8,9])
            plt.show()
            
            #############
        case 31:
            print("\n[31]Grafio de seuencia de puntos")
            
            fig, ax = plt.subplots()
            
            x=np.array([0,2,4,6,8,10])
            y=np.array([1,2,4,7,8,9])
           
            ax.scatter(x,y, s=100, color='blue', alpha=0.3)
            plt.plot(x,y,label="Grafico de puntos")
            plt.show()
        
        case 32:
            print("[32]Mostrar dos figuras a la vez en dieferentes palnos ")
            x= np.linspace(0,10,100)
            y1=np.sin(x)
            y2=np.cos(x)
            
            #primera figura
            plt.figure(1)
            plt.plot(x,y1, label='seno', color='blue')
            plt.title("Figura 1 :seno")
            plt.legend()
            plt.grid(True)
            plt.show
            
            #segunda figura
            plt.figure(2)
            plt.plot(x,y2, label='coseno', color='green')
            plt.title("figura 2:coseno")
            plt.legend()
            plt.grid(True)
            plt.show()
            
        case 33:
            print("grafico de cualquier funcion matematica ")
            
           # Crear un conjunto de valores de x
            x = np.linspace(-10, 10, 400)  # desde -10 hasta 10, con 400 puntos
            y = Modulo1.f1(x)  # calcular los valores de y

            # Graficar
            plt.figure(figsize=(8, 5))
            plt.plot(x, y, label='f(x) = 2x³ - 4x² + x - 5', color='blue')
            plt.axhline(0, color='black', linewidth=0.5)  # eje X
            plt.axvline(0, color='black', linewidth=0.5)  # eje Y
            plt.title('Gráfica de una función polinómica')
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.legend()
            plt.grid(True)
            plt.show() 
                    
        case 34:
            print("[34]")
            
            #lista de datos 
            Datos =[12, 15, 13, 16, 15, 14, 14, 16, 17, 18, 16, 19, 21, 22, 21, 20, 18]
            
            #crear el histograma
            frecuencia,limites,_= plt.hist(Datos,bins=8, color='skyblue', edgecolor='black')
            plt.xticks(limites)#limite es un array que almacena los limites de os intervalos 
            #plt.yticks(frecuencias) #frecuencia es array que almacena las frecuencias 
            
            #Añadir titulos y etiquetas
            plt.title('histograma de datos')
            plt.xlabel('valor')
            plt.ylabel('frecuencia')
            plt.grid(True)
            plt.show()
            
            
        case 35:
            print("[35]uso de matplotlib. Grafico de distrbucion normal")
            # Generar datos simulados (1000 números con distribución normal)
            datos = np.random.normal(loc=0, scale=1, size=1000)

            # Crear histograma
            plt.hist(datos, bins=30, color='green', edgecolor='black')
            plt.title('Histograma de distribución normal')
            plt.xlabel('Valor')
            plt.ylabel('Frecuencia')
            plt.grid(True)
            plt.show()
            
            
        case 36:
            print("[36]uso de pandas")
            
            #crear un DataFrame
            data={'Nombre':['Ana','Luis','Maria'],
                  'Edad':[23,35,29]}
            
            df = pd.DataFrame(data)
            
            #Mostrar
            print(df)
            
            
            
            
        case _ :
            print("opcion no valida")

    #fin de match
print("salieno del menu de opciones...")
#fin de while

print("salieno del sistema...")    


