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
while askans != 6: 
  clear()
  askans=int(input("""Please do choose what you'd like to do:
               1. Add an option to the roulette
               2. Remove an option from the roulette
               3. Show the options
               4. Spin the wheel! 
               5. Delete and start over
               6. Exit 
               """))
  if askans == 1:
    clear()
    numbopt=int(input("How many options do you wish to add? "))
    for i in range(numbopt):
      option=str(input("Please give us option " + str(i+1) + ": "))
      possans.append(option)
  if askans == 2: 
    clear()
    if len(possans)==0:
      print("Sorry, the list is empty")
      time.sleep(2)
    else:
      for x,item in enumerate(possans,0):
        print(x,'. '+item, sep='')
        time.sleep(0.1)
      while True:
        rem=int(input("Which option would you like to remove? "))
        if rem <0 or rem> len(possans)-1:
          print("Terribly sorry, that is not an option, try again")
        else:
          possans.pop(rem)
          break
  if askans == 3:
    if len(possans)==0:
      print("Sorry, the list is empty")
      time.sleep(1)
    else:
      clear()
      for x in range(len(possans)):
        print(x, '. ', possans[x] )
        time.sleep(0.1)
      cont=str(input("Press enter to continue: "))
  if askans == 4:
    clear()
    if len(possans)<2:
      print("Please give us more options")
      time.sleep(2)
    elif len(possans)>=2:
      print("Alright, let's get started!")
      time.sleep(1)
      def times3(a):
          matrizi[0].append(a)
          matrizi[0].append(a)
          matrizi[0].append(a)
          matrizi[0].append(a)
      def times2(a):
          matrizi[1].append(a)
          matrizi[1].append(a)
          matrizi[1].append(a)
      def roulettelist():
          numbl=0.0
          while numbl <= 1:
              while numbl <= 0.01:
                  numbl = numbl + 0.001
                  times3(numbl)
              while numbl <= 0.1:
                  numbl = numbl + 0.01
                  times2(numbl)
              numbl = numbl + 0.1
              matrizi[2].append(numbl)
      roulettelist()
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
  if askans == 5: 
    clear()
    possans.clear()
    kill_list=["Loading.","Loading..","Loading...","All done! You can now start again"]
    for x in kill_list:
      print(x)
      time.sleep(1)
print("Come back soon!")

