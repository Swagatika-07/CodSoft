import random

def getUser():
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors): ")
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid input. Please try again.")

def getComputer():
    return random.choice(['rock', 'paper', 'scissors'])

def winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def display_result(user, computer, result):
    print("\nYou chose:",user)
    print("Computer chose:", computer)
    print(result)

def play_again():
    while True:
        again = input("Do you want to play again? (y or n): ").lower()
        if again in ['y', 'n']:
            return again =='y'
        else:
            print("Invalid input. Please try again.")     

def main():
    user_score = 0
    computer_score = 0

    print("Rock-Paper-Scissors Game!")


    while True:
        user = getUser()
        computer = getComputer()
        result = winner(user, computer)
        display_result(user, computer, result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        print(f"Score: You {user_score} , Computer {computer_score}")

        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()