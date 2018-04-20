from math import gcd

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

    #cayley table as multi-dem list
    def cayley_table(self):
        return [ [ self.operation(a, b) for b in self.elements ] for a in self.elements ]
        
    def identity(self):
        for element in self.elements:
            for test_element in self.elements:
                if not (self.compose(element, test_element) == test_element):
                    break
            return element
        #shouldn't reach
        raise Exception('No identity, not a group')

    def inverse(self, e):
        for element in self.elements:
            if self.compose(e, element) == self.identity():
                return element
        #shouldn't reach
        raise Exception('No inverse for {0}, not a group'.format(e)) 

    #string representation of a group (shows cayley table)
    def __repr__(self):
        cayley = 'o | ' #top corner
        #print column headers
        for header in self.elements:
            cayley += str(header) + '\t'
        #figure out how long of a separator between column headers and table to print
        equals_length = len(cayley) - 4 - len(self.elements)
        cayley += '\n----'
        for i in range(0, equals_length):
            cayley += '-\t'
        cayley += '\n'
        #print element table
        for row in self.elements:
            line = (str(row) + ' | ')
            for column in self.elements:
                line += str(self.compose(row,column)) + '\t'
            cayley += line + '\n'
        return cayley

if __name__ == '__main__':
    #order matters, the operation is done from right to left
    def Z(n):
        elements = [e for e in range(0,n)]
        return Group(elements, lambda e1, e2: ((e2 + e1) % n))
    print(Z(5))
    def coprime(a,b):
        return gcd(a,b) == 1
    def U(n):
        elements = [e for e in range(1,n) if coprime(e,n)]
        return Group(elements, lambda e1, e2: ((e2 * e1) % n))
    print(U(7))
    print(U(13).inverse(3))
