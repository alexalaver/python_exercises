def func(x):
    return [-i if 2 <= y <= 7 else i for y, i in enumerate(x)]

a = [4, 2, 3, 4, 5, 6, 7, 8, 9]
print(func(a))