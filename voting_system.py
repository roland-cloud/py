 
 
 
age = int(input("Enter your age: "))
if age <= 1:
    print("You're an infant")
elif age >= 2 and age <= 12:
    print("You're a child")
elif age >= 13 and age <= 17:
    print("You're a teenager")
elif age >= 18 and age <= 79:
    print("You're an adult")
    
    nationality = input("Enter your nationality: ")    
    if nationality == "ugandan" or nationality == "kenya" or nationality == "rwandese":
        print("You can vote")
    else:
        print("You can not vote") 
    
elif age > 120:
    print("Invalid age")
else:
    print("Invalid age")