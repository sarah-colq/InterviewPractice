import sys

class LinkedList:
    def __init__(self,head = None):
        self.head = head

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def search_list(self,val):
        x = self.head
        while x and x.value != val:
            x = x.next
        return x

    def prepend(self,node):
        node.next = self.head
        self.head = node

    def append(self,node):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def delete_front(self):
        self.head = self.head.next

    def print(self):
        string = ''
        temp = self.head
        while temp:
            string += str(temp.value)
            temp = temp.next
            string += ' - > '
        string += 'None'
        print(string)

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def print(self):
        string = ''
        temp = self
        while temp:
            string += str(temp.value)
            temp = temp.next
            string += ' - > '
        string += 'None'
        print(string)

def reversell(llist):
    current = llist.head
    nextNode = current.next
    current.next = None
    prev = current.next
    while nextNode:
        prev = current
        current = nextNode
        nextNode = current.next
        current.next = prev
    llist.head = current
    return llist

def main():
    Node1 = Node(1)
    Node2 = Node(2)
    Node3 = Node(3)
    Node4 = Node(4)
    myList = LinkedList(Node1)
    myList.append(Node2)
    myList.append(Node3)
    myList.append(Node4)
    myList.print()
    newList = reversell(myList)
    newList.print()


if __name__ == "__main__":
    sys.exit(main())