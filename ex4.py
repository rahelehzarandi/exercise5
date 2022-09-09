city_name=[]
print("Enter 5 city mane:")
for i in range(0,5):
    name=input()
    city_name.append(name)
#print(city_name)
count=0
i=1
for count in city_name:
    print(f" city {i} is: {count}")
    i=i+1
