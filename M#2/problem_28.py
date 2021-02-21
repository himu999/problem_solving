a = []
n = int(input())
b = int(input())
a.append(b)
for j in range(1, n):
    c = int(input())
    a.append(c)

for m in range(1, len(a)):
    if a[m-1] > a[m]:
        print("NO")
        break
    elif m == len(a) - 1:
        print("YES")
if len(a) < 2:
    print("YES")

