t = int(input())

i = 1

while i <= t:

    a = input().split()
    list(a)
    ln = len(a)

    for k in range(ln):

        c = str(a[k])

        list(c)
        ln1 = len(c)
        for j in range(ln1-1, -1, -1):
            print(c[j], end="")

            if k < ln-1:
                if j == 0:
                    print(end=" ")
    print()

    i = i +1


