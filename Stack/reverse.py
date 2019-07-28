#this file used to reverse any type of string using Stack ADT
# first import stack class from Stack.py
from Stack import Stack

#Create an object from Stack class
new_stack = Stack()
#Check is it empty or not
print(new_stack.isEmpty())


if __name__ == '__main__':
    file =  open('data_to_reverse.txt','r')
    for line in file :
        for word in line.split():
            print(word)

        new_stack.push('\n')
    file.close()
    output = open('data_after_reverse.txt','w')
    while not new_stack.isEmpty():
        output.write(new_stack.pop()+'\n')
    output.close()
