"""

There is a secret string which is unknown to you. Given a collection of
random triplets from the string, recover the original string.

A triplet here is defined as a sequence of three letters such that each
letter occurs somewhere before the next in the given string. "whi" is a
triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once
in the secret string.

You can assume nothing about the triplets given to you other than that
they are valid triplets and that they contain sufficient information to
deduce the original string. In particular, this means that the secret
string will never contain letters that do not occur in one of
the triplets given to you.

"""


# Solution 1
def merge_to_one_list(triplets):
    one_list = []
    for line in triplets:
        one_list += line
    return list(set(one_list))


def swap(a, b, secret_list):
    index_a = secret_list.index(a)
    index_b = secret_list.index(b)
    secret_list[index_a], secret_list[index_b] = b, a
    return secret_list


def recoverSecret(triplets):
    secret = merge_to_one_list(triplets)
    flag = True

    while flag:
        flag = False

        for line in triplets:
            if secret.index(line[0]) > secret.index(line[1]):
                secret = swap(line[1], line[0], secret)
                flag = True

            if secret.index(line[0]) > secret.index(line[2]):
                secret = swap(line[2], line[0], secret)
                flag = True

            if secret.index(line[1]) > secret.index(line[2]):
                secret = swap(line[2], line[1], secret)
                flag = True
    return ''.join(secret)


# Solution 2
def recoverSecret_two(triplets):
    r = list(set([i for l in triplets for i in l]))
    for l in triplets:
        fix(r, l[1], l[2])
        fix(r, l[0], l[1])
    return ''.join(r)


def fix(l, a, b):
    if l.index(a) > l.index(b):
        l.remove(a)
        l.insert(l.index(b), a)

