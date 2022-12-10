import random

options = ['rock', 'paper', 'scissor']
computer_score = int(0)
user_score = int(0)
count = int(0)
while count < 5:
    user_choice = input("Enter rock, paper or scissor\n").lower()
    computer = random.choice(options)

    if user_choice == computer:
        print("option chosen by computer is", computer )
        print("so it's a tie ")

    elif user_choice == 'rock':
        if user_choice == 'paper':
            print("option chosen by computer is",computer)
            print("so you lost.")
            computer_score += 1
        else:
            
            print("option chosen by computer is",computer) 
            print("so you won.")
            user_score += 1

    elif user_choice == 'paper':
        if computer == 'scissor':
          print("option chosen by computer is",computer) 
          print("so you lost.")
          computer_score += 1
        else:
            print("option chosen by computer is",computer)
            print("so you won.")
            user_score += 1
            
    elif user_choice == 'scissor':
        if computer == 'rock':
            print("option chosen by computer is",computer)
            print("so you lost.")
            computer_score += 1
        else:
            print("option chosen by computer is",computer)
            print("so you won.")
            user_score += 1
    else:
            print("Error ")
            continue
    count = count+1 
   
if user_score > computer_score:
          print("computer_score:",computer_score)
          print("Your score",user_score)
          ("so you won. ")
    
elif user_score < computer_score:
          print("computer_score:",computer_score)
          print("Your score",user_score)
          print("so you lost. ")
else:
        print("computer_score=user_score score is:",computer_score)
        print("so it's a tie. ")
 