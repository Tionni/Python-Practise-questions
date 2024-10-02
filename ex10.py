def check_list(l1, l2):
    l3 = list(dict.fromkeys([i for i in l1 if i in l2]))
    return l3
# def check_list(l1, l2):
#     l3 = []
#     for i in l1:
#         if i in l2:
#             l3.append(i)
#     l3 = list(dict.fromkeys(l3))
#     return l3

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(check_list(a, b))
