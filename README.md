
# About

This project was used as a tool to familiarize myself with very basic group theory (for abstract algebra/MA407@ncsu) and python (for programming languages and modeling/CSC495-002@ncsu) during the 2018 spring semester. It's far from a complete exploration of either, but it was a fun project and helped me understand some concepts. If you'd like to contribute I'll add some things in the issues section that could be worked on for practice with groups, python, and open-source in general.

To run this file, simply open a terminal/cmd instance, change to the directory it's stored at, and type `python groups.py`.

To learn more about group theory, check out [this wonderful video on YouTube](https://www.youtube.com/watch?v=g7L_r6zw4-c) or give it a google.

# Examples and Usage

A group requires a set of elements and a binary operation over that set of elements, so those two fields are required in the initialization of a group object. I also added in a parameter that maps elements to a "pretty" string representation so that when printing the Cayley table (multiplication table of all elements in a group) it looks nice. Based on that, here's an example of constructing a basic group, the integers under addition mod n.

```python
def Z(n):
        #creates a list of all elements in the group
        elements = [e for e in range(0,n)]
        #creates the binary operation over the group, addition mod n
        operation = lambda e1, e2: ((e2 + e1) % n)
        #creates the mapping of group elements to a printable value, in this case just the element
        mapping = {e : e for e in elements}
        #constructs the group object and returns it
        return Group(elements, operation, mapping)
    
#prints the string representation of the group, the Cayley table
print(Z(5))
```

# Contributing

I have no clear goal in mind for this project, I'm just working on it because I find group theory cool and interesting. It also doubles as a good tool to familiarize myself with Python. If you'd like to contribute, feel free to check out the [issues](https://github.com/grayma/python-algebra-groups/issues) tab which lists what ideas could be implemented in the project.

# Notes

This is mostly for educational purposes, I'm far from an expert in Python or group theory, so be mindful of the following:

* Something could be incorrect or greatly improved. Feel free to file an issue, work on it, and submit a pull request.
* This is not meant to be a full abstract algebra framework. It may be fleshed out over time, but if you're interested in a full implementation, then you should check out [Sage](http://doc.sagemath.org/html/en/constructions/groups.html). 