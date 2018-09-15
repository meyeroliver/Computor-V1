from Term import *

class Equation:
    def __init__(self, string):
        self.string = string
        self.equation_items = []

    def processing_string(self):
        term = ''
        sign = '+'
        found_equal = 0;
        if self.string[0] == '-':
            sign = '-'
        for char in self.string:
            if found_equal == 1 and sign == '+':
                sign = '-'
            if found_equal == 1 and sign == '-':
                sign = '+'
            if char == '=':
                found_equal = 1
            if char == '+' or char == '-':
                final_term = sign + term
                # need to find a better way to do this
                self.equation_items.append(final_term.replace(' ', '').replace('=', ''))
                term = ''
                if char != '=':
                    sign = char
                continue
            term = term + char
        final_term = sign + term
        self.equation_items.append(final_term.replace(' ', ''))

    def reduce_equation(self):
        terms = []
        for item in self.equation_items:
            term = Term(item)
            term.printAttributes()
            print("-----------------")
            terms.append(term)

    def print_equation_items(self):
        for item in self.equation_items:
            print(item)


sum = "1*X^2 - 3*X^1 + 2*X^0 = -2*X^1"
myEquation = Equation(sum)
myEquation.processing_string()
myEquation.reduce_equation()
#myEquation.print_equation_items()
