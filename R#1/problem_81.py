t = int(input())

while t > 0:

    # a = int(input())
    summ = 0
    b = map(int, input().split())
    b = list(b)
    cont = 0

    for i in range(1, len(b)):

        summ += b[i]

    summ = int(summ / b[0])

    for j in range(1, len(b)):
        if b[j] > summ:
            cont += 1
    rate = (cont*100) / (len(b)-1)

    print("{:.3f}".format(rate)+"%")

    t -= 1
