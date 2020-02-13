"""
Next bigger number with the same digits (codewars.com kata)

You have to create a function that takes a positive integer number and
returns the next bigger number formed by the same digits:
12 ==> 21
513 ==> 531
2017 ==> 2071

If no bigger number can be composed using those digits, return -1:
9 ==> -1
111 ==> -1
531 ==> -1

Algorithm solution:
1. Find largest index i such that array[i − 1] < array[i].
2. Find largest index j such that j ≥ i and array[j] > array[i − 1].
3. Swap array[j] and array[i − 1].
4. Reverse the suffix starting at array[i].

"""


def next_bigger(num):
    snum = list(str(num))
    i = max([i for i in range(1, len(snum)) if snum[i - 1] < snum[i]],
            default=None)
    if i:
        j = max([j for j in range(i, len(snum)) if snum[j] > snum[i - 1]],
                default=None)
        if j:
            snum[j], snum[i - 1] = snum[i - 1], snum[j]
            snum[i:] = reversed(snum[i:])
            return int(''.join(snum))
    return -1


