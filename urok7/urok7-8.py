n=int(input("Введите количество чисел в последовательности: "))
c=int(input("Введите первое число последовательности"))
max=c
min=c
for i in range (n-1):

    b=int (input())
    if b> max:
        max=b
    if b<min:
        min=b
print (max)
print (min)
