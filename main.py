from game.io import prompt_guess

def play(length: int = 4, max_tries: int | None = 12, *, unique_digits: bool = True, allow_leading_zero: bool = False) -> None:
    history_guess = set()
    prompt_guess(length)


if __name__ == "__main__":
    play()