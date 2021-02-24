
num = int(input())
b = []
t = 1
while t <= num:
    b.append(input())
    t = t+1


b.sort()

for k in range(len(b)):
    print(b[k])
