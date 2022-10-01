# All operations tha can be performed on list

fruit_names = ["Apple", "Banana", "Orange", "Papaya", "Grapes"]

new_fruit = "WaterMelon"

# Operations on list

#1 append

fruit_names.append(new_fruit)

#2 extend

fruit_names.extend(["Pineapple", "MuskMelon"])

#3 Insert

fruit_names.insert(0,"Guava")

#4 remove 

fruit_names.remove("Guava")

#5 Pop

fruit = fruit_names.pop()
print(fruit)

#6 clear
fruit_names.clear()

#extending again
fruit_names.extend(["Apple", "Banana", "Orange", "Papaya", "Grapes"])

#7 index
print("Apple fruit is at index value ",fruit_names.index("Apple"))

#8 count
print("Total times Apple in list is ", fruit_names.count("Apple"))

#9 sort
fruit_names.sort()

#10 reverse 
fruit_names.reverse()

#11 copy

fruit_list_copy = fruit_names.copy()