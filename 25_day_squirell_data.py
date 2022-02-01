import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
fur_color_list = fur_color.to_list()
gray_count = fur_color_list.count("Gray")
cinnamon_count = fur_color_list.count("Cinnamon")
black_count = fur_color_list.count("Black")
squirrel_data= {
    "fur color": ["Gray", "Cinnamon", "Black"],
    "count": [gray_count, cinnamon_count, black_count]
}
squirrel_df = pandas.DataFrame(squirrel_data)
print(squirrel_df)
squirrel_df.to_csv("new_squirrel_data.csv")