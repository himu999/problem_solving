t = int(input())

i = 1

while i <= t:

    string = input()
    list(string)
    length = len(string)

    c = ""

    for k in range(length-1, -1, -1):

        c += string[k]

    if c == string:
        print("Yes! It is Palindrome!")
    else:
        print("Sorry! It is not Palindrome!")

    i = i + 1
