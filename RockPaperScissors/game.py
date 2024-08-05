import random
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, winner):
    print(Fore.CYAN + f"\nYou chose: {user_choice.capitalize()}")
    print(Fore.CYAN + f"Computer chose: {computer_choice.capitalize()}")

    if winner == 'tie':
        print(Fore.YELLOW + "It's a tie!")
    elif winner == 'user':
        print(Fore.GREEN + "You win!")
    else:
        print(Fore.RED + "Computer wins!")

def main():
    leaderboard = []

    while True:
        user_name = input("Enter your name: ").strip()
        if not user_name:
            print(Fore.RED + "Name cannot be empty. Please try again.")
            continue
        
        print(Fore.CYAN + "\n===== Rock-Paper-Scissors Game =====" + Style.RESET_ALL)
        print(Fore.CYAN + "Choose the number of rounds: " + Style.RESET_ALL)
        print(Fore.CYAN + "1. 1 round" + Style.RESET_ALL)
        print(Fore.CYAN + "2. Best of 3 rounds" + Style.RESET_ALL)
        print(Fore.CYAN + "3. Best of 5 rounds" + Style.RESET_ALL)

        rounds_choice = input("Enter your choice (1/2/3): ").strip()
        if rounds_choice == '1':
            total_rounds = 1
        elif rounds_choice == '2':
            total_rounds = 3
        elif rounds_choice == '3':
            total_rounds = 5
        else:
            print(Fore.RED + "Invalid choice. Please try again.")
            continue

        user_score = 0
        computer_score = 0

        for round_num in range(total_rounds):
            print(Fore.CYAN + f"\nRound {round_num + 1}/{total_rounds}" + Style.RESET_ALL)
            print(Fore.CYAN + "1. Rock" + Style.RESET_ALL)
            print(Fore.CYAN + "2. Paper" + Style.RESET_ALL)
            print(Fore.CYAN + "3. Scissors" + Style.RESET_ALL)

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                user_choice = 'rock'
            elif choice == '2':
                user_choice = 'paper'
            elif choice == '3':
                user_choice = 'scissors'
            else:
                print(Fore.RED + "Invalid choice. Please try again.")
                continue

            computer_choice = get_computer_choice()
            winner = determine_winner(user_choice, computer_choice)
            display_result(user_choice, computer_choice, winner)

            if winner == 'user':
                user_score += 1
            elif winner == 'computer':
                computer_score += 1

            print(Fore.CYAN + f"\nScore: You {user_score} - {computer_score} Computer" + Style.RESET_ALL)

        if user_score > computer_score:
            match_result = Fore.GREEN + f"{user_name} wins the match!"
        elif user_score < computer_score:
            match_result = Fore.RED + "Computer wins the match!"
        else:
            match_result = Fore.YELLOW + "The match is a tie!"

        print(match_result + Style.RESET_ALL)
        leaderboard.append((user_name, user_score, computer_score))

        print(Fore.CYAN + "\nLeaderboard:" + Style.RESET_ALL)
        for entry in leaderboard:
            print(Fore.CYAN + f"{entry[0]}: {entry[1]} - {entry[2]}" + Style.RESET_ALL)

        play_again = input("Do you want to play another match? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print(Fore.GREEN + "Exiting the game. Thanks for playing!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()
