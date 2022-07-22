import re
import sys
from english_words import english_words_lower_set

letters = sys.argv[1]
regex = rf"[{letters}]*{letters[0]}+[{letters}]*"

for word in english_words_lower_set:
    if len(word) < 4:
        continue
    m = re.fullmatch(regex, word)
    if m:
        print(m[0])

