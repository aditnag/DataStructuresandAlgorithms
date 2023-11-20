def foo():
    try:
        print(1)
    finally:
        print(2)


foo()

print("2******************************************************************")


def foo():
    try:
        return 1
    finally:
        return 2


k = foo()
print(k)

print("3******************************************************************")
print()
# try:
#     if '1' != 1:
#         raise "someError"
#     else:
#         print("someError has not occurred")
# except "someError":
#     print("someError has occurred")

print("4******************************************************************")
print()
# assert False, 'Spanish'

print("5******************************************************************")

x = 10
y = 8
assert x > y, 'X too small'

print("6******************************************************************")


def f(x):
    yield x + 1
    print("test")
    yield x + 2


g = f(9)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

print("7*****************************************************************")

# a = False
# while not a:
#     try:
#         f_n = input("Enter file name")
#         i_f = open(f_n, 'r')
#     except:
#         print("Input file not found")

print("8*****************************************************************")

a = "2 ** 3 + 5 ** 2"
print(a)

print("8*****************************************************************")


def multipliers():
    return [lambda x: i * x for i in range(4)]


print([m(2) for m in multipliers()])
