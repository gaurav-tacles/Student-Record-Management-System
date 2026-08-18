import random

def generate_student_id(course_code, student_number):
    student_id = str(course_code) + str(student_number).zfill(4) #zfill add input numbers of 0 to make it separated
    return student_id

def load_courses():
    courses = {}

    try:
        file = open("courses.txt", "r")
        for line in file:
            line = line.strip()

            if line == "":
                continue

            course, code = line.split(",")
            courses[course] = int(code)

        file.close()

    except FileNotFoundError:
        file = open("courses.txt", "w")
        file.close()

    return courses

def generate_course_code(courses):
    while True:
        code = random.randint(1, 99)

        if code not in courses.values():
            return code

def save_course(course, code):
    file = open("courses.txt", "a")
    file.write(course + "," + str(code) + "\n")
    file.close()

def get_course_code(course):
    courses = load_courses()

    if course in courses:
        return courses[course]

    code = generate_course_code(courses)
    save_course(course, code)

    return code

def get_next_student_number(course_code):
    counters = {}

    try:
        file = open("student_counters.txt", "r")

        for line in file:
            line = line.strip()

            if line == "":
                continue

            code, number = line.split(",")
            counters[int(code)] = int(number)

        file.close()

    except FileNotFoundError:
        file = open("student_counters.txt", "w")
        file.close()

    if course_code in counters:
        counters[course_code] = counters[course_code] + 1
    else:
        counters[course_code] = 1

    file = open("student_counters.txt", "w")

    for code, number in counters.items():
        file.write(str(code) + "," + str(number) + "\n")

    file.close()

    return counters[course_code]

def add_student():
    print("---------- ADD STUDENT ----------")

    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")

    course = input("Enter Course: ")

    course_code = get_course_code(course)
    student_number = get_next_student_number(course_code)
    student_id = generate_student_id(course_code, student_number)

    print("Student ID:", student_id)
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

def save_student(student_id, name, age, course):
    file = open("students.txt", "a")
    file.write(student_id + "," + name + "," + age + "," + course + "\n")
    file.close()