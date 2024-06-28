import random

# Import the game data
from HLgame_data import data

# Import the ASCII art to display
from HLart import logo, vs

# IDEs like Replit have their own "clear" functions to clear the output console:
from replit import clear

def assign():
    """Randomly select an option from the data."""
    return random.choice(data)

def compare(p1, p2, guess):
    """Compare the follower counts of p1 and p2."""
    if (p1['follower_count'] > p2['follower_count'] and guess == p1['name'].lower()) or \
       (p2['follower_count'] > p1['follower_count'] and guess == p2['name'].lower()):
        return True
    return False

def play_higher_lower():
    playing_game = True
    while playing_game:
        score = 0
        still_guessing = True
        person1 = assign()
        person2 = assign()
        while still_guessing:
            clear()
            print(logo)
            # Ensure person1 and person2 are not the same
            while person1 == person2:
                person2 = assign()
            
            print(f"Name: {person1['name']}, Desc: {person1['description']}, Followers: {person1['follower_count']}")
            print(vs)
            print(f"Name: {person2['name']}, Desc: {person2['description']}, Followers: {person2['follower_count']}")
            print("----------------------------------------------")
            print(f"Your current score is: {score}")
            print("----------------------------------------------")
            guess = input("Enter name of person with Higher Followers: ").lower()
            
            if guess not in [person1['name'].lower(), person2['name'].lower()]:
                print("Invalid input. Please enter a valid name.")
                continue
            
            if compare(person1, person2, guess):
                score += 1
                person1 = person2
                person2 = assign()
            else:
                still_guessing = False
                print("You lose!")
        
        play_again = input("Want to Play Again? (y/n): ").lower()
        if play_again == 'y':
            continue
        else:
            playing_game = False
            clear()
            print("Bye!")

if __name__ == '__main__':
    play_higher_lower()
