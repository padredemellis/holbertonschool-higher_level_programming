#!/usr/bin/python3
'''
We create an inheritor class
'''

class MyList(list):
    '''My list inheritor of list'''
    
    
    def print_sorted(self):
        
        
        """
        Prints the list in ascending sorted order.
        Assumes all elements are of type int.
        Does not modify the original list.
        """
        print(sorted(self))
