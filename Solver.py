from Operations import *


class Solver:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.solution = []

    @property
    def solve_linear_equation(self):
        if self.b.coefficient == 0:
            return None
        c_coefficient = -1 * self.c.coefficient
        solution_1 = float(c_coefficient) / float(self.b.coefficient)
        self.solution.append(solution_1)
        return self.solution

    def solve_quadratic_equation(self):
        a_coefficient = self.a.coefficient
        b_coefficient = self.b.coefficient
        c_coefficient = self.c.coefficient
        root = ft_sqrt(ft_power(b_coefficient, 2) - 4 * a_coefficient * c_coefficient)
        solution_1 = (-b_coefficient + root) / 2
        solution_2 = (-b_coefficient - root) / 2
        self.solution.append(solution_1)
        self.solution.append(solution_2)
        return self.solution

    def solve_complex_equation(self):
        a_coefficient = self.a.coefficient
        b_coefficient = self.b.coefficient
        c_coefficient = self.c.coefficient
        root = ft_sqrt(ft_abs(ft_power(b_coefficient, 2) - 4 * a_coefficient * c_coefficient))
        my_complex = ft_complex(-b_coefficient, root)
        return str(my_complex[0]) +" +/- "+ str(my_complex[1]) + "i"

    @property
    def main(self):
        return 0


if __name__ == "__main__":
    main()
