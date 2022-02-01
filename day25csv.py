
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1]!="temp":
#             temperature.append((int(row[1])))
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # type of data
# # print(type(data)) -> dataframe
# # print(type(data["temp"])) ->series
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # # sum = sum(temp_list)
# # # size = len(temp_list)
# # # avg = sum/size
# # # print(round(avg,2))
# # print(round(data["temp"].mean(),2))
# # print(data["temp"].max())
# #
# # # get data in column
# # print(data["condition"])
# # print(data.condition)
#
# # get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])
#
# # convert monday temp into Fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_in_fahrenheit = monday_temp*1.8 + 32
# print(monday_temp_in_fahrenheit)

# create a dataframe from scratch
data_dict = {
    "students": ["Prakash", "shanky", "saras"],
    "scores": [75,76,77]
}
data = pandas.DataFrame(data_dict)
print(data)
# data_dict to csv
data.to_csv("my_own_created_dataset.csv")