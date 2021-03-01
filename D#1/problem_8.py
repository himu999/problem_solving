t = int(input())

i = 1

while i <= t:

    s = map(int, input().split())
    b = list(s)

    b.sort()
    c = len(b)

    print("Case {}:".format(i), end=" ")

    for j in range(c):
        if j == c - 1:
            print(b[j])
        else:
            print(b[j], end=" ")

    i = i + 1
