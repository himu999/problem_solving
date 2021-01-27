T = int(input())

k = 1

while k <= T:

    num = int(input())
    print("Case", k, end=":")
    for i in range(1, num + 1, 1):

        if num % i == 0:
            print(end=" ")
            print(i, end="")

    k = k + 1
    print()
