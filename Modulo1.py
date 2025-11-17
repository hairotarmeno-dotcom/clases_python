###### este modulo contiene todos lo metodos necesarios que se utilizaran en el pograma menu
#Funcion a aplicar
def potencia(numero):
    
    Rpta=numero**2
    
    return Rpta

def ordenar_lista(lista):
    """Ordena una lista de números en orden ascendente."""
    return sorted(lista)


import numpy as np # Necesario para manejar arrays y calcular la media

def imprimir(texto, lista):
  cont=1
  for i in lista:
    print(f"Lista de {texto} {cont} = {i}")
    cont=cont+1

def sumar(a, b):
  resultado = a + b
  return resultado

