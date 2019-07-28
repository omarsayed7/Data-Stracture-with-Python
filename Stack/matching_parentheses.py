'''
Code Description :
------------------
Each opening symbol must match its corresponding closing symbol
Example
Correct: ()(()){([()])}
Correct: ((()(()){([()])}))
Incorrect: ({[])}
etc...
'''
#frist import Stack class
from Stack import Stack



def is_matched(expr):
    '''
    return true if all delimiters are matched , False if not!
    '''
    #define a blueprint for the delimiters
    left = '({['
    right = ')}]'
    #Create an object from Stack class
    new_stack = Stack()

    #Check is it empty or not
    print('init:',new_stack.isEmpty())

    for x in expr :
        if x in left :
            new_stack.push(x)
        elif x in right:
            if new_stack.isEmpty():
                return False
            elif right.index(x) != left.index(new_stack.pop()):
                return False
    return new_stack.isEmpty()

if __name__ == '__main__':
    print('is matched :',is_matched('[][(]'))
