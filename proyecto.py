#Ejemplo 1

def mostrar_lista(nodo):
  for i in 5:
    print(nodo)
    nodo = nodo.siguiente

def mostrar_backward(list):
  if list is None:return
  cabeza = list
  cola = list.siguiente
  mostrar_backward(cola)
  print(cabeza, end=" ")

class Nodo:

  def __init__( self , dato=None , siguiente=None ):
    self.dato = dato
    self.siguiente = siguiente

  def __str__( self ):
    return str( self.dato )
  

#Comprobando su funcionalidad:
nodo5 = Nodo( "Viernes" )
nodo4 = Nodo( "Jueves" ,nodo5)
nodo3 = Nodo( "Miercoles" ,nodo4)
nodo2 = Nodo( "Martes" ,nodo3)
nodo1 = Nodo( "lunes" ,nodo2)

print(nodo1)
mostrar_lista(nodo1)
mostrar_backward(nodo1)
