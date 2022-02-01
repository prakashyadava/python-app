student_heights = input("Enter the height of students: ").split()
for n in range (0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
    # print(student_heights[n])
sum =0
for i in range (0,len(student_heights)):
    sum += student_heights[i]
avg = round(sum / len(student_heights))

print(f"Average is : {avg}")