import random


def play_rock_paper_scissors():
    """
    This function runs a complete game of Rock-Paper-Scissors with scoring.
    """
    user_score = 0
    computer_score = 0
    choices = ['rock', 'paper', 'scissors']

    print("--- Welcome to Rock, Paper, Scissors! 🗿📄✂️ ---")

    # --- Main Game Loop ---
    while True:
        # 1. User Input
        user_choice = input("\nChoose rock, paper, or scissors: ").lower()

        # Validate user's input
        if user_choice not in choices:
            print("❌ Invalid choice. Please pick rock, paper, or scissors.")
            continue

        # 2. Computer Selection
        computer_choice = random.choice(choices)

        # 4. Display Result (Choices)
        print(f"\n➡️ You chose: {user_choice}")
        print(f"🤖 Computer chose: {computer_choice}\n")

        # 3. Game Logic
        if user_choice == computer_choice:
            print("It's a tie! 🤝")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                (user_choice == 'scissors' and computer_choice == 'paper') or \
                (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round! 🎉")
            user_score += 1
        else:
            print("The computer wins this round! 🤖")
            computer_score += 1

        # 5. Score Tracking
        print("---------------------------------")
        print(f"Score -> You: {user_score} | Computer: {computer_score}")
        print("---------------------------------")

        # 6. Play Again
        play_again = input("\nPlay another round? (y/n): ").lower()
        if play_again != 'y':
            break

    # --- End of Game ---
    print("\nThanks for playing! Here is the final score:")
    print(f"🏆 Final Score -> You: {user_score} | Computer: {computer_score} 🏆")


# --- Start the game ---
if __name__ == "__main__":
    play_rock_paper_scissors()
