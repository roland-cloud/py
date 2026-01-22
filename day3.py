
print(1>3) #false coz 1 is less than 3
print(1<3) #true coz o
print(1 == 1)  #equal to?
print("1" == 1)
print(3 == len("job"))
print(True == True)

# ==
print (len('mango') == len('avocado')) #false mango has less letters than avocado


# is
print('1 is 1', '1 is 1') #true coz 1 is 1
print('1 is not 2', '1 is not 2') #false coz 1 is not 2


#in keyword
print('A in group' , 'A' in 'group') #false coz letter A is not found in word group
print ("R in Roland" , "R" in "Roland") # true coz we found letter R in word Roland


#logical operators
#they all have to match if one if true and one is false = they wont satisfy the ans will be false
print (3 > 2 and 4 > 3)
print (3 > 2 and 4 < 3)


#strings : anything under " " or ' '
letter ="P"
print (letter)
print(len(letter)) # one only -p
greeting = "hello, john"
print(greeting)

#multiline_string
multiple_string= """"

hey big man what is your name ? my name is roland aselamushine nomicos i am  Congolese by nationaloity
and i am 23 years old age
"""
print(multiple_string)


#String concatenation
first_name = "roland"
last_name = "nomicos"
space = "-" #space in your stucked words
full_name = first_name + space +last_name
print(full_name)


#escape sequences in strings
print ("hello.\nhow are you doing")  #it writte for you hello. how are you doing with a break line
print ("hello.\thow are you doing") #it writte for you hello. how are you doing with a space
print ("hello.\\how are you doing") #it writte for you hello. how are you doing with \
print ('hello.how are you doing\'s, this is roland laptop') #it writte with apostrophy


#%s : is used for letters
#%d : is used for digits 
#it helps you put together your word (sentence)
first_name = "roland"
last_name = "nomicos"
age = 20
skill = "python"
location = "i live in uganda"
formatted_string = " I am %s %s, I am %d years old, I am learning %s , %s " %(first_name, last_name,age, skill, location)
print (formatted_string)


#multiple strings in []
python_libraries = ['Django','Flask','Numpy']
formatted_string = 'the following are python libraries:%s' %(python_libraries)
print(formatted_string)
#
first_name = "roland"
last_name = "nomicos"
language ='python'
formatted_string = 'I am {} {}. i teach {}' .format(first_name, last_name, language)
print(formatted_string)


#CALCULATOR
a = int(input("Enter a number:"))
b = int(input("Enter an other number:"))

print('{} + {} = {}' .format(a, b, a + b))
print('{} - {} = {}' .format(a, b, a - b))
print('{} * {} = {}' .format(a, b, a * b))
print ('{} / {} = {:.2f}' .format(a, b, a / b)) #limit it to two
#:.2f : reduce the number of decimal 
print('{} % {} = {}' .format(a, b, a % b))
print('{} // {} = {}' .format(a, b, a // b))
print('{} **{} = {}' .format(a, b, a ** b))

#
x, y, z= 1, 2, 3
print(x,y,z)

#accessing characters in a string by index
#PYTHON
#012345
lang = 'python'
first_letter = lang[0]
print(first_letter)


#counting indexing
print(lang[3]) #print H coz its on L3
print(lang[-1]) #helps us to print the last variable
print(lang[0-3]) #print PYT only
print(lang[-3:]) #print last three words
print(lang[0:6:2]) #Put 6coz we ignore the last char



#METHODS

#string methods in python
challenge = 'thirty days of python'  #only first letter
print(challenge.capitalize())

challenge = 'THIRTY DAYS OF PYTHON'   #lower
print(challenge.lower())

challenge = 'thirty days of python'  #capital
print(challenge.upper())

challenge = 'thirty days of python'
print(challenge.count('t')) #means it will count how many letter 't' i have in my doc

#chceck if your last words is ended with ...
challenge = 'thirty days of python'
print(challenge.endswith('on'))  #true
print(challenge.endswith('tion')) #false coz our sentence has not ended with 'tion'

#find in which index y is 
challenge = 'thirty days of python'
print(challenge.find('y'))  #5
print(challenge.find('y')) #8

#replace methode (to replace word )
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) #replace python by coding


#split
fruits = "banana orange apple peach"
print (fruits)
finish_sentence = fruits.split()
print (fruits)
# split fruits under '' value


