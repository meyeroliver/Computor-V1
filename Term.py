class Term:
    def __init__(self, string):
        self.coefficient = int(string.split('*')[0])
        self.variable_degree = int(string.split('*')[1].split('^')[1])

    def printAttributes(self):
        print("The coefficient is -> ",  self.coefficient)
        print("The degree of x is -> ", self.variable_degree)

