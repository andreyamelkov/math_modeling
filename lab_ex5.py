for a in range(2,int(input('input number:'))):
    b = 0
    for c in range(1,a):
        if a%c == 0:
            b += c
    if b == a:
        print(a)