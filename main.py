from student import Student
from database import load_students, save_students

students = load_students()


def add_student():
    student_id = input("Student ID: ")
    name = input("Name: ")
    age = input("Age: ")
    grade = input("Grade: ")

    student = Student(student_id, name, age, grade)

    students.append(student.to_dict())
    save_students(students)

    print("\nStudent Added Successfully!\n")


def show_students():
    if not students:
        print("\nNo Students Found\n")
        return

    print()

    for student in students:
        print("-----------------------------")
        print(f"ID    : {student['ID']}")
        print(f"Name  : {student['Name']}")
        print(f"Age   : {student['Age']}")
        print(f"Grade : {student['Grade']}")
    print("-----------------------------")


def search_student():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["ID"] == student_id:
            print("\nStudent Found\n")
            print(student)
            return

    print("\nStudent Not Found\n")


def delete_student():
    student_id = input("Student ID: ")

    for student in students:
        if student["ID"] == student_id:
            students.remove(student)
            save_students(students)
            print("\nDeleted Successfully\n")
            return

    print("\nStudent Not Found\n")


def update_student():
    student_id = input("Student ID: ")

    for student in students:
        if student["ID"] == student_id:

            student["Name"] = input("New Name: ")
            student["Age"] = input("New Age: ")
            student["Grade"] = input("New Grade: ")

            save_students(students)

            print("\nUpdated Successfully\n")
            return

    print("\nStudent Not Found\n")


while True:

    print("""
======== Student Management System ========

1. Add Student
2. Show Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

==========================================
""")

    choice = input("Choose: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Good Bye!")
        break

    else:
        print("Invalid Choice")
