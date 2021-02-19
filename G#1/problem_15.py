t = int(input())

i = 1

while i <= t:

    b = []

    string = input()
    a = list(string)
    a.sort()
    small_letter = "abcdefghijklmnopqrstuvwxyz"

    for j in range(len(a)):
        cont = 0

        for k in range(0, len(a)):

            if a[j] in small_letter:
                if a[j] == a[k]:
                    cont = cont + 1

        if a[j] in small_letter:
            if a[j] not in b:
                print(a[j], "=", cont)
                b.append(a[j])
    if i < t:
        print()

    i = i + 1
