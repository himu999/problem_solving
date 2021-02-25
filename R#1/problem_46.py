import cmath
t = int(input())

i = 1

while i <= t:
    a, b, c = map(int, input().split())
    s = (a + b + c) / 2
    area = cmath.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Area = {:.3f}".format(area.real))

    i = i + 1
