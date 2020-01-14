"""

Bob is preparing to pass IQ test. The most frequent task in this test is
to find out which one of the given numbers differs from the others.
Bob observed that one number usually differs from the others in evenness.
Help Bob — to check his answers, he needs a program that among the given
numbers finds one that is different in evenness, and return a position
of this number.

! Keep in mind that your task is to help Bob solve a real IQ test,
which means indexes of the elements start from 1 (not 0)

##Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the
 numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the
 numbers are odd

"""


# First solution
def iq_test(numbers):
    numbers = numbers.split(' ')
    c_c = 0
    c_n = 0
    for num, val in enumerate(numbers):
        if int(val) % 2 == 0:
            c_c += 1
            c_c_value = num + 1
        else:
            c_n += 1
            c_n_value = num + 1

    if c_c == 1:
        return c_c_value
    else:
        return c_n_value


# Second solution
def iq_test_compact(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1



