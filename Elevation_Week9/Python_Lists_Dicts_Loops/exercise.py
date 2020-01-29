# #exercise 1
# library = {
# 	"books": [
# 		{"title": "Name of the Wind0" , "author": "Patrick Rothfuss0"},
# 		{"title": "Name of the Wind1", "author": "Patrick Rothfuss1"},
# 		{"title": "Name of the Wind", "author": "Patrick Rothfuss2"},
# 		{"title": "Name of the Wind3", "author": "Patrick Rothfuss3"}
# 	]
# }
# books_length = len(library["books"])
# books = library["books"]
# print(library["books"][books_length - 1])

##exercise 2
#for book in books:
#	if book["title"] == "Name of the Wind":
#		print(book["author"])


# #exercise 3+4
# names = ["Ashley", "Donovan", "Lucas"]
# ages = [23, 47, 18]
# people = []
#
# length = len(names)
# {"name": "Ashley", "age": 23}
# for i in range(0, length):
# 	people.append({"name": names[i], "age": ages[i]})
# 	print(people[i]["name"] + " is " + str(people[i]["age"]) + "y/o.")

# #exercise 5
# employee_data = [
#     {"employee_id": 412, "department": "Finance", "salary": 1300},
#     {"employee_id": 833, "department": "Sales", "salary": 4200},
#     {"employee_id": 347, "department": "Sales", "salary": 2800},
#     {"employee_id": 148, "department": "Finance", "salary": 1200},
#     {"employee_id": 334, "department": "Finance", "salary": 2600},
#     {"employee_id": 533, "department": "Sales", "salary": 1800},
#     {"employee_id": 992, "department": "Sales", "salary": 3100},
# ]
# department_salaries =  {}
# finance_salary = 0
# sales_salary = 0
#
# for i in employee_data:
#     if i["department"] == "Finance":
#         finance_salary += i["salary"]
#         department_salaries.update({"Finance": finance_salary})
#     if i["department"] == "Sales":
#         sales_salary += i["salary"]
#         department_salaries.update({"Sales":sales_salary})
# print(department_salaries)

#exercise 5
code = {
    "0": "A",
    "1": "E",
    "2": "O",
    "3": "U",
    "4": "G",
    "5": "R",
    "6": "T",
    "7": "U",
    "8": "Y"
}

encrypted_message = "82705145106"
array_message = []
code_keys = code.keys()

for i in encrypted_message:
   for j in code_keys:
       if i == j:
           array_message.append(code[j])

message = '' .join(array_message)
print (message)


