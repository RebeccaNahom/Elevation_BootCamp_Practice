import json
import csv

# # spot check 1
# the_file = open("attendance.txt")
# attendance = the_file.read().split("\n")
#
# student_attendance = {}
# for i in attendance:
#     if i in student_attendance:
#         student_attendance[i] += 1
#     else:
#         student_attendance[i] = 1
#
# print(student_attendance)

# # spot check 2
# the_file = open("example.txt")
# groceries = the_file.read().split("\n")
#
# goodies = ["Barnacle", "Circus", "Rake", "Cherry", "Steam", "Toothpaste", "Knee", "Coat"]
#
# with open('example.txt', 'a') as the_file:
#     for goodie in goodies:
#         if goodie.startswith("C"):
#             the_file.write(goodie + "\n")
#
# # Spot Check 3
# import json
# summary = {
#     "male": {
#         "total": 0,
#         "alive": 0
#     },
#     "female": {
#         "total": 0,
#         "alive": 0
#     }
# }
#
# the_file = open("turtles.json")
# turtles = json.load(the_file)
# print(turtles[0]["gender"])
#
# with open("turtles_summary.json", "a") as f:
# 	for turtle in turtles:
# 		if turtle["gender"] == "female":
# 			summary["female"]["total"] += 1
# 			if turtle["condition"]["status"] == "alive":
# 				summary["female"]["alive"] +=1
# 		if turtle["gender"] == "male":
# 			summary["male"]["total"] += 1
# 			if turtle["condition"]["status"] == "alive":
# 				summary["male"]["total"] += 1
# 	json.dump(summary, f)
#
#
# import csv
# total_expenses = 0
#
# with open ('expenses.csv') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     next(csv_reader)
#     for row in csv_reader:
#         print(row)
#         total_expenses += int(row[1])
#
#
# print(total_expenses)
# import csv
#
# products = [
#     {"name": "Apple", "product": "iPad", "price": 999},
#     {"name": "Apple", "product": "iPod", "price": 1999},
#     {"name": "Apple", "product": "iPed", "price": 2999},
#     {"name": "Apple", "product": "iPud", "price": 3999},
#     {"name": "Apple", "product": "iPid", "price": 4999}
# ]
#
# with open("products.csv", "w") as csv_file:
#     csv_writer = csv.writer(csv_file)
#
#     for product in products:
#         # create a list with our data (the values from the dict above)
#         data_in_list = [product["name"], product["product"], product["price"]]
#
#         # writes a single row each time
#         csv_writer.writerow(data_in_list)

# # Spot Check 4

stocks = [
    {"name": "Apple", "price": 246},
    {"name": "Tesla", "price": 328},
    {"name": "Microsoft", "price": 140},
    {"name": "Amazon"},
    {"name": "Lionsgate", "price": 8},
    {"name": "Netflix", "price": 276},
    {"name": "Google"},
    {"name": "Activision", "price": 55},
]

with open("stocks.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(["company", "price"])

    for stock in stocks:
        name = stock["name"]
        price = 0
        if "price" in stock:
            price = stock["price"]
        csv_writer.writerow([name, price])
