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
            val = val + j + (a / j)

    if a == val:
        print("YES, {} is a perfect number!".format(a))
    else:
        print("NO, {} is not a perfect number!".format(a))

    i = i + 1
