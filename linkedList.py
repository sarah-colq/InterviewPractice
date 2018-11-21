import sys

class LinkedList:
    def __init__(self,head = None):
        self.head = head

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def set_next(self,next):
        self.next = next