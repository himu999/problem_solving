a = []
length = int(input())
first_element = int(input())
a.append(first_element)
"""
  when there is no elements in list means list is empty. a empty list can't be unsorted.
"""

message = "YES"

for i in range(1, length):
    b = int(input())
    a.append(b)

    if b < a[i-1]:
        message = "NO"

print(message)

