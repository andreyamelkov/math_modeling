print("Введите делимое")
a=int(input())
print("Введите делитель")
b=int(input())
if b==0:
    print("Делитель равен 0")
    exit()
if a%b==0:
    print("Делится нацело")
else:
    aaaa=str("Не делится нацело,остаток раывен")
    print(aaaa , a%b)
    aaaa=str("Частное равно")
    print(aaaa, int(a/b))