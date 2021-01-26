T = int(input())
i = 1

while i <= T:

    i = i+1
    num = int(input())

    if num < 0:
        break
    else:
        if num % 2 == 0:
            print("even")
        else:
            print("odd")
