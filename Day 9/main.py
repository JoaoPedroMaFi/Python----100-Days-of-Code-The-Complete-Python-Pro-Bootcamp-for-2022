# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again", }
#
# print(programming_dictionary["Bug"])

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
#
# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
#
# # TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     if student_scores[student] < 70:
#         student_grades[student] = "Fail"
#     elif student_scores[student] < 80:
#         student_grades[student] = "Acceptable"
#     elif student_scores[student] < 90:
#         student_grades[student] = "Exceeds Expectations"
#     else:
#         student_grades[student] = "Outstanding"
#
# # 🚨 Don't change the code below 👇
# print(student_grades)
#
# #6378-cb94-42f7-4257-8461-053e 3bee-0183
#
# # Nesting
#
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }
#
# travel_log = {
#     "France": {
#         "Visited_cities": ["Paris", "Lille", "Dijon"],
#         "total_visited": 12,
#     },
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above
#
# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country,visits, cities):
#     dict = {"country": country,
#            "visits": visits,
#            "cities": cities
#            }
#     travel_log.append(dict)
#
#
#
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
dict[1] = 4
print(dict[1])
