class Term:
    def __init__(self, string):
        self.coefficient = float(string.split('*')[0])
        self.variable_degree = float(string.split('*')[1].split('^')[1])
        self.checksum = 0
        self.term_str = ""

    def to_string(self):
        sign = ""
        if self.coefficient >= 0:
            sign = "+"
        self.term_str = sign + str(self.coefficient) + " * X^" + str(self.variable_degree)
        return self.term_str

    def add_coefficient(self, term2):
        self.coefficient += term2.coefficient

    def print_attributes(self):
        print("The coefficient is -> ",  self.coefficient)
        print("The degree of x is -> ", self.variable_degree)

