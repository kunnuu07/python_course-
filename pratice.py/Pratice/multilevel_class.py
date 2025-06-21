class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_person_info(self):
        print(f"The Name Of Person Is {self.name} and the age Of person is {self.age}")

class Student(person):
    student_id = "STU07092007"
    course = "Bsc.Forensic Science & Cyber Security"
    def Display_student_info(self):
        print(f"The Student Id Is {self.student_id} and the Course of Student Is {self.course}")

class Graduate_Student(Student):
    specialization = "Student Specialization in Msc.cyber Security"
    def display_graduate_info(self):
        print(f"Name Of Student Is {self.name} and {self.specialization}")

a = Graduate_Student("Kunal Shirsath","19")
a.display_person_info()
a.Display_student_info()
a.display_graduate_info()

