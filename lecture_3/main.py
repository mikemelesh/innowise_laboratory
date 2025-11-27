from student import *

while True:
    print("1. Add student")
    print("2. Add grades for a student")
    print("3. Generate a full report")
    print("4. Find the top student")
    print("5. Exit program")
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            name = input("Enter student name: ")
            add_student(name)
        case "2":
            name = input("Enter student name: ")
            if name not in students:
                print(f"Student {name} not found")
                continue
            while True:
                grade = input("Enter a grade (or 'done' to finish): ")
                if grade == "done":
                    break
                try:
                    grade = int(grade)
                    if 0 <= grade <= 100:
                        add_grade(name, grade)
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        case "3":
            show_report()
        case "4":
            find_top_student()
        case "5":
            print("Exiting program.")
            exit()