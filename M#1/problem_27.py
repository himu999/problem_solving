t = int(input())
i = 1

while i <= t:

    summation = 0
    num = input()
    c = int(num)
    list(num)

    b = len(num)

    for m in range(b):

        summation = summation + pow(int(num[m]), b)

    if c == summation:
        print(c, "is an armstrong number!")
    else:
        print(c, "is not an armstrong number!")

    i = i + 1
