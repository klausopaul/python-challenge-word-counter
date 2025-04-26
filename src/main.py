import os


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    """
    main _summary_

    Returns:
        _type_: _description_
    """
    print ("Hello World!")
    return None


if __name__ == "__main__":
    cls()
    main()
