t = int(input())

i = 1

while i <= t:

    lower_bound, upper_bound = map(int, input().split())

    if lower_bound > upper_bound:
        print("Invalid!")
    else:
        for k in range(1, upper_bound+1):

            if k % lower_bound == 0:
                print(k)

    print()

    i = i + 1
