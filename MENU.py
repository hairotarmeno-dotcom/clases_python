#MENU de opciones para uso de listas, tuplas, diccionarios
#apliacione a diversos ejercicios
#definicion de METODOS (funcione o procedimentos)
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
        
        
        
        
        case _ :
            print("opcion no valida")

    #fin de match
print("salieno del menu de opciones...")
#fin de while

print("salieno del sistema...")    


