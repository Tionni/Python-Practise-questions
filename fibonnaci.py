


def fibonnaci(n):
    t1 = 0
    t2= 1
    nextterm = t1 + t2
    print(t1)
    print(t2)
    m = 3
    while (m <= n):
        print(nextterm)
        t1 = t2
        t2 = nextterm
        nextterm = t1 + t2
        m = m + 1

print("Enter a number")
n = int(input())
fibonnaci(n)
