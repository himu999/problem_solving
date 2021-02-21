a = []
length = int(input())
""" when there is no elements in list means list is empty. a empty list can't be unsorted. """

message = "YES"

for i in range(length):
    b = int(input())
    a.append(b)

    if i > 0:
        if b < a[i - 1]:
            message = "NO"

print(message)
