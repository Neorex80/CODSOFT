---

# Rock-Paper-Scissors Game

This is a command-line Rock-Paper-Scissors game written in Python. It allows users to play against the computer, choose the number of rounds, and keep track of scores with a leaderboard.

## Features

- **User Input**: Prompt the user to choose rock, paper, or scissors.
- **Computer Selection**: Generate a random choice for the computer.
- **Game Logic**: Determine the winner based on the choices.
- **Display Result**: Show the user's choice, computer's choice, and the result.
- **Score Tracking**: Keep track of scores for multiple rounds.
- **Leaderboard**: Display a leaderboard with players' scores.
- **Play Again**: Ask the user if they want to play another match.

## Prerequisites

- Python 3.x
- `colorama` library for colored terminal output

You can install the `colorama` library using pip:

```bash
pip install colorama
```

## Usage

1. Clone the repository or download the `rock_paper_scissors.py` file.
2. Open your terminal and navigate to the directory containing `rock_paper_scissors.py`.
3. Run the application:

```bash
python rock_paper_scissors.py
```

## How to Play

1. Enter your name when prompted.
2. Choose the number of rounds (1, 3, or 5).
3. Select rock, paper, or scissors for each round.
4. View the result and scores after each round.
5. Check the leaderboard at the end of the match.
6. Choose whether to play another match.

## Example

```
Enter your name: John

===== Rock-Paper-Scissors Game =====
Choose the number of rounds: 
1. 1 round
2. Best of 3 rounds
3. Best of 5 rounds
Enter your choice (1/2/3): 2

Round 1/3
1. Rock
2. Paper
3. Scissors
Enter your choice: 1

You chose: Rock
Computer chose: Scissors
You win!

Score: You 1 - 0 Computer

Round 2/3
1. Rock
2. Paper
3. Scissors
Enter your choice: 2

You chose: Paper
Computer chose: Rock
You win!

Score: You 2 - 0 Computer

Round 3/3
1. Rock
2. Paper
3. Scissors
Enter your choice: 3

You chose: Scissors
Computer chose: Rock
Computer wins!

Score: You 2 - 1 Computer

John wins the match!

Leaderboard:
John: 2 - 1
Do you want to play another match? (yes/no): no
Exiting the game. Thanks for playing!
```

## License

This project is licensed under the MIT License.

---
