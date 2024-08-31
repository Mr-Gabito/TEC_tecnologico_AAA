import random

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
    option=str(input("Give us an option :D "))
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
      print(random.choice(possans))
  if askans == 5: 
    possans.clear()
    print("Loading...")
    print("All done! You can now reset it")
  if askans == 6:
    print("Come back soon!")
    break


