x=int(input("x="))
y=int (input("y="))
z=int (input("z="))

if x+y<=z or x+z<=y or y+z<= x:
     print("Треугольник не существует")
elif x!=y and x!=z and y!=z :
    print("Разносторонний")
elif x==y==z:
    print("Равносторонний")
else:
    print("Равнобедренный")
    