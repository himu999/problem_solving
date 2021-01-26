k = 0
for i in range(1000, 0, -1):
    print(i, end="\t")
    k = k + 1
    if k % 5 == 0:
        print()
