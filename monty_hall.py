# the Monty Hall Problem!

import random

# two options for modes
modes = ["i", "s"]

# the doors
doors = ['1', '2', '3']

def main():
  # keep track of what is more successful over time
  stay_score = 0
  switch_score = 0
  
  print("Welcome to the Monty Hall Game! \n")
  
  mode = input("Enter 'i' for interactive or 's' for simulation: ")

  # handle error
  if mode not in modes:
    print("Invalid mode.")
    return

  # in interactive mode, you decide whether to play again
  # by pressing 'y'
  elif mode == "i":
    print("\n You are now in interactive mode! \n")
    again = 'y'
    while again == 'y':
      switch_score, stay_score = interactive(switch_score, stay_score)
      print('Switch score is: ' + str(switch_score))
      print('Stay score is: ' + str(stay_score))
      again = input("\nPlay again? (y/n): ")

  # in simulation mode, you decide how many times (i) to run the simulation
  else:
    # default 
    i = 100
    while True: 
      try:
        i = int(input('Run how many times? '))
        break
      except ValueError:
        print('Invalid input.')
        continue
    j = 0
    while j < i:
      switch_score, stay_score = simulation(switch_score, stay_score)
      j += 1
    print('\n Switch score is: ' + str(switch_score))
    print('Stay score is: ' + str(stay_score))
  print("Thanks for playing!")
  return 

def interactive(switch_score, stay_score):
  prizes = ['brand new flying car', 'brand new refrigerator/microwave combo', 
            'vacation to the Bahamas', 'home makeover', 
            'super computer that can store over 200 megabytes', 
            'new 20 x 30 ft TV', 'pair of 3D glasses for real-life']

  str_prize = random.choice(prizes)

  print("\n AUDIENCE: Let's Make A Deal!!!!")
  print("\n MONTY HALL (THE HOST):")
  print("You are faced with three doors, identical in appearance.\n" +  
  "Behind two are goats. Behind one is a " + str_prize + "!" +
  "\nYou will have the opportunity now to choose one door of the three." +
  "\nThen, we will reveal what is behind one of the other two doors. " +
  "\nYou will be given the chance to switch doors, or stay with your original choice."
  + "\nChoose wisely, and good luck!")
  print("\n (APPLAUSE)")
  # the prize
  prize = random.choice(doors)

  # door choice by user
  door = input("\n Enter the door you want to pick (1, 2, or 3): ")

  # handle error case
  while door not in doors:
    door = input("\n MONTY: You must pick one of the three doors (1, 2, 3): ")

  # open the first door
  door_opened = door_open(door, prize)

  print("\n Door " + str(door_opened) + " is opened... ")
  print("\n MONTY: It's a goat!")
  print("\n GOAT: Maaa-aaa!")
  print("\n MONTY: And you can't take that home!")
  
  # chance to switch or stay 
  move = input("\n Do you want to switch doors? (y/n): ")

  # handle switch case
  if move == 'y':
    door = switch(door, door_opened)

  print("\n MONTY: You chose door " + str(door) + "! Let's take a look... ")
  
  # check if winner, update corresponding scores
  if door == prize:
    print("\n Congratulations, you just won a " + str_prize + "!!!" + 
          " Thanks for playing Let's Make a Deal!")
    print("\n (APPLAUSE) \n")
    if move == 'y':
      switch_score += 1
    else:
      stay_score += 1
  else:
    print("\n And... it's a goat. Better luck next time!")
    print("\n AUDIENCE: AWWWW \n")

  return switch_score, stay_score
  
def door_open(door, prize):
  for x in doors:
    if x != door and x != prize:
      return x
  return 0
  
def switch(door, door_opened):
  return door_open(door, door_opened)

def simulation(switch_score, stay_score):
  moves = ['switch', 'stay']
  prize = random.choice(doors)
  door = random.choice(doors)
  move = random.choice(moves)
  
  if move == 'switch':
    door = switch(door, door_open(door, prize))
    if door == prize:
      switch_score += 1
  
  elif door == prize and move == 'stay':
    stay_score += 1
  
  return switch_score, stay_score

main()
