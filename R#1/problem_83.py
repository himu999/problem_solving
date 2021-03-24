t = int(input())

while t > 0:

    num = int(input())

    if 1 < num % 2 != 0:
        print("Not a power of 2")
    else:

        i = 0
        b = pow(2, i)
        while b <= num:

            if num == b:

                print("It's a power of 2")
                break
            else:
                i += 1
                b = pow(2, i)

        else:
            print("Not a power of 2")

    t -= 1
