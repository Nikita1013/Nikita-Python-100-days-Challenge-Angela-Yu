student_scores = input("input a list of students score : \n").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# ---------------------------------------------
for max_score in student_scores:
    if (student_scores[n] < max_score):
        print(f"The maximum score is :  {max_score}")

# print(max(student_scores))
# print(min(student_scores))