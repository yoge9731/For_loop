# For Loops

#1
cities = ["Bengalore", "Mysore", "Hubballi", "Mangaluru"]
for city in cities:
    print(city)

#2
for i in range(1,11):
    print(i)

#3
for i in range(1,11):
    print(i, end=" ")

#4
bag = ["red", "green", "blue"]
for ball in bag:
    print(ball)

#5
for i in range(1, 11, 3):
    print(i)

#6
name="yoge"
for letter in name:
    print(letter)

#7
name="chandan"
for letter in name:
    print(letter*2)

#8
name = "chandan"
for index, x in enumerate(name):
    print(x*(index+1))

#9
l=[12, 23, 55, 66, 36]
for index, i in enumerate(l):
    print(f"{i} is in {index}th index")

#10
for i in range(1,6):
    for j in range(1,6):
        print(f"{i}x{j} = {i*j}")
    print( )

# using break statement
cities = ["Bengalore", "Mysore", "Hubballi", "Mangaluru"]
for city in cities:
    if city=="Hubballi":
        print(f"Found {city} !")
        break
    print( )
        
# continue
cities = ["Bengalore", "Mysore", "Hubballi", "Mangaluru"]
for city in cities:
    if city=="Hubballi":
        continue
    print(city)

# enumarate
cities = ["Bengalore", "Mysore", "Hubballi", "Mangaluru"]
for index, city in enumerate(cities):
    print(f"city {index + 1}: {city}")

# else with for loop
for city in cities:
    print(city)
else:
    print('no more city!')

l=[1,2,3,4,5,6,7,8,9,10]
for num in l:
    print(num)
else:
    print("all printed")

p=[1,2,3,4,5,6,7,8,9,10]
for i in p:
    print(i)
    if i==6:
        break
else:
    print("all printed")   

d={"name":"yogee", "age":30}
for key, values in d.items( ):
    print(key," ",values)

for i in range(1,11):
    print(f" 2 x {i} = {2*i}")

for i in range(2,11):
    for j in range(1,11):
        print(i, "_", j)

for i in range(2,11):
    for j in range(1,11):
        print(f" {i} x {j} = {i*j}")
