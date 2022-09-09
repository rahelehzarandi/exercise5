import random
dicelist =[]
i=1
count=int(input("Enter the dice roll count:", ))
for i in range(count):
    dice=random.randint(1,6)
    dicelist.append(dice)
print(dicelist)
sumroll=sum(dicelist)
print("%i is sum of the roll"%sumroll)