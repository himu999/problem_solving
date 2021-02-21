t = int(input())

i = 1

while i <= t:
    a = input()
    b = ord(a)

    if 48 <= b <= 57:
        print("Numerical Digit")
    elif 65 <= b <= 90:
        print("Uppercase Character")
    elif 97 <= b <= 122:
        print("Lowercase Character")
    else:
        print("Special Character")

    i = i + 1
