# with open("weather-data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv
# prints all the data
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)

# Printing only temperature
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# import pandas
# # using Pandas
# data = pandas.read_csv("weather-data.csv")
# print(data)

import pandas

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray","Cinnamon", "Black"],
    "Count": [grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
