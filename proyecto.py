from os import system, name
import random
import time


def clear():
#El proposito de esta funcion es borrar la terminal para que se vea mas bonito el codigo al correrlo 
# Esta informacion la consegui por StackOverflow en internet
  if name == 'nt':
    _ = system('cls')

print("Hello! Welcome to the Lucky G Roulette")
print("\n")
print("Are you having trouble with a question on your quiz or exam?")
print("Do you wish to leave it all to luck?")
print("Fear not as we have you covered")
print("\n")
print("It's quite simple actually")
print("You give us the options and we'll randomly select one for you!")
matrizi=[[],[],[]]



def askusern():
#Esta funcion le pide al usuario que ponga su nombre para que pueda utilizarlo luego
  print("First, what should we call you? ")
  name=input()
  return name
print("Welcome to the show ", askusern().title(),"!")
time.sleep(2)
askans=0
possans=[]

def manyoptions():
#Esta funcion le pide al usuario cuantas opciones le gustaria agregar a la ruleta
  while True:
    numbopt=input("How many options do you wish to add? ")
#Se repite esta misma pregunta si la respuesta no es un digito por el comando de .isdigit
    if numbopt.isdigit():
       break
#.isdigit verifica si el input es numero, este comando me lo enseño un amigo
  numbopt=int(numbopt)
#Luego utilice int para cambiar el input del usuario a un numero
  for i in range(numbopt):
#Luego por el numero de opciones que quiere el usuario, pregunta las opciones y las agrega a una lista
    option=str(input("Please give us option " + str(i+1) + ": "))
    possans.append(option)



def inkans():
#Esta funcion te deja eliminar una opcion de la lista
  if len(possans)==0:
#Si la lista esta vacia le dice al usuario, dejando el mensaje por 2 segundos por el comando time
    print("Sorry, the list is empty")
#El comando time lo encontre en linea en StackOverflow
#Lo que hace es que lo que sea que imprime, le pone un timer para luego seguir con el resto del codigo
    time.sleep(2)
  else:
#Si la lista ya tiene opciones, imprime todas y las numera en orden empezando del 1
    for x,item in enumerate(possans,1):
      print(x,'. '+item, sep='')
      time.sleep(0.1)
    while True:
      rem=input("Which option would you like to remove? ")
#Con el mismo comando de .isdigit, se verifica si es digito para seguir con el codigo
#Luego se le resta 1 para que sea la posicion de la lista
      if not rem.isdigit():
          continue
      rem=int(rem)
      rem=rem-1
#Si la respuesta del usuario no existe en la lista, le pide que vuelva a poner una opcion
      if rem <0 or rem> len(possans)-1:
        print("Terribly sorry, that is not an option, try again")
      else:
#Si no, con el comando .pop elimina la opcion en la posicion de la lista
        possans.pop(rem)
        break


def showlist():
#Esta funcion imprime todas las opciones que lleva el usuario
  if len(possans)==0:
#Si la lista esta vacia entonces imprime que no hay opciones
    print("Sorry, the list is empty")
    time.sleep(1)
  else:
#Si no, imprime las opciones junto con un numero para ordenar
    clear()
    for x in range(len(possans)):
      print(x+1, '. ', possans[x] )
      time.sleep(0.1)
#Y para regresar al menu, se le pide que pique enter
    contin=str(input("Press enter to continue: "))

def times4(a):
#Esta funcion agrega 4 veces la opcion a la matriz en la posicion 0
  matrizi[0].append(a)
  matrizi[0].append(a)
  matrizi[0].append(a)
  matrizi[0].append(a)
          
def times3(a):
#Esta funcion agrega 3 veces la opcion a la matriz en la posicion 1
  matrizi[1].append(a)
  matrizi[1].append(a)
  matrizi[1].append(a)

def roulettelist():
#Esta funcion hace la matriz con multiples numeros para que se imprima de forma bonita la ruleta
#Practicamente va agregando a la matriz los numeros desde 0.001 hasta 1
  numbl=0.0
  while numbl <= 1:
    while numbl <= 0.01:
      numbl = numbl + 0.001
      times4(numbl)
    while numbl <= 0.1:
      numbl = numbl + 0.01
      times3(numbl)
    numbl = numbl + 0.1
    matrizi[2].append(numbl)

def gamble():
#Esta funcion pone a andar la ruleta, llamando la funcion de roulettelist para hacer la matriz
  roulettelist()
#Si la lista de opciones esta vacia o solo tiene una opcion, le pide al usuario que de mas opciones
  if len(possans)<2:
    print("Please give us more options")
    time.sleep(2)
#Si no, con la funcion de roulettelist
#Y con el comando de random que aprendimos en clase
#imprime opciones aleatorias con el time de todos los numeros creados en roulettelist
  elif len(possans)>=2:
    print("Alright, let's get started!")
    time.sleep(1)
    for x in matrizi[0]:
      print(random.choice(possans))
      time.sleep(x)
    for x in matrizi[1]:
      print(random.choice(possans))
      time.sleep(x)
    for x in matrizi[2]:
      print(random.choice(possans))
      time.sleep(x)
#Al final, imprime una ultima opcion aleatoria que es la respuesta, y se regresa al menu despues de 3 segundos
    print("Your answer is", random.choice(possans))
    time.sleep(3)

def listelimination():
#Esta funcion borra la lista de opciones completamente para que pueda volver a iniciar el usuario
  possans.clear()
  kill_list=["Loading.","Loading..","Loading...",
               "All done! You can now start again"]
  for x in kill_list:
    print(x)
    time.sleep(1)

while askans != 6: 
#Aqui imprime el menu de opciones para mandar a llamar la funcion necesaria
  clear()
  askans=input("""Please do choose what you'd like to do:
               1. Add an option to the roulette
               2. Remove an option from the roulette
               3. Show the options
               4. Spin the wheel! 
               5. Delete and start over
               6. Exit 
               """)
#Igual si la respuesta no es del 1-6 o un digito, se repite la pregunta
  if not askans.isdigit():
     continue
  askans=int(askans)
  

#Y finalmente, la llamada de cada funcion para cada opcion del menu
  if askans == 1:
    clear()
    manyoptions()
  if askans == 2: 
    clear()
    inkans()
  if askans == 3:
    showlist()
  if askans == 4:
    clear()
    gamble()  
  if askans == 5: 
    clear()
    listelimination()
    
print("Come back soon!")

