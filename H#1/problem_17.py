t = int(input())

i = 1

while i <= t:

    vowel = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    cont = 0
    line = input()
    list(line)

    for j in range(len(line)):

        if line[j] in vowel:
            cont = cont + 1

    print("Number of vowels " + "=", cont)

    i = i + 1
