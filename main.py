from game.io import prompt_guess, print_feedback, print_result, print_status
from game.validate import is_new_guess
from game.secret import generate_secret
from game.logic import init_state, score_guess, is_won, apply_guess

def play(length: int = 4, max_tries: int | None = 12, *, unique_digits: bool = True, allow_leading_zero: bool = False) -> None:
    history_guess = set()
    game = init_state(generate_secret(), length, None, True, False, history_guess)

    while True:
        guess = prompt_guess(length)

        if guess not in history_guess:
            if is_new_guess(guess, history_guess):
                bull_cow = score_guess(game["secret"], guess)
                apply_guess(game, guess)
                print("====================")
                print_feedback(guess, bull_cow[0], bull_cow[1])
                print_status(game)
                print("====================")
                if is_won(bull_cow[0], length):
                    print_result(game)
                    break
        else:
            print("duplicate number - try again")





if __name__ == "__main__":
    play()