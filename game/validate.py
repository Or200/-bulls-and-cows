def is_valid_guess(guess: str, length: int, unique_digits: bool = True) -> tuple[bool, str]:
    my_set = set()
    if len(guess) == length and guess.isdigit():
        if unique_digits:
            for i in guess:
                my_set.add(i)
            if len(my_set) == length:
                return True, guess
        else:
            return True, guess
        
    return False, guess
            

    

def is_new_guess(guess: str, history: set[str]) -> bool:
    pass

