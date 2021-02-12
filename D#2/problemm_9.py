import math

t = int(input())

i = 1

while i <= t:

    num = int(input())

    sqr = math.sqrt(num)

    if num % sqr == 0:

        print("YES")

    else:
        print("NO")

    i = i + 1
