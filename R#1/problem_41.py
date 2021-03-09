t = int(input())

i = 1

while i <= t:
    n = int(input())

    summation = 1

    for j in range(2, n+1):
        temp = 1
        for k in range(1, j + 1):
            temp = temp * k

        summation += (j / temp)

    print("{:.4f}".format(summation))
    i = i + 1
