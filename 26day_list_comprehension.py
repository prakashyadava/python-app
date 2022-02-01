import random
# for loop
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n+1
#     new_list.append(add_1)
# print(new_list)
# List comprehension
# new_list = [new_item for item in list]
# name = "prakash"
# new_list = [letter  for letter in name.title()]
# print(new_list)

# name_list = ["Prakash","shanky","saras","aa"]
# new_list = [n.upper() for n in name_list if len(n) > 5]
# print(new_list)

# numbers = [1, 1, 2, 3,5,8,13,21,34,55]
# # squared_numbers = [n**2 for n in numbers]
# # print(squared_numbers)
# result = [n for n in numbers if n%2==0]
# print(result)

# with open("26_file1.txt") as file1:
#     file1_list = file1.readlines()
#
# with open("26_file2.txt") as file2:
#     file2_list = file2.readlines()
#
# # common = [int(n) for n in file1_list if file2_list.count(n) >= 1]
# common = [int(n) for n in file1_list if n in file2_list]
# print(common)

# dictonary comprehension
# names = ["Alex","Adam","Beth","Carl","Downy","Elizabeth"]
#
# student_scores = {student:random.randint(1,100)  for student in names}
# # passed_student = {student:student_scores[student] for student in student_scores if student_scores[student] >=60} this is also correct
# passed_student = {student:score  for (student,score) in student_scores.items() if score >= 60}
# print(student_scores)
# print(passed_student)

# sentences = "What is the Airspeed Velocity of an Unladen swallow?"
# word_count = {word:len(word) for word in sentences.split()}
# print(word_count)
#
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "sunday": 24,
# }
# weather_f = {day:(temp*9/5) + 32 for (day,temp) in weather_c.items()}
# print(weather_c)
# print(weather_f)

# looping through dictionary
import pandas
student_dict ={
    "student": ["Angela","James","Lily"],
    "score": [56 ,76, 98]
}
# for (key,value) in student_dict.items():
#     print(key,":",value)
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
# loop through a data frame
# for (key,value) in student_data_frame.items():
#     print(value)

# loop through rows of data frame
for (index,row) in student_data_frame.iterrows():
    if row.student=="Angela":
        print(row.score)