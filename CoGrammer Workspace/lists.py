fruits = ['apple','banana','orange']
fruits.extend(['grape','pineapple'])
print(fruits)


#print(len(fruits))
fruits.insert(3,'blueberry')
print(fruits)
#changing a range of items
fruits[1:3] = ['kiwi','strawberry']
print(fruits)

fruits_tuple = ("cherry","grandadilla")
fruits.extend(fruits_tuple)
print(fruits)

print(type(fruits), type(fruits_tuple))

#Removing
removed_item = fruits.pop(2)
print(removed_item)

fruits.remove("banana")
