t = int(input())

i = 1

while i <= t:

    num1, num2 = map(int, input().split())
    temp1 = num1
    temp2 = num2
    summation = 1

    j = 2
    while num1 >= 1 and num2 >= 1:

        if temp1 < j and temp2 < j:
            if num1 > 0 and num2 > 0 and num1 - num2 == 0:
                summation = summation * num1
                break
            elif num1 > 1 and num2 > 1:
                summation = num1 * num2 * summation
                break
            elif num1 > 1:
                summation = num1 * summation
                break
            elif num2 > 1:
                summation = num2 * summation
                break

        elif num1 % j == 0 or num2 % j == 0:

            summation = summation * j

            if num1 % j == 0 and num2 % j == 0:
                num1 = num1 / j
                num2 = num2 / j
                j = j + 1

            elif num1 % j == 0:
                num1 = num1 / j
                j = j + 1

            else:
                num2 = num2 / j
                j = j + 1

        else:
            j = j + 1

    print("LCM = {}".format(int(summation)))

    i = i + 1
