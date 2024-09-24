#Fullname and age
fname = "Xylyn Jriel"
lname = "Corpuz"
age= 18

fullname = fname + " " + lname

#Hello my name is...
print("Hello, my name is", fullname + ".", "I am", str(age), "years old.")

#Convert to uppercase if else
if fullname.isupper ():
    print(fullname)
    
else:
    new_fullname = fullname.upper ()
    print(new_fullname)
