
def score_guess(secret: str, guess: str) -> tuple[int, int]:
    bulls = 0
    cows = 0

    for i in guess:
        if i in secret:
            cows += 1

    for i in range(len(guess)):
        if guess[i] in secret and guess[i] == secret[i]:
            bulls += 1
    
    cows = cows - bulls

    print(bulls, cows)
    return bulls, cows 


def is_won(bulls: int, length: int) -> bool:
    return bulls == length

    
def init_state(secret: str, length: int, max_tries: int | None, unique_digits: bool, allow_leading_zero: bool, seen: dict) -> dict:
    GameState = {
    "secret": secret,
    "length": length,
    "max_tries": max_tries,
    "tries_used": 0,
    "unique_digits": unique_digits,
    "allow_leading_zero": allow_leading_zero,
    "history": [],
    "seen": seen
}


def apply_guess(state: dict, guess: str) -> tuple[int, int]:
    pass

