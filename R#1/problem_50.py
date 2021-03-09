t = int(input())

j = 1

while j <= t:

    string = input()
    a = list(string)

    for i in range(len(string)):

        if a[i] == "L":
            a[i] = a[i-1]

        elif a[i] == "R":
            a[i] = a[i+1]

    for k in range(len(a)):
        print(a[k], end="")
    else:
        print()

    j = j + 1
