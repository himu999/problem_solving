t = int(input())

i = 1

while i <= t:

    a, b, c = map(int, input().split())

    while a <= b:
        if a % c == 0:
            print(a)
            a = a + c
        else:
            a = a + 1

    print()

    i = i + 1
