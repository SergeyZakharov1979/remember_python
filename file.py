a, b, oper = int(input()), int(input()), input()

if oper == "+":
    print(a + b)
elif oper == "-":
    print(a - b)
elif oper == "*":
    print(a * b)
elif oper == "/":
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        print(a / b)
else:
    print('Неверная операция')
