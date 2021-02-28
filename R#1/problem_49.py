import cmath
t = int(input())

i = 1

b = "is not a prime"
c = "is a prime"

while i <= t:

    a = int(input())
    d = cmath.sqrt(a)
    d = int(d.real)

    if a > 2 and a % 2 == 0:
        print(a, b)
        i = i + 1
        continue

    else:
        for k in range(3, d + 1, 2):

            if a == 2:
                print(a, c)
                break
            elif a % k == 0:
                print(a, b)
                break
        else:
            print(a, c)

    i = i + 1
