import numpy 
n2=int(input("Введите 'высоту'))
n1=int(input("Вдите 'ширину':"))
m1=numpy.zeros (shape =(3,n1,n2))
for m in range(0,2,1):
 for i in range (0,n1,1):
     for n in range (0,n2,1):
         print ("Введите значение",i+1,"-го по высоте и ",n+1,"-го по ширине символа ", m,"-го массива",end='',sep='')
         m1[m,i,n]=input()
for (x1,x2,x3), value  in numpy.ndenumerate(m1):
    print(x1,x2,x3)
    
