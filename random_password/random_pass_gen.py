import random
import pyperclip


DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
LOWCASE_ALPHA = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
UPCASE_ALPHA = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

SYMBOLS = ["@", "#", "$", "%", "=", ":", "?", ".", "/", "|", "~", ">", "*", "(", ")"]


def random_pass(MAX_LEN=12, no_symbols=False):
    rand_digit = random.choice(DIGITS)
    rand_locase = random.choice(LOWCASE_ALPHA)
    rand_upcase = random.choice(UPCASE_ALPHA)
    if not no_symbols:
        rand_symbols = random.choice(SYMBOLS)
        COMBINED_LIST = DIGITS + LOWCASE_ALPHA + UPCASE_ALPHA + SYMBOLS
    else:
        rand_symbols = ""
        COMBINED_LIST = DIGITS + LOWCASE_ALPHA + UPCASE_ALPHA

    temp_pass = rand_digit + rand_locase + rand_upcase + rand_symbols

    for _ in range(MAX_LEN - len(temp_pass)):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        temp_pass_list = list(temp_pass)
        random.shuffle(temp_pass_list)

    password = "".join(temp_pass_list)

    pyperclip.copy(password)
    print("Password copied to clipboard")
