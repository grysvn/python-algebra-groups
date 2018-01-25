class Group:
    def __init__(self, elements, operation):
        self.elements = elements
        self.operation = operation
    
    #read e1 o e2
    def compose(self, e1, e2):
        if (e1 not in self.elements) or (e2 not in self.elements):
            raise Exception('Elements not in group.')
        value = self.operation(e1, e2)
        if value not in self.elements:
            raise Exception('Closure does not hold.')
        return value

    def cayley_table(self):
        return [ [ self.operation(a, b) for b in self.elements ] for a in self.elements ]

    def __repr__(self):
        cayley = "o | " #top corner
        #print column headers
        for header in self.elements:
            cayley += str(header) + "\t"
        #figure out how long of a separator between column headers and table to print
        equals_length = len(cayley) - 4 - len(self.elements)
        cayley += "\n===="
        for i in range(0, equals_length):
            cayley += "=\t"
        cayley += "\n"
        #print element table
        for row in self.elements:
            line = (str(row) + " | ")
            for column in self.elements:
                line += str(self.compose(row,column)) + "\t"
            cayley += line + "\n"
        return cayley

#order matters, the operation is done from right to left
def mod_addition(e1, e2):
    return (e2 + e1) % 5

Z5 = Group([0,1,2,3,4], mod_addition)
print("1 o 3 = " + str(Z5.compose(1,3)))
print()
print(Z5)

