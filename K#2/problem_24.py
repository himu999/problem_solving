t = int(input())

i = 1

while i <= t:
    a = []
    n = int(input())

    input_num = input()
    my_list = input_num.split(" ")
    list(my_list)

    b = len(my_list)

    for k in range(0, n, 2):
        if k < n - 2:
            print(my_list[k], end=" ")
        else:
            print(my_list[k])

    i = i + 1


# tt = int(input())
#
# while (tt):
#
#     n = int(input())
#     stri = input()
#     my_list = stri.split(' ')
#     ans_list = []
#
#     ans = ""
#     for i in range(0, n, 2):
#         if (i):
#             ans += ' '
#         ans += str(my_list[i])
#
#     print(ans)
#     tt -= 1