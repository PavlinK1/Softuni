data = input()
courses = {}
while ":" in data:
    student_name, id, course_name = data.split(":")

    if course_name not in courses:
        courses[course_name] = {}
    courses[course_name][id] = student_name
    data = input()

searched_courses = data
searched_courses_list = searched_courses.split("_")
searched_courses = ' '.join(searched_courses_list)

for course_name in courses:
    if course_name == searched_courses:
        for id, name in courses[course_name].items():
            print(f"{name} - {id}")
