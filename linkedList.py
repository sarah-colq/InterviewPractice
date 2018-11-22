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


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def main():
    print(1)

if __name__ == "__main__":
    sys.exit(main())