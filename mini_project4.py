# Student performance analytics toolkit

students={
    "S101":{
        "name":"Aman",
        "marks":[78,65,88]
    },
    "S102":{
        "name":"Riya",
        "marks":[35,72,61]
    }

}

def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    if len (marks)==0:
      return 0

    return calculate_total(marks)/len(marks)

def get_grade(average):
    if average>=75:
        return"Distinction"
    elif average>=60:
        return "First Division"
    elif average>=40:
        return "Pass"
    else:
        return"Fail"

    def bulid_report(student):
        marks=student["marks"]
        total=calculate_total(marks)
        average=calculate_average(marks)
        grade=get_grade(average)


        return{
            "name":student["name"],
            "marks":marks,
            "total":total,
            "average":average,
            "grade":grade

        }
    def get_top_students(students):
      return list(filter(
        lambda item: calculate_average(item[1]["marks"]) >= 75,
        students.items()
    ))
    def get_student_names(students):
      return list(map(
        lambda item: item[1]["name"],
        students.items()
    ))

    def flexible_average(*marks):
      if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)

    def class_summary(students, **options):
     title = options.get("title", "Class Report")
     passing_mark = options.get("passing_mark", 40)


    if len(students) == 0:
        print("No student records available.")
        return

    total_average = 0
    passed = 0

    for student in students.values():
        average = calculate_average(student["marks"])
        total_average += average

        if average >= passing_mark:
            passed += 1

    class_average = total_average / len(students)

    print("Total Students:", len(students))
    print(f"Class Average: {class_average:.2f}")
    print("Students Passed:", passed)



def recursive_sum(n):
    if n <= 0:
        return 0

    return n + recursive_sum(n - 1)


    
def get_top_students(students):
    return list(filter(
        lambda item:calculate_average(item[1]["marks"])>=75,
        students.items()
         ))

def build_report(student):
    marks = student["marks"]

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = get_grade(average)

    report = {
        "name": student["name"],
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    return report


def get_student_names(students):
    names = list(map(
        lambda item: item[1]["name"],
        students.items()
    ))

    return names
def get_student_names(students):
    return list(map(
        lambda item: item[1]["name"],
        students.items()
    ))
# 11. Main Function
def main():
    print("===== STUDENT PERFORMANCE REPORT =====")

    for student_id, student in students.items():
        report = build_report(student)

        print("\nStudent ID:", student_id)
        print("Name:", report["name"])
        print("Marks:", report["marks"])
        print("Total:", report["total"])
        print(f"Average: {report['average']:.2f}")
        print("Grade:", report["grade"])

    print("\nStudent Names:", get_student_names(students))
     
    top_students = get_top_students(students)

    top_names = list(map(
    lambda item: item[1]["name"],
    top_students
))

    print("High Performers:", top_names)

total_average=0

for student in students.values():
      average = calculate_average(student["marks"])
      total_average += average
main()

print("Recursive Sum from 1 to 5:", recursive_sum(5))
