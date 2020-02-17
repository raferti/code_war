"""

Create a simple calculator that given a string of operators (), +, -, *, /
and numbers separated by spaces returns the value of that expression

Example:
Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7

Remember about the order of operations! Multiplications and divisions have
a higher priority and should be performed left-to-right. Additions and
subtractions have a lower priority and should also be performed left-to-right.


calc = Calculator()
print(calc.evaluate('2 + 3 * 4 / 3 - 6 / 3 * 3 + 8'))
"""


class Calculator(object):

    def update_list(self, source, opr):
        swith = {
            '/': lambda x, y: x / y,
            '*': lambda x, y: x * y,
            '-': lambda x, y: x - y,
            '+': lambda x, y: x + y
        }

        ss_copy = source[:]
        idx = source.index(opr)
        a = float(ss_copy.pop(idx - 1))
        b = float(ss_copy.pop(idx))
        res = swith[opr](a, b)
        ss_copy.remove(opr)
        ss_copy.insert(idx - 1, res)
        return ss_copy

    def evaluate(self, string):
        ss = string.split()

        while len(ss) > 1:
            for sign in ss:
                if (sign == '/') or (sign == '*'):
                    ss = self.update_list(ss, sign)
            for sign in ss:
                if (sign == '+') or (sign == '-'):
                    ss = self.update_list(ss, sign)

        return float(ss[0])
