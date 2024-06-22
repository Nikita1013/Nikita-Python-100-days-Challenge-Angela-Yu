students_height = input("input the height of the student: \n").split()
for n in range(0, len(students_height)):
    students_height[n] =  int(students_height[n])
    
print(students_height)

#----------------------------------------------------
total_height = 0
for height in students_height:
    total_height += height
    
print(f"Total height of the students is : {total_height}")

noOfStudents = 0
for students in students_height:
    noOfStudents += 1

print(f"Total No of Students : {noOfStudents}")

avg_height = total_height / noOfStudents
print(f"The average height of the students is : {avg_height}")