# students_scores = {"prakash": 99,
#                  "shanky":88,
#                  "saras":78,
#                  "pratyush":68,
#                  "harsh":58,
#                  "himanshu":48}
# students_grades = {}
# for student in students_scores:
#     score = students_scores[student]
#     if score>90:
#         students_grades[student] = "Excellent"
#     elif score>80:
#         students_grades[student] = "Exceed Expectation"
#     elif score>70:
#         students_grades[student] = "Try to improve"
#     elif score>60:
#         students_grades[student]= "Do more hardwork"
#     elif score>=50:
#         students_grades[student] = "very low"
#     elif score>0:
#         students_grades[student] = "Fail"
#
# print(students_grades[1])
# #
# def add_new_country(country_visited, times_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)
#
# travel_log = [
#     {
#     "country" : "France",
#     "visits" : 12,
#     "cities" : ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country" : "Germany",
#         "visits" : 5,
#         "cities" : ["Berlin", "Hamburg", "Stuttgart"]
#     }
# ]
#
# add_new_country("Russia", 12, ["Moscow", "Saint Petersburg"])
# print(travel_log)
bid_details  = {}
bid_value = []
next = True
while next:
    name = input("Enter your name : ")
    bid = int(input("Enter your bid : $"))
    bid_details[name] = bid
    bid_value.append(bid)
    ask = input("Is there any person in room ,Type 'Yes' or ' No': ")
    if ask=="No":
        next =False


max = 0
for val in bid_value:
    if max<= val:
        max = val


for key in bid_details:
    if bid_details[key]==max:
        print(f"The winner is {key} with a bid of ${bid_details[key]}")
