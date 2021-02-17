t = int(input())

i = 1
while i <= t:
    cnt = 0
    string = input()
    letter = input()

    list(string)

    for m in range(len(string)):
        if string[m] == letter:
            cnt = cnt + 1

    if cnt != 0:
        print("Occurrence of "+"'"+letter+"'"+" in "+"'"+string+"'"+" =", cnt)
        # print("Occurrence of \'{0}\' in \'{1}\' =".format(letter, string), cnt)
    else:
        print("'"+letter+"'"+" is not present")

    i = i + 1
