
# Number Guessing Game

This is a simple number guessing game implemented in Python. The program selects a random number within a user-defined range, and the player has a limited number of attempts to guess the correct number. The game provides hints after each guess to help the player.

## Features

- **User-Defined Range**: The player sets the minimum and maximum range for the random number.
- **Limited Attempts**: The player has 5 attempts to guess the correct number.
- **Hints Provided**: After each incorrect guess, hints are provided to indicate whether the guess was too high or too low.
- **Even/Odd Hint**: If the player reaches the last attempt, a hint is given indicating whether the number is even or odd.
- **First Try Bonus**: If the player guesses the number correctly on the first attempt, they receive a bonus.

## How to Play

1. **Set the Range**: Enter the minimum and maximum values for the range in which the random number will be selected.
2. **Start the Game**: The game will prompt you to press ENTER to start.
3. **Make Guesses**: You have 5 attempts to guess the number. Enter your guess and receive hints if your guess is incorrect.
4. **Win or Lose**: If you guess the number correctly within the attempts, you win the amount. If you guess it correctly on the first try, you win an additional bonus. If you don't guess the number within the attempts, you lose, and the correct number is revealed.

## How It Works

1. **Initialization**: The program initializes the range and attempts, then generates a random number within the range.
2. **Starting the Game**: The game prompts the player to start and explains the rules.
3. **Game Loop**: The player makes guesses, and the game provides feedback after each guess. If the guess is correct, the player wins. If the guess is incorrect, the game gives hints and reduces the number of attempts.
4. **Ending the Game**: After all attempts are used or the correct number is guessed, the game ends and displays the result.

## Installation

1. **Clone the Repository**: Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/Riya-2603/number-guessing-game.git
   ```
3. **Navigate to the Project Directory**:
   ```bash
   cd number-guessing-game
   ```
4. **Run the Game**:
   ```bash
   python game.py
   ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- Python community for the libraries and support.
