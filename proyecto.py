import random
import time


print("Hello! Welcome to the Lucky G Roulette")
print("\n")
print("Are you having trouble with a question on your quiz or exam?")
print("Do you wish to leave it all to luck?")
print("Fear not as we have you covered")
print("\n")
print("It's quite simple actually")
print("You give us the options and we'll randomly select one for you!")
lista=[]
def askusern():
  print("First, what should we call you? ")
  name=input()
  return name
print("Welcome to the show ", askusern().title(),"!")
askans=0
possans=[]
while askans != 6: 

  askans=int(input("""First of all, please do choose what you'd like to do:
               1. Add an option to the roulette
               2. Remove an option from the roulette
               3. Show the options
               4. Spin the wheel! 
               5. Delete and start over
               6. Exit 
               """))
  if askans == 1:
    numbopt=int(input("How many options do you wish to add? "))
    for i in range(numbopt):
      option=str(input("Please give us option " + str(i+1) + ": "))
      possans.append(option)


      #FIND HOW TO MAKE THE QUESTION ONLY BE A NUMBER AND REPEAT IF NOT


  if askans == 2: 
    for x,item in enumerate(possans,0):
      print(x,'. '+item, sep='')


    #CHANGE THE WHILE TRUE TO AN ACTUAL CONDITION


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
    else:
      for x in range(len(possans)):
        print(x, '. ', possans[x] )
  if askans == 4:
    if len(possans)<2:
      print("Please give us more options")
    if len(possans)>2:
      print("Alright, let's get started!")
      time.sleep(1)
      def times3(a):
        lista.append(a)
        lista.append(a)
        lista.append(a)
      def times2(a):
        lista.append(a)
        lista.append(a)
      def roulettelist(listl):
        numbl=0.0
        while numbl <= 1:
          while numbl <= 0.01:
            numbl = numbl + 0.001
            times3(numbl)
          while numbl <= 0.1:
            numbl = numbl + 0.01
            times2(numbl)
          numbl = numbl + 0.1
          listl.append(numbl)
      roulettelist(lista)
      for x in lista:
        print(random.choice(possans))
        time.sleep(x)
      print("Your answer is", random.choice(possans))
  if askans == 5: 
    possans.clear()
    kill_list=["Loading.","Loading..","Loading...","All done! You can now start again"]
    for x in kill_list:
      print(x)
      time.sleep(1)
print("Come back soon!")

#FIND HOW TO CLEAR THE TERMINAL FOR EACH OPTION
