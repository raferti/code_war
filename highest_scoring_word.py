"""

Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in
the alphabet: a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest
in the original string.
All letters will be lowercase and all inputs will be valid.

"""

# First solution
def high(x):
    max_sum_letter = 0
    for word in x.split():
        sum_letter = sum([ord(i) - 96 for i in word])
        if max_sum_letter < sum_letter:
            max_sum_letter = sum_letter
            find_word = word
    return find_word


# Second solution
def high_second(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
