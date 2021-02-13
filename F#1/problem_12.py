t = int(input())

i = 1

while i <= t:

    count = 0

    factorial = 1
    num = int(input())

    for k in range(1, num + 1, 1):
        factorial = factorial * k

    num_to_string = list(str(factorial))
    num_to_string.reverse()
    list1 = num_to_string.copy()

    length = len(list1)

    for k in range(length):
        if int(list1[k]) == 0:
            count = count + 1
        else:
            print(count)
            break

    i = i + 1
