import random

def generate_secret(length: int = 4, *, unique_digits: bool = True, allow_leading_zero: bool = False) -> str:
    secret_num_list = []
    secret_num_set = set()

    if unique_digits:
        while len(secret_num_set) != length:
            num = int((random.random()) // 0.1)
            secret_num_set.add(str(num))

        secret_num_list = list(secret_num_set)

    else:
        while len(secret_num_list) != length:
            num = int((random.random()) // 0.1)
            if num not in secret_num_list:
                secret_num_list.append(str(num))



    if not allow_leading_zero:
        while secret_num_list[0] == "0":
            secret_num_list[0] = str(int((random.random()) // 0.1))
        


    secret_num = "-".join(secret_num_list)
    return secret_num
