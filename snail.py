"""

Snail Sort
Given an n x n array, return the array elements arranged from outermost
elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the
next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

This image will illustrate things more clearly:

NOTE: The idea is not sort the elements from the lowest value to the
highest; the idea is to traverse the 2-d array in a clockwise
snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array
inside an array [[]].

https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/python
"""


# Solution 1 (bad practice - need rafactoring)
def count_element(array):
    sum_len = sum(array, [])
    return len(sum_len)


def right(x, y, source, out, cnt):
    for _ in range(1, cnt):
        x += 1
        out.append(source[y][x])
    return x, y


def bottom(x, y, source, out, cnt):
    for _ in range(1, cnt):
        y += 1
        out.append(source[y][x])
    return x, y


def left(x, y, source, out, cnt):
    for _ in range(1, cnt):
        x -= 1
        out.append(source[y][x])
    return x, y


def top(x, y, source, out, cnt):
    for _ in range(1, cnt):
        y -= 1
        out.append(source[y][x])
    return x, y


def snail(array):
    sn = []
    cc = count_element(array)
    x, y = -1, 0
    takt = sorted([i for i in range(1, len(array[0])+1)] * 2 + [len(array[0])+1])
    while len(sn) != cc:
        t = takt.pop()
        x, y = right(x, y, array, sn, t)
        if len(sn) == cc:
            break

        t = takt.pop()
        x, y = bottom(x, y, array, sn, t)
        if len(sn) == cc:
            break

        t = takt.pop()
        x, y = left(x, y, array, sn, t)
        if len(sn) == cc:
            break

        t = takt.pop()
        x, y = top(x, y, array, sn, t)
        if len(sn) == cc:
            break
    return sn


# Solution 2
def snails(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = list(zip(*array))
        array.reverse()
    return a


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print(snail(array))
