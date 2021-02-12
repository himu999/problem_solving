import math
t = int(input())
i = 1
while i <= t:

    num = int(input())

    k = math.sqrt(num)
    difference = k - int(k)

    if difference > 0:
        print("NO")
    else:
        print("YES")

    i = i + 1



