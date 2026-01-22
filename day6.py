student_name = input("what is your name: ")
score = int(input("what is your score"))


print(student_name)
print(score)
print(type(student_name))
print(type(score))

#if condition
if score < 50:       
    print(f"{student_name}, you have failed")
else: 
    print(f"{student_name}, you have passed")
    
    if score > 80:
            print(f"{student_name},  excellent")
            
           
#to know if a number is paire ou impaire  
#number = int(int("enter a number"))
#if number % 2 ==0:
# print(f"{number} is an even number")
#else:
# #print(f"{number} is an odd number")
         
              
            
            # to know if a number is positif ou negatif
    a = int(input("enter a num"))
    if a < 0:
        print('A is negative')
    elif a == 0:
        print('A is zero')
    else:
        print('A is a positive number')
        
        #elif:independant of if
        
        #exercise calculate in terms or grade
        
        percentage_score = float(input("enter your percentage score"))
        
        if percentage_score <= 100 and percentage_score >= 80:
            print('Grade A')
        elif percentage_score <=79 and percentage_score >=70:
            print('Grade B')
        elif percentage_score <=69 and percentage_score >=60:
            print('Grade C')
        elif percentage_score <=59 and percentage_score >=50:
            print('Grade D')
        else:
            print('E')
            
            
            #the second way
        #percentage_score >=90:
        #print('A')
        #elif percentage_score >=80:
        #print('B')
        #elif percentage_score >=70:
        #print('C')
        #elif percentage_score >=60:
        #print('D')
        #elif percentage_score >=50:
        # print('E')
        #elif percentage_score >=40:
        #print('Failed')
        #else:
        #print('invalid')
            
    #count
    count = 0
while count < 10:
    print(count)
    count += 1
    print("good bye")
else:
    print("count is no longer than 10")

                

    