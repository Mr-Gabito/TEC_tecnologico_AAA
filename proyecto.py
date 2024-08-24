import random

print("Hello! Welcome to the Lucky G Roulette")
print("\n")
print("Are you having trouble with a question on your quiz or exam?")
print("Do you wish to leave it all to luck?")
print("Fear not as we have you covered")
print("\n")
print("It's quite simple actually")
print("You give us the options and we'll randomly select one for you!")



#Possible answers attempt
possans=[]
askans=input("Give us the options: ")
possans.append(askans)
print(f'Alright we have the options: {possans}')

#Have to figure out how to make a loop, to ask the same question

final=input("Are those all the options? Yes or no? ")
if final==("no"):
  print("Ok then...")
elif final==("yes"):
  print("Alright, let's get started!")
  print(random.choice(possans))
else:
  print("Please answer with yes or no")

#Also need to figure out how to continue the question if the answer is not yes or no

if len(possans)<2:
  print("Please give us more options")

#Need to know where to put this part on the code

