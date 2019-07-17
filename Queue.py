class Queue:
    def __init__(self):
        '''
        Initialization the Queue class automatically
        class methods :
            1-enqueue
            2-peek
            3-dequeue
            4-isEmpty
            5-sizeof
        '''
        self.queue = []

    def enqueue(self,data):
        '''
        add new item into the queue
        '''
        self.queue.append(data)

    def dequeue(self):
        '''
        delete the first item added in the queue
        then
        return the item has been deleted
        '''
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        '''
        return the first item added in the queue
        '''
        return self.queue[0]

    def isEmpty(self):
        '''
        return true if the queue is empty
        '''
        return self.queue == []

    def sizeof(self):
        '''
        return the size of the queue
        '''
        return len(self.queue)

if __name__ == '__main__':
    newqueue = Queue()
    print(newqueue.isEmpty())
    newqueue.enqueue(5)
    newqueue.enqueue(33)
    newqueue.enqueue(10)
    newqueue.enqueue(20)
    print(newqueue.isEmpty())
    print(newqueue.sizeof())
    print(newqueue.peek())
    newqueue.dequeue()
    print(newqueue.sizeof())
    print(newqueue.peek())
