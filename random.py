import random
NumeroEleg=0
nummax=0
dificultad=0
intentos=0
print("seleccione la dificultad (facil=1 o dificil=2)")
dificultad=int(input())

if dificultad==1:
    intentos=6
    Numero=random.randint(1,20)
    nummax=20
if dificultad==2:
    intentos=7
    Numero=random.randint(1,200)
    nummax=200
    

print("adivina un numero del 1 al", nummax)
print("tienes", intentos,"intentos")

Numeroeleg=int(input())


while (Numeroeleg!=Numero):
    intentos=intentos-1
    if intentos==0:
        break
    else:
        if Numeroeleg>Numero:
            print("incorrecto, seleccione un numero menor")
            Numeroeleg=int(input())
        else:
            if Numeroeleg<Numero:
                print("incorrecto, seleccione un numero mayor")
                Numeroeleg=int(input())

if Numeroeleg!=Numero:
    print("perdiste, se te acabaron los intentos, el numero era", Numero)
else:
    print("felicidades, el numero era", Numero)