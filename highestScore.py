score = input("Enter the score of student : ").split()
highest_score = int(score[0])

for i in  range (0,len(score)):
    if int(score[i])>= highest_score:
        highest_score = int(score[i])

print(f"Highest score the list {score} is {highest_score}")
'''
 or we can also use min() or max() method to find the min and max value 
'''
# for n in range (0,len(score)):
#     score[n] = int(score[n])
#
# print(max(score))