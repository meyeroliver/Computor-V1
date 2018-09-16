from Operations import *


class Solver:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.solution = []

    def solve_linear_equation(self):
        c_coefficient = -1 * self.c.coefficient
        solution_1 = c_coefficient / self.b.coefficient
        self.solution.append(solution_1)
        return self.solution

    def solver_quadratic_equation(self):
        a_coefficient = self.a.coefficient
        b_coefficient = self.b.coefficient
        c_coefficient = self.c.coefficient
        root = ft_sqrt(ft_power(b_coefficient, 2) - 4 * a_coefficient * c_coefficient)
        solution_1 = (-b_coefficient + root) / 2
        solution_2 = (-b_coefficient - root) / 2
        self.solution.append(solution_1)
        self.solution.append(solution_2)
        return self.solution
    
    def main(self):
        return 0


if __name__ == "__main__":
    main()
