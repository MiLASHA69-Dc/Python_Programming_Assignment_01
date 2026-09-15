'''Assignment: Python Basics and Data Structures 
   Part 1: Python Introduction and Data Types'''

#Question:01 - Personal Information 
print("\n------- QUESTION 1 - Personal Information -------")

name= "Milasha N. Subasinghe"
age = 25
height= 5.2
is_student= True

print("Name         : ", name)
print("Age          : ", age)
print("Height       : ", height)
print("Is a Student : ", is_student)
print("\n")

#Question:02 - Data Types
print("\n------- QUESTION 2 - value and data type -------")

name = "Abdurrahman" 
age = 25 
height = 1.75 
is_student = True

print("\n",name)
print(type(name))

print(age)
print(type(age))

print(height)
print(type(height))

print(is_student)
print(type(is_student))
print("\n")


#Question:03 - Lists (Food Items)
print("\n------- QUESTION 3 - Lists (Food Items)-------")

foods=["Pasta", "Burger", "Pizza", "Salad", "Sushi"]

#Qs:3.1
print("\nQs.3.1")
print("Foods = ",foods) 

#Qs.3.2
print("\nQs.3.2")
print("First food item: ",foods[0], "& Last food item: ", foods[4]) 

#Qs.3.3
print("\nQs.3.3")
foods.append("Tacos") 
print("After adding a food item: ",foods)

#Qs.3.4
print("\nQs.3.4")
foods.remove("Burger")
print("After removing a food item: ",foods)

#Qs.3.5
print("\nQs.3.5")
foods[0] = "Spaghetti" 
print("After changing 1st food item: ",foods)

#Qs.3.6
print("\nQs.3.6")
print("Final List: ",foods)
print("\n")


#Question:04 - Lists (Student Scores)
print("\n------- QUESTION 4 - Lists (Student Scores) -------")

scores = [75, 80, 65, 90, 85] 

#Qs.4.1
print("\nQs.4.1")
print("scores= ",scores)

#Qs.4.2
print("\nQs.4.2")
print("The highest score is: ", max(scores))

#Qs.4.3
print("\nQs.4.3")
print("The lowest score is: ", min(scores))

#Qs.4.4
print("\nQs.4.4")
scores.append(95)
print("After adding a new score: ", scores)

#Qs.4.5
print("\nQs.4.5")
print("Updated List: ",scores)
print("\n")

#Question 05: Tuples (Days of the Week)
print("\n------- QUESTION 5 - Tuples (Days of the Week) -------")

days= ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

#Qs.5.1
print("\nQs.5.1")
print("Week Days= ",days)

#Qs.5.2
print("\nQs.5.2")
print("First Day: ", days[0] )

#Qs.5.3
print("\nQs.5.3")
print("Last Day: ", days[6])

#Qs.5.4
print("\nQs.5.4")

#days[1]="Holiday" 
#print(days)
print ("\nWhen I try to change a value in a tuple, I got an error that it doesn't allow me to change. Because tuples are immutable, which means tuples are read-only after cretaed and they cannot modified. But lists can be changed.")



#Question 06: Sets (Removing duplicate values)
print("\n------- QUESTION 6 - Sets (Removing duplicate values) -------")

numbers = [1, 2, 3, 4, 2, 5, 3, 6, 1] 

#Qs.6.1
print("\nQs.6.1")
Set = set(numbers)

#Qs.6.2
print("\nQs.6.2")
print("Original List: ", numbers)
print("After converted to Set: ", Set)

#Qs.6.3
print("\nQs.6.3")
print("Duplicate values dissapeared after converting to Set because a set only keeps unique values. They are automatically remover when the list convert into a set. So that, each value appears only once.")


#Question 07: Sets (Unique programming languages)
print("\n------- QUESTION 7 - Sets (Unique programming languages) -------")

Languages = ["Python", "Java", "Python", "C++", "JavaScript", "Python"]

Language_Set = set(Languages)
print("\nOriginal List: ", Languages)
print("\nAfter converted to Set: ", Language_Set)

Language_Set.add("Django")
print("\nUpdated Set: ", Language_Set)


#Question 08: Dictionary 
print("\n------- QUESTION 8 - Dictionary (Student Information) -------")

Students = {"Name":"Ne Yo", "Age":35 , "Course":"Backend Development", "Level":"Beginner Level", "Skills":"Python, SQL, java, node.js " }

#QS.8.1
print("\nQs.8.1")
print("Student Information: ", Students)

#QS.8.2
print("\nQs.8.2")
print("Student Name: ", Students["Name"])

#Qs.8.3
print("\nQs.8.3")
Students["Email"] = "neyo.celebrity@gmail.com"
print("Student Information with Email: ", Students)

#Qs.8.4
print("\nQs.8.4")
Students["Level"] = "Level 3"
print("Student Information after changing Level: ", Students)

#Qs.8.5
print("\nQs.8.5")
Students.pop("Age")
print("Student Information after removing Age: ", Students)

#Qs.8.6
print("\nQs.8.6")
print("Final Student Information: ", Students)

#Question 9 - Student Management Data
print("\n------- QUESTION 9 - Dictionary (Student Information) -------")

Student_01 = {"Name": "John", "Age": 22, "Course": "Backend Development", "Skills":["Python", "HTML", "Git"]}
Student_02 = {"Name": "Mary", "Age": 24, "Course": "Data Analysis", "Skills":["Excel", "SQL", "Python"]}
Student_03 = {"Name": "Bob", "Age": 27, "Course": "Cyber Security", "Skills":["Python", "C", "JavaScript"]}

print("\nStudent_01: ", Student_01)
print("\nStudent_02: ", Student_02)
print("\nStudent_03: ", Student_03)

