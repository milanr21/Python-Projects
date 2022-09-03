import random;

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors];

#Write your code below this line 👇

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if user_choice >= 3 or user_choice < 0:
  print("you typed an ivalid number, you lose!")
else:
  print(game_images[user_choice]);
  computer_choice = random.randint(0,2);
  print("Computer Chose:")

  print(game_images[computer_choice]);

  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 2 and user_choice == 0:
    print("You lose!");
  elif user_choice == 0 and computer_choice == 1:
    print("You lose!");
  elif computer_choice == 0 and user_choice == 1:
    print("You Win!");
  elif user_choice == 1 and computer_choice == 2:
    print("You Lose!");
  elif computer_choice == 1 and user_choice == 2:
    print("You Win!");
  elif user_choice == computer_choice:
    print("draw");
