from cmath import sqrt

t = int(input())

i = 1

while i <= t:
    x1, y1 = map(float, input().split())
    r = float(input())
    x2, y2 = map(float, input().split())

    equation = pow((x2 - x1), 2) + pow((y2 - y1), 2)

    distance = sqrt(equation)

    if distance.real <= r:
        print("The point is inside the circle")
    else:
        print("The point is not inside the circle")

    i = i + 1

