# Pass by ref
# def fun(x) :
#     x[0] = 20
#     return x

# lst = [10, 11, 12, 13, 14, 15]
# fun(lst)

# print(lst)

# Pass by value
# def new(a) :
#     x = '2' + a
#     print(x)
#     print(id(x))

# a = "hello"
# new(a)

# print(a)
# print(id(a))

# Required Arguments

# def sum_list(items, items1):
#     sum_numbers = 0
#     for x in items:
#         sum_numbers += x
#         return sum_numbers

# lst = [1, 2, -8]
# print(sum_list(lst))

# Keyword Arguments

# def printinfo(name, age):
#     print("Name: ", name)
#     print("Age: ", age)
#     return

# printinfo( age= 50, name = "miki")

# Default Arguments

# def printinfo(name, age = 35):
#     print("Name: ", name)
#     print("Age: ", age)
#     return

# printinfo( age= 50, name = "miki")
# printinfo( name = "miki")

# Variable Arguments

def sum(*args):
    total = 0
    for i in args:
        total += i
    return total
