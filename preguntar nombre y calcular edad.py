nombre=""
AñoNac=0
Añoactual=0
edad=0

print("ingrese su nombre de usuario")
nombre=input()

print("ingrese su año de nacimiento")
AñoNac=int(input())

print("ingrese el año en el que estamos")
Añoactual=int(input())

edad=Añoactual-AñoNac

print("hola", nombre, "usted tiene",edad,"años")