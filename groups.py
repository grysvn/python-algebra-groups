from math import gcd

class Group:
    def __init__(self, elements, operation, table_name_map):
        """
        elements:       elements of the group
        operation:      operation on group
        table_name_map: map for cayley table to prettify any complex objects in groups for printing
        """
        self.elements = elements
        self.operation = operation
        self.table_name_map = table_name_map
        self.id = None #placeholder to find group identity later
    
    def compose(self, e1, e2):
        """
        e1: element 1 of composition
        e2: element 2 of composition

        returns the composition of e1 and e2. read "e1 o e2"
        """
        if (e1 not in self.elements) or (e2 not in self.elements):
            raise Exception('Elements not in group.')
        value = self.operation(e1, e2)
        if value not in self.elements:
            raise Exception('Closure does not hold for {0} + {1} = {2}.'.format(e1,e2,value))
        return value
        
    def identity(self):
        """
        Gets the identity of the group
        """
        if self.id:
            return self.id #if already found return
        for element in self.elements:
            for test_element in self.elements:
                if not (self.compose(element, test_element) == test_element):
                    break
            self.id = element
            return element
        #shouldn't reach
        raise Exception('No identity, not a group')

    def inverse(self, e):
        """
        e: element to find inverse of

        finds the inverse of an element `e`
        """
        for element in self.elements:
            if self.compose(e, element) == self.identity():
                return element
        #shouldn't reach
        raise Exception('No inverse for {0}, not a group'.format(e)) 

    def __repr__(self):
        longest = max(len(str(v)) for k,v in self.table_name_map.items()) + 2
        #makes an element into a guarenteed len cell
        def cell(data,filler=' '):
            #thanks https://stackoverflow.com/questions/5676646/how-can-i-fill-out-a-python-string-with-spaces
            return '{message:{fill}{align}{width}}'.format(
               message=data,
               fill=filler,
               align='^',
               width=longest
            )
        #maps elements to pretty values and strs
        def data_cell(e):
            return cell(str(self.table_name_map[e]))
        vert_sepr = '|' #vertical bar separator
        def hori_sepr(char): #horizontal row separator
            return cell('',filler=char)
        def row_sepr(char): #row separator
            return (hori_sepr(char) + vert_sepr * 2) + ((hori_sepr(char) + vert_sepr) * len(self.elements)) + '\n'

        cayley = cell('o') + vert_sepr * 2
        #headers
        for header in self.elements:
            cayley += data_cell(header) + vert_sepr
        cayley += '\n' + row_sepr('=')

        #table
        for row in self.elements:
            line = (data_cell(row) + vert_sepr * 2)
            for column in self.elements:
                line += data_cell(self.compose(row,column)) + vert_sepr
            cayley += line + '\n' + row_sepr('-')
        return cayley

if __name__ == '__main__':
    ###########
    #group Z_n#
    ###########
    def Z(n):
        elements = [e for e in range(0,n)]
        return Group(elements, lambda e1, e2: ((e2 + e1) % n), {e : e for e in elements})
    print("Z_5")
    print(Z(5))

    ###########
    #group U_n#
    ###########
    def coprime(a,b):
        return gcd(a,b) == 1
    def U(n):
        elements = [e for e in range(1,n) if coprime(e,n)]
        return Group(elements, lambda e1, e2: ((e2 * e1) % n), {e : e for e in elements})
    print("U_8")
    print(U(8))

    ###########
    #group S_3#
    ###########
    p0 = ((1,2,3),(1,2,3))
    p1 = ((1,2,3),(2,3,1))
    p2 = ((1,2,3),(3,1,2))
    p3 = ((1,2,3),(1,3,2))
    p4 = ((1,2,3),(3,2,1))
    p5 = ((1,2,3),(2,1,3))
    p = (p0,p1,p2,p3,p4,p5)
    name_map = { p[i] : "p{0}".format(i) for i in range(0,len(p)) }
    #operation on S_3
    def map(e1,e2):
        return ((1,2,3), tuple( e1[1][e1[0].index(i)] for i in e2[1] ) )
    S3 = Group(p, map, name_map)
    print("S_3")
    print(S3)
    print("Identity: {0}".format(S3.identity()))
    print("Inverse of p4: {0}".format(name_map[S3.inverse(p4)]))

