t = int(input())
i = 1

while i <= t:
    a = input()
    list(a)

    vowel = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    v_count = []
    c_count = []

    for j in range(len(a)):
        if a[j].isalpha():

            if a[j] in vowel:
                v_count.append(a[j])
            else:
                c_count.append(a[j])
    for m in range(len(v_count)):
        print(v_count[m], end="")
    print()

    for n in range(len(c_count)):
        print(c_count[n], end="")
    print()

    i = i + 1
