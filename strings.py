import sys

def palindrome(s):
    n = len(s)
    i = 0
    j = n - 1
    while i < j:
        while s[i] == " ":
            i+=1
        while s[j] == " ":
            j -= 1
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def main():
    print(palindrome('nurses  run'))
    print(palindrome('hello'))
    print(palindrome('01210'))

if __name__ == "__main__":
    sys.exit(main())