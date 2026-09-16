
# Python Assignment 01 - Part 2: Student Information Management 

#-------------Student Information Manager------------
print("\n-------------Student Information Manager------------")

name = "John Legend"           #string
age = 35                       #integer
height = 1.75                  #float
is_currently_enrolled = True   #boolean

print("\nString  => Student Name:", name)
print("\nInteger => Age:", age)
print("\nFloat   => Height:", height)
print("\nBoolean => Is Currently Enrolled:", is_currently_enrolled)


#-------------Question 1 - Creating Lists------------
print("\n-------------Question 1 - Creating Lists------------")

Skills = ["Python","Java","C++","JavaScript","SQL","HTML"] 
print("\nSkills = ", Skills)

print("\nFirst Skill: ",Skills[0])

Skills.append("React")
print("\nList after adding a new skill: ", Skills)

Skills.remove("JavaScript")
print("\nUpdated List: ", Skills)


#-------------Question 2 - Creating Tuples---------------------
print("\n-------------Question 2 - Creating Tuples------------")

favorite_numbers = (6, 14, 30)
print("\nFavorite numbers = ",favorite_numbers)
print("\nSecond number of the tuple: ",favorite_numbers[1])

#-------------Question 3 - Creating Sets---------------------
print("\n-------------Question 3 - Creating Sets------------")

Hobbies = {"music","reading","swimming","music","cooking","traveling","music"}

print("\nHobbies = ",Hobbies)
print("\nA set contains only unique values, so the value 'music' doesn't repeat in the set over and over again.")
Hobbies.add("cycling")
print("\nHobbies = ",Hobbies)


#-------------Question 4 - Creating Dictionary---------------------
print("\n-------------Question 4 - Creating Dictionary------------")

Student_info = {"Name": name, "Age": age, "Height": height, "Is_currently_enrolled": is_currently_enrolled, "Skills": Skills,"Favorite_numbers": favorite_numbers, "Hobbies": Hobbies}

#Qs.4.1 - Print the student's name.  
print("\nQs.4.1")
print("Student Name:", Student_info["Name"])

#Qs.4.2 - Print their skills.
print("\nQs.4.2")
print("Student's Skills = ", Student_info["Skills"])

#Qs.4.3 - Add a new key called "country". 
print("\nQs.4.3")
Student_info["Country"] = "Sri Lanka"
print("After adding country: ", Student_info)

#Qs.4.4 - Update the student's age. 
print("\nQs.4.4")
Student_info["Age"] = 48
print("After changing age: ", Student_info)

#Qs.4.5 - Print the complete dictionary. 
print("\nQs.4.5")
print("Final Dictionary: ",Student_info)


#-----------Bonus Challenge-------------------------
print("\n-----------Bonus Challenge--------------")

my_name = "Milasha Subasinghe"
my_age = 25
my_fav_programming_lang = "Python"

my_info = {"name":my_name,"age":my_age,"fav_programming_lang":my_fav_programming_lang}

print("\nHellooo {} !!!".format(my_info["name"]))

print("\nYou're {} years old! Cool!".format(my_info["age"]))

print("\nAnd your favorite programming language is {} Awesome!".format(my_info["fav_programming_lang"]))


#----------------Differencess between List, Tuple, Set and Dictionary----------------
print("\n----------------Differencess between List, Tuple, Set and Dictionary----------------")

print("\nList")
print("A List stores multiple values and it keeps them in order. It's mutable, which means the values can be modified after created. Lists store duplicate values. Stored values are accessed using indexing starting from 0th position.")

print("\nTuple")
print("Tuples also store multiple values and they keep them in order. But Tuples are immutable, which means the values cannot be modified after created. Tuples store duplicate values. Stored values are accessed using indexing.")

print("\nSet")
print("A Set stores multiple values but it doesn't keep them in order. It's mutable, which means the values can be modified after created. New values can be added and existing values can be removed. Sets store only unique values, so duplicate values are automatically removed. Stored values are accessed using iteration.")

print("\nDictionary")
print("A Dictionary stores multiple values in key-value pairs. It's mutable, which means the values can be modified after created. Dictionaries store unique keys, but the values can be duplicated. Stored values are accessed using their keys.")