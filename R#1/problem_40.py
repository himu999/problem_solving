t = int(input())

i = 1

while i <= t:

    summation = 0

    base, power = map(int, input().split())
    for k in range(power+1):
        summation = summation + pow(base, k)
    print("Result =", summation)

    i = i + 1
