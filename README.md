# PythonCourse
def NodCalculation(a, b, NOD = None ):
    if a == 0 and b > 0:
        NOD = b
        return NOD
    elif b == 0 and a > 0:
        NOD = a
        return NOD
    elif b == 0 and a == 0:
        NOD = 0
        return NOD
    if a>b:
        n=a
    else:
        n=b
    for i in range(1,n):
        if (a % i == 0) and (b % i == 0):
            NOD = i

    return NOD


a = int(input('Ввод числа a: '))
b = int(input('Ввод числа b: '))

NOD=NodCalculation(a, b)

print(a, b, NOD)
