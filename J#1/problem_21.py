t = int(input())

i = 1

while i <= t:

    string = input()
    list(string)

    for j in range(len(string)-1, -1, -1):

        print(string[j], end="")
    print()

    i = i + 1
