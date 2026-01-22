#lists

fruit = ['banana','orange', 'mango']
print (fruit)

#list()function
#it is used to create a list
empty_list=list()
print(empty_list)

#list is a collection where you can change a name 
friut=['banana', 'orange', 'mango']
vegetables = ['tomato', 'cabbage', 'onion', 'carot']

#print the list and its length
print('fruit:', fruit)
print ('number of fruit:' , len(fruit))


name = "john"
print(name[0:3])
print(fruit[-1])


#slicing a list
fruit = ['banana', 'orange', 'mango']
print(fruit[1:3])
print(fruit[0:2])

web_tech= ['html', 'css', 'js', 'redux', 'node', 'mongo', 'mongoDB']
print(web_tech[2:5]) # it will print js, redux, node
print(web_tech[0:7:2])# the last two helps us to skip x2

web_tech[0]= "PHP" #we replace  html (the first index to PHP)
print(web_tech)


web_tech2= ['html', 'css', 'js', 'redux', 'node', 'mongo', 'mongoDB']
print(len(web_tech2) -1) #print the ........index

#check items in a list if its true or faulse
#list of fruit
fruit1=['mango', 'avocado', 'pineapple', 'watermelon', 'coco']
print(fruit1.index("mango"))
print('mango' in fruit1)
print(fruit1)


#add one element on your list
#append
fruit1.append("papaya")
print(fruit1)


#pop is used to remove the last item
fruit1.pop()
print(fruit1)

#delete it helps you to delete a lot of items 
fruit1=['mango', 'avocado', 'pineapple', 'watermelon', 'coco']
del fruit1[0:2]
print(fruit1)


#clear: delete all
fruit1=['mango', 'avocado', 'pineapple', 'watermelon', 'coco']
fruit1.clear()

#copy
fruit1=['mango', 'avocado', 'pineapple', 'watermelon', 'coco']
fruit1_copy = fruit1.copy()
print(fruit1_copy)

#join a list with +
fruit4=['mango', 'avocado', 'pineapple', 'watermelon', 'coco']
fruit5=['cpu', 'pc', 'php']
f_fruit= fruit4 + fruit5
print(f_fruit)

#extend
#syntax
lst = ['item1', 'item2']
lst2 =['item3', 'item4']
lst3 =['item5', 'item6']
lst.extend(lst2)
print(lst)

#count
#syntax
lst = ['item1', 'item2', 'item1']
print(lst.count('item1'))

#reverse: it reverses the order
name = ['r', 'o', 'l', 'a', 'n', 'd']
name.reverse()
print(name)


#sorting list items(ascendently)
school = [22, 23, 29, 24,19, 25, 26, 28]
school.sort()
print(school)


#reverse descendetly
school = [22, 23, 29, 24,19, 25, 26, 28]
school.sort(reverse=True)
print(school)



