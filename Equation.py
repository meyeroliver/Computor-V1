from Term import *
from Solver import *


class Equation:
    """
        Reduced eqaution format
        The degree expresses that of the variable e.g (X, Y)
        a -> degree 2
        b -> degree 1
        c -> degree
    """
    def __init__(self, string):
        self.string = string
        self.equation_items = []
        self.reduced_equation = []
        self.terms = []
        self.a = Term("0*X^2")
        self.b = Term("0*X^1")
        self.c = Term("0*X^0")

    def processing_string(self):
        term = ''
        sign = '+'
        found_equal = 0;
        if self.string[0] == '-':
            sign = '-'
        for char in self.string:
            if found_equal == 1 and sign == '+':
                sign = '-'
            elif found_equal == 1 and sign == '-':
                sign = '+'
            if char == '=':
                found_equal = 1
            if char == '+' or char == '-' or char == '=':
                if term == ' ' or term == '':
                    sign = char
                    continue
                final_term = sign + term
                self.equation_items.append(final_term.replace(' ', '').replace('=', ''))
                term = ''
                if char != '=':
                    sign = char
                continue
            term = term + char
        final_term = sign + term
        self.equation_items.append(final_term.replace(' ', ''))

    def reduce_equation(self):
        for item in self.equation_items:
            term = Term(item)
            self.terms.append(term)
        """
        The following will group the like together
        """
        for item in self.terms:
            if item.variable_degree == 2:
                self.a.add_coefficient(item)
            elif item.variable_degree == 1:
                self.b.add_coefficient(item)
            else:
                self.c.add_coefficient(item)
        self.print_reduced_equation()

    def check_highest_degree_1(self):
        previous = 0
        for item in self.terms:
            if item.variable_degree > previous and item.coefficient != 0:
                previous = item.variable_degree
        return previous

    def check_highest_degree(self):
        if self.a.coefficient != 0:
            return str(self.a.variable_degree)
        elif self.b.coefficient != 0:
            return str(self.b.variable_degree)
        else:
            return str(self.c.variable_degree)

    def check_discriminant(self):
        return self.b.coefficient * self.b.coefficient - 4 * self.a.coefficient * self.c.coefficient

    def print_discriminant_result(self, discriminant):
        if discriminant > 0:
            print("A positive discriminant indicates that the quadratic has two distinct real number solutions.")
        elif discriminant == 0:
            print("A discriminant of zero indicates that the quadratic has a repeated real number solution.")
        else:
            print("A negative discriminant indicates that neither of the solutions are real numbers.")

    def print_highest_degree(self, degree):
        print("Polynomial degree -> " + str(degree))

    def print_equation_items(self):
        for item in self.equation_items:
            print(item)

    def print_reduced_equation(self):
        reduced_equation_string = self.a.to_string()[1:] + " " + self.b.to_string() + " " + self.c.to_string() + " = 0"
        print("Reduced form ->  "+reduced_equation_string)


if __name__ == "__main__":
    summer_1 = "1*X^2 - 5*X^1 + 2*X^0 = -2*X^1"
    summer_2 = "-2*X^1 + 0*X^2 + 2*X^1 - 18*X^0 = -4*X^1 + 6*X^0"
    summer_3 = "-10*X^4 + 0*X^2 + 0*X^1 = -4*X^0"
    summer_4 = "4*X^1 = 4*X^1"
    myEquation = Equation(summer_3)
    myEquation.processing_string()
    myEquation.reduce_equation()
    highest_degree = int(myEquation.check_highest_degree_1())
    myEquation.print_highest_degree(highest_degree)
    workerBee = Solver(myEquation.a, myEquation.b, myEquation.c)
    if highest_degree == 0:
        print("There is no solution for this problem")
    elif highest_degree == 1:
        result = workerBee.solve_linear_equation[0]
        if result is None:
            print("Solution is undefined")
        else:
            print("The solution is :")
            print("X = " + str(result))
    elif highest_degree == 2:
        discriminant = myEquation.check_discriminant()
        myEquation.print_discriminant_result(discriminant)
        result = workerBee.solver_quadratic_equation()
        print("X1 = " + str(result[0]))
        print("X2 = " + str(result[1]))
    else:
        print("The polynomial degree is strictly greater than 2, I can't solve.")

