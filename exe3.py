divisible_num=[]
num1=int(input('Please enter integer number:', ))
for i in range(1,num1+1):
    if num1 % i == 0:
        divisible_num.append(i)
#print(divisible_num)
if len(divisible_num)==2:
    print("%s is a prime number"% num1)
else:
    print("%s is NOT prime number" % num1)

