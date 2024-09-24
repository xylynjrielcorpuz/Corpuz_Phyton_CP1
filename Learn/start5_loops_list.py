#while loops

i = 1
while i <= 2:
    print(i)
    i = i + 1

i = 2
while i <= 3:
    print(i * '*')
    i = i + 1

#lists
course = ["BSIT", "BSCS", "BSCompEn", "BSLIS"]
course [-2]= "BSCompEng"
print(course[-1]) #index
print(course)
print(course[0:3]) #does not include the last index

#list methods

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.insert (2, 3)
numbers.remove(3)
# numbers.clear() --doesn't expect any values
print(1 in numbers) #bolean operator
print(len(numbers)) #how many items in the list