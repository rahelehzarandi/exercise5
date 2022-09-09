num1=0
num_list=[]
while num1 != '':
    num1=input("Enter numbers:", )
    if num1 != '':
         num_list.append(int(num1))
#for i in range(0,len(num_list)):
    #num_list[i] = int( num_list[i])
num_list.sort(reverse= True)
print("the greatest numbers are :",num_list[0:5])


