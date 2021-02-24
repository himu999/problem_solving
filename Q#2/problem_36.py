t = int(input())

i = 1

while i <= t:

    number = int(input())
    c = str(number)
    d = len(c)
    e = ""

    for k in range(d - 1, -1, -1):
        e += c[k]

    print(int(e))

    i = i + 1
