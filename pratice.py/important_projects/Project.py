def file(name, student_info, performance_info):
    filename = name + ".txt"
    with open(filename, "w") as f:
        f.write("Student Info Is Given Below:\n \n")
        f.write(student_info + "\n")
        f.write(performance_info + "\n")
        f.write("Student Info Is Ended.\n")

name = input("Enter Student Name Here: ")
institude = input("Enter Student college Name Here: ")
current_education = input("Student in Current Year:  ")
print("\n")

def student_information():

    class student:
        def __init__(self , name , institude , current_education):
            self.name = name
            self.institude = institude
            self.current_education = current_education

        def student_info(self):
            info = f"Student Name Is: {self.name} \n Collage Name: {self.institude} \n {self.name} is current in {self.current_education} \n"
            print("Recheck the form Information Again\n")
            print(info)
            return info
        
    class student_performance(student):
        def performance(self):
            n = int(input("How Many Subjects Do You Have ?? \n "))

            subject  = []
            for i in range(n):
                sub = input(f"Enter Subject {i+1} Name: ")
                subject.append((sub))
            print("")
            mark  = []
            for i in range(n):
                marks = int(input(f"Enter Yor Mark for {subject[i]}: "))
                mark.append(marks)

            max_mark = n * 100
            Total_marks = sum(mark)
            percentage = ( Total_marks * 100 ) /  max_mark

            # use to store subject and marks
            subject_marks_info = "Subjects and Marks:\n"
            for i in range(n):
                subject_marks_info += f"{subject[i]}: {mark[i]}\n"

            result = (
                f"{subject_marks_info}\n"
                f"Total Marks: {Total_marks}/{max_mark}\n"
                f"Percentage: {percentage:.2f}%\n"
            )
            print(f"{Total_marks}/{max_mark}")
            print(percentage)
            return result 
        


    printf = student_performance(name,institude,current_education )


    student_info = printf.student_info()
    performance_info = printf.performance()

    file(name , student_info , performance_info)

student_information()