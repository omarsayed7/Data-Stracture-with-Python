class Stack:
    def __init__(self):
        '''
        Initialization the stack class automatically
        class methods :
            1-push
            2-peek
            3-pop
            4-isEmpty
            5-sizeof
        '''
        self._stack = []

    def isEmpty(self):
        '''
        return true if the stack is empty
        '''
        return self._stack == []

    def push(self,data):
        '''
        push new item into the stack
        '''
        self._stack.append(data)

    def pop(self):
        '''
        delete the last item added in the stack
        then
        return the item has been deleted
        '''
        data = self._stack[-1]
        del self._stack[-1]
        return data

    def peek(self):
        '''
        return the last item added in the stack
        '''
        return self._stack[-1]

    def sizeof(self):
        '''
        return the size of the stack
        '''
        return len(self._stack)


if __name__ == '__main__':
    newstack = Stack()
    print(newstack.isEmpty())
    newstack.push(5)
    newstack.push(2)
    newstack.push(4)
    newstack.push(10)
    print(newstack.sizeof())
    print(newstack.isEmpty())
    print(newstack.peek())
    print(newstack.pop())
    print(newstack.sizeof())
