import random

# Print the rules of the game
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

# Start an infinite loop to allow continuous play
while True:

    # Prompt user for their choice
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    # Take input from the user
    choice = int(input("Enter your choice : "))

    # Ensure the user enters a valid choice
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please '))

    # Assign choice_name based on user's choice
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    # Display user's choice
    print("Your choice is :", choice_name)

    # Generate computer's choice randomly
    comp_choice = random.randint(1, 3)

    # Ensure computer's choice is not the same as user's choice to avoid a draw
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    # Assign comp_choice_name based on computer's choice
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    
    # Display computer's choice
    print("Computer's choice is :", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    # Determine the result of the game
    if choice == comp_choice:
        print('It is a draw\n', end="")
        result = "Draw"

    # Condition for when Paper wins
    if (choice == 1 and comp_choice == 2):
        print('Paper wins\n', end="")
        result = 'Paper'
    elif (choice == 2 and comp_choice == 1):
        print('Paper wins\n', end="")
        result = 'Paper'

    # Condition for when Rock wins
    if (choice == 1 and comp_choice == 3):
        print('Rock wins\n', end="")
        result = 'Rock'
    elif (choice == 3 and comp_choice == 1):
        print('Rock wins\n', end="")
        result = 'Rock'

    # Condition for when Scissors wins
    if (choice == 2 and comp_choice == 3):
        print('Scissors wins\n', end="")
        result = 'Scissors'
    elif (choice == 3 and comp_choice == 2):
        print('Scissors wins\n', end="")
        result = 'Scissors'

    # Display the result of the game
    if result == 'Draw':
        print("It's a tie\n")
    elif result == choice_name:
        print("User wins\n")
    else:
        print("\nComputer wins\n")

    # Ask the user if they want to play again
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    
    # Exit the loop if the user chooses 'n'
    if ans == 'n':
        break

# Thank the user for playing
print("Thank you for playing!")
