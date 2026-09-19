# Question 02: Student Grade Evaluator & Class Performance Tracker

# Qs.02.a - Initial Setup & Batch Count
print("\n")
count = int(input("How many student entries do you want to  create?"))
student_records={}

# Qs.02.b - Dynamic Entry Loop
for i in range(count):
    print(f"\nEntry {i+1}:")
    name = str(input("Enter student name: "))
    score = float(input("Enter score (0-100):"))
    student_records[name] = score

# Qs.02.c - c. Evaluation & Performance Analysis
passed_count=0
failed_count=0
total_score=0

print("\n========================================") 
print ("EVALUATION RESULTS") 
print("========================================")

for name, score in student_records.items():
    total_score = total_score + score

    if score >= 70:
        grade = "Grade A"
        status = "Passed with Distinction"
        passed_count = passed_count + 1
    elif score >= 50:
        grade = "Grade B"
        status = "Passed"
        passed_count = passed_count + 1 
    else:
        grade = "Grade F"
        status = "Need Improvement"
        failed_count = failed_count + 1   

    print(f"{name} :Score {score:.1f} | {grade} | {status}")

#Qs.02.d - Class Summary   
average_score = total_score / count
print("======================================== ")

print("\n======================================== ")
print("CLASS PERFORMANCE")
print("======================================== ")
print(f"Average Score:{average_score:.1f}")
print(f"Totatl Passed:{passed_count}")
print(f"Total Failed:{failed_count}")