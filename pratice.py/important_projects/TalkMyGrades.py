'''🧠 Project: Voice-Based Student Report Card Generator
📝 Description:
This project will:

Ask user for student details (name, subjects, marks).

Use a loop to enter multiple subjects and marks.

Use conditional logic to assign grades.

Use OOP to define a Student class.

Use pyttsx3 to read out the report card.'''

import pyttsx3
import os

def speak(data):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)

    engine.setProperty('rate',155)
    engine.setProperty('volume',1.0)

    engine.say(data)
    engine.runAndWait()
    engine.stop()
    
name = str(input("Enter Your Name: ")).upper()

def file(student_inf , Student_performanc):
    folder = "student_info"
    os.makedirs(folder, exist_ok=True) 
    filename = f"{name.replace(' ', '_')}_report.txt"
    filepath = os.path.join(folder, filename)

    with open(filepath,"w") as f:
        f.write(student_inf + "\n")
        f.write("\n\n")
        f.write(Student_performanc + "\n")
        f.write("\n\n")
        f.write("Student info is Saved !!")


class student:
    def student_info(self):
        info = f" Student Name Is: {name} \n"
        return info
    
class student_(student):
    def student_performance(self):
        try:
            sub = int(input("How Many Subject DO you Have???\n "))
        except Exception as e:
            e = "Invalid Input.Please Enter a Number"
            print(e)

        subject =[]
        marks = []

        for i in range(sub):
            subs = str(input("Enter Subject Name: "))
            subject.append(subs)

        print("\n")


        for i in range(sub):
            mark = int(input(f"Enter {subject[i]} Marks: "))
            marks.append(mark)

        max_marks = sub*100
        Total = sum(marks)
        Percentage = (Total / max_marks)*100
        Percentage = round(Percentage , 2)

        if(Percentage < 35):
            msg = f"Next Time Better Luck {name}"
            print(msg)
            speak(msg)

        else:
            msg = f"Congrats Your Passed \n You Got {Percentage}%"
            print(msg)
            speak(msg)
        
        # Build performance report string
        report = ""
        for i in range(sub):
            report += f"{subject[i]}: {marks[i]}\n" # we can use for loop for only print subject and marks
        report += f"Total: {Total}/{max_marks}\n\n"
        report += f"Percentage: {Percentage}%\n\n"
        report += f"Result: {msg}"

        return report

a = student_()
info = a.student_info()
performance = a.student_performance()

file(info ,performance)

