t = int(input())

i = 1

while i <= t:
    a, b, c = map(int, input().split())

    for k in range(1, c+1):

        if k % a == 0 and k % b == 0:

            print(k)
    if i < t:
       print()

    i = i + 1
