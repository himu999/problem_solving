from builtins import int

T = int(input())

i = 1
while i <= T:
    i = i + 1
    num = input()
    num_as_list = list(num)
    list_length = len(num_as_list)
    summation = int(num_as_list[0]) + int(num_as_list[list_length - 1])
    print("Sum =", summation)
    num_as_list.clear()
