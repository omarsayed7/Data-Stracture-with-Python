# class Node used to construct a node in the linkedlist
#### inside the constructor define the data we contain in the node
#### and refrence to the next node
class Node(object):
    def __init__(self,data):
        self.data = data
        self.nextNode = None
# class linked list used to store the operations of the linked list
#### in linked list we only can access to the first node which is called head
#### and the size of the linked list
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size_ = 0

# method to insert some data at the beginning of the linked list remember O(1)
    def insert_start(self,data):
        self.size_ += 1
        newNode = Node(data)

        if not self.head :
            self.head = newNode
        else :
            newNode.nextNode = self.head
            self.head = newNode

# method to get the size of the linked list remember O(1)
    def size(self):
        return self.size_

# method to insert at the end of linked list, we have to iterate over the L.L O(N)
    def insert_end(self,data):
        self.size_ += 1
        newNode = Node(data)
        last_node = self.head

        while last_node.nextNode is not None :
            last_node = last_node.nextNode

        last_node.nextNode = newNode

# method to traverse L.L which can be traversed in only forwrad direction starting form the first data element, O(N)
    def traverse(self):
        last_node = self.head
        list_items = []
        while last_node is not None :
            list_items.append(last_node.data)
            last_node = last_node.nextNode
        print(list_items)

# method to remove an existing node using the key for that node.
    def remove(self,data):
        if self.head is None :
            return
        self.size_ -= 1
        previousNode = None
        current_node = self.head
        while current_node.data != data:
            previous_node = current_node
            current_node = current_node.nextNode
        if previous_node is None :
            self.head = current_node.nextNode
        else :
            previous_node.nextNode = current_node.nextNode
# method for searching in the linked list by the value of the needed node
    def search(self,data):
        current_node = self.head
        print(current_node.data,data)
        while current_node.data != data :
            current_node = current_node.nextNode

        if current_node.data != data :
            return "Given item doesn't exist"
        else :
            if current_node.data == data and current_node.nextNode is None :
                return current_node.data , current_node.nextNode
            elif current_node.data == data and current_node.nextNode is not  None:
                return current_node.data , current_node.nextNode.data



if __name__ == '__main__':
    linkedlist = LinkedList() # start a linked List
    linkedlist.insert_start(1)
    linkedlist.insert_start(2)
    linkedlist.insert_start(3)
    linkedlist.insert_start(4)
    linkedlist.insert_end(100)

    linkedlist.traverse()

    size = linkedlist.size()
    print('size:',size)

    linkedlist.remove(3)

    linkedlist.traverse()

    size = linkedlist.size()
    print('size after removing:',size)

    node = linkedlist.search(90)
    print(node)
