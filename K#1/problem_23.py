t = int(input())

i = 1

while i <= t:

    dictionary = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
        "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25,
        "Z": 26
    }

    string = input()
    a = list(string)

    for K in range(len(a)):

        if a[K] in dictionary:
            print(dictionary[a[K]], end="")
    print()

    i = i + 1

# n = int(input())
# l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for i in range(n):
#     st = input()
#     n_st = ''
#     for k in st:
#         n_st+= str(l.index(k)+1)
#     print(n_st)