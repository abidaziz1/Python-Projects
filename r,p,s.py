import random
def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'paper' and computer_choice == 'rock') or \
        (user_choice == 'scissors' and computer_choice == 'paper'):
            return 'user'
    else:
        return 'computer'

def display_round_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win this round!")
    else:
        print("Computer wins this round!")

def display_final_scores(user_score, computer_score):
    print("\nFinal Scores:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations, you won the game!")
    elif user_score < computer_score:
        print("Sorry, you lost the game.")
    else:
        print("It's a tie game!")

def play_rock_paper_scissors():
    user_score = 0
    computer_score = 0
    rounds = int(input("Enter the number of rounds you want to play: "))
    for _ in range(rounds):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_round_result(user_choice, computer_choice, winner)
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1
    display_final_scores(user_score, computer_score)

if __name__=="__main__":
    print("Welcome to the Rock-Paper-Scissors Game!")
    while True:
        play_rock_paper_scissors()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break