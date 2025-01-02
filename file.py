a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if a2 < a1:
    a1, a2 = a2, a1
    b1, b2 = b2, b1

if b1 < a2:
    print('пустое множество')
elif b1 == a2:
    print(a2)
elif a1 <= a2 and b1 <= b2:
    print(a2, b1)
elif a1 <= a2 and b1 >= b2:
    print(a2, b2)