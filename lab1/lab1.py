from math import *

def num1():
    x = int(input("Input x: "))
    y = int(input("Input y: "))
    z = int(input("Input z: "))

    a = abs(5-2*e)/((1+x**2)*(y - tan(z)))
    b = abs(y-4)+((y-x)**2)/6+((x-y)**2)/7

    print("a = ", a)
    print("b = ", b)

def num2():
    a = 2
    b = -1
    h = 0.15
    x = 4.0
    while (x < 5.5):
        f = a*((x**b+x)/3-x**(3/4))
        print("f(",x,")= ", f)
        x += h

def num3():
    h = 0.01
    x = 1
    while (x < 3):
        print("f(", x, ") = ", sqrt(log(cos(sqrt(x)))))
        x += h

def num4():
    x = []
    y = []
    for i in range(3):
        x.append(float(input(f"Input x {i+1}: ")))
        y.append(float(input(f"Input y {i+1}: ")))
    s1 = sqrt((x[1] - x[0])**2 + (y[1] - y[0])**2)
    s2 = sqrt((x[2] - x[1])**2 + (y[2] - y[1])**2)
    s3 = sqrt((x[0] - x[2])**2 + (y[0] - y[2])**2)
    p = s1 + s2 + s3
    s = p / 2
    s = sqrt(s * (s - s1) * (s - s2) * (s - s3))
    print("p = :", p)
    print("S = :", s)


def num5():
    v1 = float(input())
    v2 = float(input())
    s1 = float(input())
    t = float(input())
    s2 = (v1+v2)*t
    print("S = ", s1 + s2)


def num6():
    try:
        a = int(input("Input a>=1: "))
        b = int(input("Input b<=100: "))
        if ((a >= 1) or (b <= 100)):
            print("a^2+b^2 = ", a ** 2 + b ** 2)
            print("a^2-b^2 = ", a ** 2 - b ** 2,)
            print("a^2/b^2 = ", round((a ** 2) / (b ** 2), 3),)
            print("a^2*b^2 = ", (a ** 2) * (b ** 2),)
        else:
            print("Uncorrect nuber")
    except ValueError:
        print("Uncorrect simbol")


def num7():
    try:
        x = int(input("Input -10 <= x <= 10: "))
        if (-10 <= x <= 10):
            print("y = ", 3*x**6-6*x**2-7)
        else:
            print("Uncorrect nuber")
    except ValueError:
        print("Uncorrect simbol")

def num8():
    try:
        a = []
        b = []
        c = []
        for i in range(2):
            a.append(float(input(f"Input A {i + 1}: ")))
            b.append(float(input(f"Input B {i + 1}: ")))
            c.append(float(input(f"Input C {i + 1}: ")))
        if all(-10 <= lim <= 10 for lim in a + b + c):
            d = a[0] * b[1] - a[1] * b[0]
            x = (c[0] * b[1] - c[1] * b[0])/d
            y = (a[0] * c[1] - a[1] * c[0])/d
            print("x = ", round(x, 4))
            print("y = ", round(y, 4))
        else:
            print("Uncorrect nuber")
    except ValueError:
        print("Uncorrect simbol")

def num9():
    Davidov = 60000
    Petrov = 90000
    Maximov = 150000
    profite = 117000

    invests = Davidov + Petrov + Maximov
    shareDavid = Davidov / invests
    sharePetr = Petrov / invests
    shareMaxim = Maximov / invests

    print("Davidov share ", profite*shareDavid)
    print("Petrov share ", profite*sharePetr)
    print("Maximov share ", profite*shareMaxim)

while True:
    try:
        choice = int(input("Input number of ex 1-9, to exit 0:"))
        if choice == 0:
            break
        elif choice in range(1,10):
            number = globals()[f'num{choice}']
            number()
        else:
            print("Uncorrect nuber")
    except ValueError:
        print("Uncorrect simbol")