t = int(input())

i = 1

while i <= t:

    num = int(input())

    if num >= 2:

        for k in range(num, -1, -1):

            if k >= 2:
                print("2^{}".format(k), end=" + ")
            else:
                if k > 0:
                    print("2", end=" + ")
                else:
                    print("1")
    else:
        for j in range(num, -1, -1):
            if j > 0:
                print("2", end=" + ")
            else:
                print("1")

    i = i + 1
