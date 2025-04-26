import os


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    """
    main _summary_

    Returns:
        _type_: _description_
    """
    sentence = str(input("Enter a sentence: "))

    # Get the individual words
    words = sentence.split()

    # Count how many words
    number_of_words = len(words)

    # Get the longest word
    max = 0
    length = 0
    longest_word = ""

    for w in words:
        length = len(w)
        if length >= max:
            max = length
            longest_word = w

    print(f"The number of words in the sentence is: {number_of_words}")
    print(f"The longest word in the sentence is: '{longest_word}'", end="\n\n")


if __name__ == "__main__":
    cls()
    main()
