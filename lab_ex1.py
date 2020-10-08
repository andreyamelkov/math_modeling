print("ax**2 + bx + c = 0:")
print("Введите коэфиценты для уравнения")
a=float(input("a="))
b=float(input("b="))
c=float(input("b=")) 


D=b**2-(4*a*c)
print("Дескреминант равен:",D)


if D>0:
    x1=(-b+(D**1/2)/(2*a))
    x2=(-b-(D**1/2)/(2*a))
    print("x1=",x1)
    print("x2=",x2)
elif D==0:
    x=-b/(2*a)
    print ("x=",x)
else:
    print("Уравнение не имеент значения")