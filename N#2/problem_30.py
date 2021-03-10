import cmath as c
t = int(input())

i = 1

while i <= t:

    a = int(input())
    b = c.sqrt(a)
    m = int(b.real)
    val = 1

    for j in range(2, m+1):

        if a % j == 0:
            val = val + j + (a/j)

    if a == val:
        print("YES, {} is a perfect number!".format(a))
    else:
        print("NO, {} is not a perfect number!".format(a))

    i = i + 1








# T = int(input())
# while T > 0:
#     n = int(input())
#     result = 1
#     m = int(n**0.5)
#     for i in range(2,m + 1):
#         if n % i == 0:
#                 result =result + i + (n/i)
#     if result == n:
#         print("YES, {} is a perfect number!".format(n))
#     else:
#         print("NO, {} is not a perfect number!".format(n))
#     T -= 1