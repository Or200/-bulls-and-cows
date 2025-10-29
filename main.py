from game.validate import is_new_guess

def play(length: int = 4, max_tries: int | None = 12, *, unique_digits: bool = True, allow_leading_zero: bool = False) -> None:
    history_guess = set()
    is_new_guess("2345", history_guess)


if __name__ == "__main__":
    play()