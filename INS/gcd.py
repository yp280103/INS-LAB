num1 = int(input("enter the num1: "))
num2 = int(input("enter the num2: "))
l1 = []
l2 = []
for i in range(1,num1+1):
    if num1 % i == 0:
        l1.append(i)
for i in range(1,num2+1):
    if num2 % i == 0:
        l2.append(i)
print(num1 , "=" , l1)
print(num2 , "=" , l2)

for i in l1:
    for j in l2:
        if i == j:
            max_num = i 
print(max_num)