from queue import Empty


students = {}

def add_student(name):
    if name not in students:
        students[name] = []
    else:
        print(f"Student {name} already exists.")
    return students

def add_grade(name, grade):
    students[name].append(grade)
    
def show_report():
    average_grades = []
    if len(students) > 0:
        for name, grades in students.items():
            if len(grades) != 0:
                avg = sum(grades) / len(grades)
                average_grades.append(avg)
                print(f"{name}'s average grade is: {avg}")
            else:
                print(f"{name}'s average grade is N/A.")
        if(len(average_grades) > 0):
            print(f"Max average: {max(average_grades)}")
            print(f"Min average: {min(average_grades)}")
            print(f"Overall average: {sum(average_grades) / len(average_grades)}")
        else:
            print("There're no students with grades.")
            
    else:
        print("There're no students.")

def find_top_student():
    if not students:
        print("There're no students to choose from.")
    else:
        top_student = max(students.items(), key=lambda x: sum(x[1]) / len(x[1]) if len(x[1]) != 0 else 0)
        if len(top_student[1]) == 0:
            print("There is no top student with grades.")
        else:
            print(f"The student with the highest average is {top_student[0]} with an average of {sum(top_student[1]) / len(top_student[1])}")