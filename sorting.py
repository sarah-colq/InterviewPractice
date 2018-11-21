import sys

def quicksort(a):
    size = len(a)
    print(a)
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

def heapsort(a):
    print(a)

def main():
    arr = [3,2,1,4,7,2,5]
    print(quicksort(arr))
    print(mergesort(arr))

if __name__ == '__main__':
    sys.exit(main())