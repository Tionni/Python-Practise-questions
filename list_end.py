
def list_ends(a):
    a2 = []
    a2.append(a[0])
    a2.append(a[-1])
    return a2
    
a = [5, 10, 15, 20, 25]

print(list_ends(a))