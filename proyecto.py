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

def askusern():
  print("First, what should we call you? ")
  name=input()
  return name
print("Welcome to the show ", askusern().title(),"!")

possans=[]
while True: 

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
  if askans == 2: 
    for x,item in enumerate(possans,0):
      print(x,'. '+item, sep='')
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
      #CAN BE IMPROVED WITH DEF FUNCTION
      for l in [0.001, 0.001, 0.001,
          0.002, 0.002, 0.002,
          0.003, 0.003, 0.003,
          0.004, 0.004, 0.004,
          0.005, 0.005, 0.005,
          0.006, 0.006, 0.006,
          0.007, 0.007, 0.007,
          0.008, 0.008, 0.008,
          0.009, 0.009, 0.009,
          0.01, 0.01, 0.01,
          0.02, 0.02, 0.02,
          0.03, 0.03, 0.03,
          0.04, 0.04, 0.04,
          0.05, 0.05, 0.05,
          0.06, 0.06, 0.06,
          0.07, 0.07, 0.07,
          0.08, 0.08, 0.08,
          0.09, 0.09, 0.09,
          0.1, 0.1, 0.1,
          0.2, 0.2, 0.2,
          0.3, 0.3,
          0.4, 0.4,
          0.5, 0.5,
          0.6, 0.6,
          0.7,
          0.8,
          0.9,
          1]:
        print(random.choice(possans))
        time.sleep(l)
      print("Your answer is ", random.choice(possans))
  if askans == 5: 
    possans.clear()
    kill_list=["Loading.","Loading..","Loading...","All done! You can now start again"]
    for x in kill_list:
      print(x)
      time.sleep(1)
  if askans == 6:
    print("Come back soon!")
    break


