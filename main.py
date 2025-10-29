from game.secret import generate_secret

def play(length: int = 4, max_tries: int | None = 12, *, unique_digits: bool = True, allow_leading_zero: bool = False) -> None:
    generate_secret()



if __name__ == "__main__":
    play()