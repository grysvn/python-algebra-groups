class Group:
    def __init__(self, elements, operation):
        self.elements = elements
        self.operation = operation
    
    def compose(self, e1, e2):
        if (e1 not in self.elements) or (e2 not in self.elements):
            raise Exception('Elements not in group.')
        value = self.operation(e1, e2)
        if value not in self.elements:
            raise Exception('Closure does not hold.')
        return value

    def cayley_table(self):
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

def mod_addition(e1, e2):
    return (e1 + e2) % 5

Z4 = Group([0,1,2,3,4], mod_addition)
print("1 o 3 = " + str(Z4.compose(1,3)))
print()
print(Z4.cayley_table())

