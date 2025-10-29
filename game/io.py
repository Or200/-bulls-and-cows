from .validate import is_valid_guess

def prompt_guess(length: int) -> str:

    while True:
        guess = input("input 4 num: ")
        if is_valid_guess(guess, length):
            return guess
        print("Error - input 4 num")

def print_feedback(guess: str, bulls: int, cows: int) -> None:
    print(f"guess: {guess}.  bulls: {bulls}.  cows: {cows} ")

def print_status(state: dict) -> None:
    pass

def print_result(state: dict, won: bool) -> None:
    pass

