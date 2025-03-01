"""
This is a Wordle inspired program.
"""

__author__: str = "730578258"


def contains_char(word: str, character: str) -> bool:
    """determines if a single character is found in a given word"""
    assert len(character) == 1, f"len('{character}') is not 1"
    x: int = 0
    while x < len(word):
        if word[x] == character:
            return True
        x += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """returns a string of the emoji with color that
    codes the correctness associated with guess;
    each operator should incrementally build the string
    character by character to create colored positions"""
    assert len(guess) == len(secret), "Guess must be the same length as secret"

    # this ensures that the length of guess matches the length of secret
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    result: str = ""
    x: int = 0
    while x < len(guess):
        if guess[x] == secret[x]:
            # correct letter and position outputs a green box
            result += GREEN_BOX
        elif contains_char(secret, guess[x]):
            # correct letter but wrong position outputs a yellow box
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
            # letter isn't in the secret word outputs a white box
        x += 1
    return result


def input_guess(expected_length: int) -> str:
    """ask the player to guess the expected length of the word"""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")

    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # need to establish state variables
    total_turns: int = 6
    current_turn: int = 1
    win: bool = False

    # need to create a loop to start the game
    while current_turn <= total_turns and not win:
        print(f"=== Turn {current_turn}/{total_turns} ===")  # print the turn number

        # evaluating the player's guess:
        player_guess: str = input_guess(len(secret))
        result: str = emojified(player_guess, secret)
        print(result)

        # checking to see if the player won
        if player_guess == secret:
            win = True
        else:
            current_turn += 1
    # end of the game message part
    if win:
        print(f"You won in {current_turn}/{total_turns} turns!")
    else:
        print(f"X/{total_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
