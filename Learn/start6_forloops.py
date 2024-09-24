# for loops

grades = [85, 86, 87, 88, 89, 90]

for item in grades: #can iterate all items in the grades list
    print(item)


i = 0
while i < len(grades):
    print(grades[i])
    i = i + 1


#range fuction --- generate  a sequence of number

mygrades = range(75, 101, 3) #starting value, excluded ending , step per increment
for grade in mygrades:
    print(grade)


#tuples --immutable/ cannot be changes once created

number = (1, 2, 3) #does not support re-assignments 