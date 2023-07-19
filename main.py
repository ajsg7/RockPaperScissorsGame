#print('Hello, world!')
#Alan
#takes in 5 inputs and displays sum and average
import random
import check_input

def main():
  budget = 100
  One = 1
  Two = 2
  Three = 3
  #bet = int(input("How much you wanna bet?" ))
  print("-Three card Monte-\nFind the queen to double your bet!")
  print("\n\nYou have $" + str(budget))  
  answer = True
  while( budget > 0 and answer ):
    bet = check_input.get_int_range("How much you wanna bet? ",1, budget)
    print("+-----+  +-----+  +-----+")
    print("|     |  |     |  |     |")
    print("|  1  |  |  2  |  |  3  |")
    print("|     |  |     |  |     |")
    print("+-----+  +-----+  +-----+")    
    Queen = random.randint(1, 3)
    if budget > 0:
      Guess = check_input.get_int_range("Find the queen: ", 1, 3)
    if Guess == Queen:
      budget += (2*bet)
      print("You got lucky this time")
      print("You have $" + str(budget))
    elif Guess != Queen:
      budget -= bet
      print("Sorry... you lose.")
      print("You have $" + str(budget))
    if Queen == One:
      print("+-----+  +-----+  +-----+")
      print("|     |  |     |  |     |")
      print("|  Q  |  |  K  |  |  K  |")
      print("|     |  |     |  |     |")
      print("+-----+  +-----+  +-----+")
    if Queen == Two:
      print("+-----+  +-----+  +-----+")
      print("|     |  |     |  |     |")
      print("|  K  |  |  Q  |  |  K  |")
      print("|     |  |     |  |     |")
      print("+-----+  +-----+  +-----+")
    if Queen == Three:
      print("+-----+  +-----+  +-----+")
      print("|     |  |     |  |     |")
      print("|  K  |  |  K  |  |  Q  |")
      print("|     |  |     |  |     |")
      print("+-----+  +-----+  +-----+")
    if(budget > 0):
      answer = check_input.get_yes_no("Play again? (Y/N): ")
  if budget <= 0:
      print("You're out of money!")
main()