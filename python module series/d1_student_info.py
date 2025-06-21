def get_student_data():
    student_marks = {}
    n = int(input("How many students? "))

    for _ in range(n):
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        student_marks[name] = marks

    return student_marks

def calculate_average(marks_dict):
    total = sum(marks_dict.values())
    avg = total / len(marks_dict)
    return avg

def find_topper(marks_dict):
    topper = max(marks_dict, key=marks_dict.get)
    return topper, marks_dict[topper]

# Main program
students = get_student_data()
avg = calculate_average(students)
topper, top_marks = find_topper(students)

print(f"\nAverage marks: {avg}")
print(f"Topper: {topper} with {top_marks} marks")
