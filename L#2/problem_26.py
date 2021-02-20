t = int(input())

i = 1

while i <= t:

    cont = 0

    num = float(input())

    while num > 1:
        num = num / 2
        cont = cont + 1

    print(cont, "days")

    i = i + 1
