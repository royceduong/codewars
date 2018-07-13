
# def unique_in_order(iterable):
#     array = []
#     for v in iterable:
#             array.append(v)
#     print(array)
#     return array


# def unique_in_order(iterable):
#     a = list(iterable)
#     i = 0
#     b = []
#     n = len(a)
#     while i < n:
#         j = 1
#         while j < n:
#             if j != n-1:
#                 if a[i] == a[j]:
#                     j += 1
#                 else: 
#                     b.append(a[i])
#                     i = j
#                     j += 1
#             else:
#                 if a[i] == a[j]:
#                     b.append(a[i])
#                 else:
#                     b.append(a[i])
#                     b.append(a[j])
#                 j += 1
#                 i = n
#     print(b)


# def unique_in_order(iterable):
#     a = list(iterable)
#     n = len(a)
#     i = 0
#     b = []
#     while i < n:
#         j = i + 1
#         while j < n and a[i] == a[j]:
#             j += 1
#         b.append(a[i])
#         i = j
#     print(b)
#     return b


# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]


def unique_in_order(iterable):
    a = list(iterable)
    i = 0
    b = []
    n = len(a)
    while i < n:
        j = i + 1
        while j < n and a[i] == a[j]:
            j += 1
        b.append(a[i])
        i = j
    print(b)
    return b
unique_in_order('AAAABBBCCDAABBB')
unique_in_order('ABBCcAD')   
unique_in_order([1,2,2,3,3])  