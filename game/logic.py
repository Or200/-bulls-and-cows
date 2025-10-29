
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
    pass

# class GameState(TypedDict): {
#     "secret": str,
#     "length": int,
#     "max_tries": int | None,
#     "tries_used": int,
#     "unique_digits": bool,
#     "allow_leading_zero": bool,
#     "history": list[tuple[str, int, int]], # [(guess, bulls, cows), ...]
#     "seen": set[str] # ניחושים שנעשו
# }
    
def init_state(secret: str, length: int, max_tries: int | None, unique_digits: bool, allow_leading_zero: bool) -> GameState:
    pass

def apply_guess(state: GameState, guess: str) -> tuple[int, int]:
    pass

