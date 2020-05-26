import sys
from .random_pass_gen import random_pass


def main():
    args = sys.argv[1:]
    no_symbol = True if "--no_symbol" in args else False
    args.remove("--no_symbol")

    if len(args) == 0:
        random_pass(no_symbols=no_symbol)
    else:
        if "-l" in args:
            try:
                random_pass(int(args[args.index("-l") + 1]), no_symbols=no_symbol)
            except Exception as e:
                print("Command Not Found.")
                help()
        elif sys.argv[1] == "-h":
            help()
        else:
            print("Command Not Found.")
            print("Use 'random_pass -h' to get help.")


def help():
    print(
        """
Available Commands:

    -h  -  To get help.
    -l <length of required password>  -  To Mension the length of password to generate. (Default is 12).
    --no_symbol  -  To not include special symbols in the password.
    """
    )


if __name__ == "__main__":
    main()
