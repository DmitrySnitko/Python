import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

D = (b ** 2) - 4*a*c
print("Дискриминант:",D)

if D > 0:
    print("Первый корень уравнения:",int((-b + D ** 0.5) / (2 * a)))
    print("Второй корень уравнения:",int((-b - D ** 0.5) / (2 * a)))
elif D == 0:
    print("Первый корень уравнения:",int(-b / (2 * a)))
    print("Второй корень уравнения:",int(-b / (2 * a)))
else:
    print("Первый корень уравнения:",complex(-b, abs(D) ** 0.5 / (2 * a)))
    print("Второй корень уравнения:",complex(-b, -(abs(D) ** 0.5 / (2 * a))))