num = int(input())

n1, n2 = 0, 1
count = 0

if num == 1:
    print(n1)
else:
    while count < num:
        result = n1 + n2
        n1 = n2
        n2 = result
        count += 1

print(n1)
