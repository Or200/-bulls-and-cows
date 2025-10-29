from .validate import is_valid_guess

def prompt_guess(length: int) -> str:

    while True:
        guess = input("input 4 num: ")
        if is_valid_guess(guess, length):
            return guess
        print("Error - input 4 num")

def print_feedback(guess: str, bulls: int, cows: int) -> None:
    pass

def print_status(state: GameState) -> None:
    pass

def print_result(state: GameState, won: bool) -> None:
    pass

