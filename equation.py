import math as m

a = float(input("Ввод числа a: "))
b = float(input("Ввод числа b: "))
c = float(input("Ввод числа c: "))

if a == 0 and b != 0 and c != 0:
    x = -c/b
    print(x)
elif a != 0 and b == 0 and c != 0:
    if c < 0:
        x = m.sqrt(-c/a)
        print(x)
elif a != 0 and b != 0 and c == 0:
    x = 0
    x2= -b/a
    print(x,x2)
elif a != 0 and b != 0 and c != 0:
    D = b*b - 4*a*c
    if D>0:
        x = (-b + m.sqrt(D))/(2*a)
        x2 = (-b - m.sqrt(D))/(2*a)
        print(x,x2)
    elif D == 0:
        x = -b/(2*a)
        print(x)
else:
    x = 0
    print(x)
