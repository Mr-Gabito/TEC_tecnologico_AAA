from os import system, name
import random
import time


def clear():
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
  print("First, what should we call you? ")
  name=input()
  return name
print("Welcome to the show ", askusern().title(),"!")
time.sleep(2)
askans=0
possans=[]

def manyoptions():
  while True:
    numbopt=input("How many options do you wish to add? ")
    if numbopt.isdigit():
       break
  numbopt=int(numbopt)
  for i in range(numbopt):
    option=str(input("Please give us option " + str(i+1) + ": "))
    possans.append(option)



def inkans():
    if len(possans)==0:
      print("Sorry, the list is empty")
      time.sleep(2)
    else:
      for x,item in enumerate(possans,1):
        print(x,'. '+item, sep='')
        time.sleep(0.1)
      while True:
        rem=input("Which option would you like to remove? ")
        if not rem.isdigit():
           continue
        rem=int(rem)
        rem=rem-1
        if rem <0 or rem> len(possans)-1:
          print("Terribly sorry, that is not an option, try again")
        else:
          possans.pop(rem)
          break


def showlist():
    if len(possans)==0:
      print("Sorry, the list is empty")
      time.sleep(1)
    else:
      clear()
      for x in range(len(possans)):
        print(x+1, '. ', possans[x] )
        time.sleep(0.1)
      contin=str(input("Press enter to continue: "))

def times4(a):
    matrizi[0].append(a)
    matrizi[0].append(a)
    matrizi[0].append(a)
    matrizi[0].append(a)
          
def times3(a):
    matrizi[1].append(a)
    matrizi[1].append(a)
    matrizi[1].append(a)

def roulettelist():
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
    roulettelist()

    if len(possans)<2:
      print("Please give us more options")
      time.sleep(2)
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
      print("Your answer is", random.choice(possans))
      time.sleep(3)

def listelimination():
    possans.clear()
    kill_list=["Loading.","Loading..","Loading...",
               "All done! You can now start again"]
    for x in kill_list:
      print(x)
      time.sleep(1)

while askans != 6: 
  clear()
  askans=input("""Please do choose what you'd like to do:
               1. Add an option to the roulette
               2. Remove an option from the roulette
               3. Show the options
               4. Spin the wheel! 
               5. Delete and start over
               6. Exit 
               """)
  if not askans.isdigit():
     continue
  askans=int(askans)
  
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

