T = int(input())
i = 1

while i <= T:

    a = int(input())
    for k in range(1, a + 1, 1):

        for j in range(1, a + 1, 1):
            print(end="*")

        print()

    if i == T:
        break
    else:
        print()

    i = i + 1
