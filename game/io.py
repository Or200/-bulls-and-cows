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
    print(f"your try: {state["tries_used"]}.  your history: {state["history"]}")

def print_result(state: dict) -> None:
    print(f"The number is: {state["secret"]} your try: {state["tries_used"]} your history: {state["history"]}")
