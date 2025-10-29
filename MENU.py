#MENU de opciones para uso de listas, tuplas, diccionarios
#apliacione a diversos ejercicios

#definiiocn de variables
op = 0 #op(designa la opcion elegida en el menu)
###variables para caso 1
pA=0; pB=0; pC=0; pT=0; total=0; k=0; A=0; B=0; C=0
###variables para caso 2
a=0; b=0 ;  c=0  ; D=0; x1Real=0; x2Real=0  ;x1Imag=0j ; x2Imag=0j

###varaibles para caso 3


while(op!=40):

    print("\n\nMENU DE OPCIONES")
    print("[1]PROBLEMA DE PRORRATEO DE GASTOS")
    print("[2]SOLUCION DE ECUACION CUADRATICA")
    print("[3] USO DE LISTAS")
    print("[4]USO DE TUPLAS")
    print("[5]USO DE DICCIONARIO")
    print("[6]")
    print("[7]")
    print("[8]")
    print("[9]")
    print("[10]")
    print("[11]")
    print("[12]")
    print("[13]")
    print("[14]")
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
            
            
            

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

      
            
        case _ :
            print("opcion no valida")

    #fin de match
print("salieno del menu de opciones...")
#fin de while

print("salieno del sistema...")    


