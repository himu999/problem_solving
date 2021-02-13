t = int(input())
i = 1
factorial = 1
while i <= t:

    num = int(input())

    for k in range(1, num+1, 1):
        factorial = factorial * k

    print(factorial)
    factorial = 1

    i = i + 1
