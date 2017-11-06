import math
import time


R_0 = 100
a = 3.9083 * (10**(-3))
b = -5.775 * (10**(-7))

def space():
    print()
    print()

def main():
    space()
    R = float(input("R = "))
    space()
    t = ((((-R_0)*a) + math.sqrt((R_0 ** 2) * (a ** 2) - 4 * R_0 * b * (R_0 - R))) / (2 * R_0 * b))
    space()
    if(t == -0.0):
        print("t = 0 C")
    else:
        print("t =",t,"C")
    x = input("")
    main()

main()


R = result

t = ((((-R_0)*a) + math.sqrt((R_0 ** 2) * (a ** 2) - 4 * R_0 * b * (R_0 - R))) / (2 * R_0 * b))

print(t)
x = input("")
