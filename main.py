## This code counts the number of unique words and the number of their occurrences within a text

import re
from collections import Counter


def format_text(fullText):
    allAlphaNumString = re.sub(r'[^a-zA-Z0-9]', ' ', fullText).lower()
    return allAlphaNumString.split()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fullText = open('cat_in_the_hat.txt').read()
    formattedText = format_text(fullText)
    wordSet = Counter(formattedText)
    x = 1
    for word, instances in wordSet.items():
        print(x, end=' ')
        print(word, instances)
        x += 1
