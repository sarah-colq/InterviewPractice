import sys
import math

class MaxHeap:

    def __init__(self):
        self.heap = []
        self.length = 0
        self.heap_size = 0

    def parent(self,i):
        return math.ceil(i/2) - 1

    def right(self,i):
        return 2*i + 1

    def left(self,i):
        return 2*i + 2

    def max_heapify(self,i):
        l = self.left(i)
        r = self.right(i)
        if l <= self.heap_size - 1 and self.heap[l] > self.heap[i]:
            largest = l
        else:
            largest = i
        if r <= self.heap_size - 1 and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i],self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    def build_max_heap(self,A):
        self.heap_size = len(A)
        self.heap = A
        self.length = len(A)
        start = math.floor(self.heap_size/2 - 1)
        for i in range(start,-1,-1):
            self.max_heapify(i)

def heapsort(a):
    A = MaxHeap()
    A.build_max_heap(a)
    size = len(a)
    for i in range(size - 1,0,-1):
        A.heap[0],A.heap[i] = A.heap[i], A.heap[0]
        A.heap_size = A.heap_size - 1
        A.max_heapify(0)
    return A.heap

def quicksort(a):
    size = len(a)
    if size > 1:
        r = size - 1
        x = a[r]
        i = -1
        for j in range(0,r):
            if a[j] <= x:
                i += 1
                a[i],a[j] = a[j],a[i]
        a[i+1],a[r] = a[r],a[i+1]
        q = i + 1
        a[:q] = quicksort(a[:q])
        a[q+1:] = quicksort(a[q+1:])
    return a

def mergesort(a):
    size = len(a)
    if size > 1:
        split = size//2
        c = mergesort(a[:split])
        d = mergesort(a[split:])
        b = []
        while c or d:
            if c and d:
                if c[0] < d[0]:
                    b.append(c.pop(0))
                else:
                    b.append(d.pop(0))
            elif c:
                b.extend(c)
                c = []
            else:
                b.extend(d)
                d = []
        a = b
    return a

def main():
    arr = [3,2,1,4,7,2,5]
    arr2 = [1,2,3,4,3]
    print(quicksort(arr))
    print(mergesort(arr))
    print(mergesort(arr2))
    print(quicksort(arr2))
    print(heapsort(arr2))
    print(heapsort(arr))

if __name__ == '__main__':
    sys.exit(main())