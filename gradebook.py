from enum import Enum
# unigue identifiers

import uuid
#for dates and time
from datetime import datetime

class AliveStatus(Enum):
    Deceased = 0
    Alive = 1

class Person:
    # constructor
    def __init__(self, first_name, last_name, dob, alive=AliveStatus.Alive):
        # initialize values
        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = alive

    def update_first_name(self, first_name):
        self.first_name = first_name

    def update_last_name(self, last_name):
        self.last_name = last_name

    def update_dob(self, dob):
        self.dob = dob

    def update_status(self, status):
        self.alive = status
    # age calculation
    def calculate_age(self):
        # get todays date
        today = datetime.today()
        # parese date into datetime objec?
        dob = datetime.strptime(self.dob, '%Y-%m-%d')
        # calculate 
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age
        
    def check_alive_status(self):
        age = self.calculate_age()
        if age >= 120:
            self.alive = AliveStatus.Deceased
        else:
            self.alive = AliveStatus.Alive

# inheritance!!!
class Instructor(Person):
    # constructor
    def __init__(self, first_name, last_name, dob, alive=AliveStatus.Alive):
        super().__init__(first_name, last_name, dob, alive)
        self.instructor_id = f"Instructor_{uuid.uuid4()}"

# inheritance!!!
class Student(Person):
    # constructor
    def __init__(self, first_name, last_name, dob, alive=AliveStatus.Alive):
        #call parent    
        super().__init__(first_name, last_name, dob, alive)
        #unique id for student with uuid
        self.student_id = f"Student_{uuid.uuid4()}"


class ZipCodeStudent(Student):
    pass

class PreKStudent(Student):
    pass

class Classroom:
    def __init__(self):
        self.students = []
        self.instructors = []

    def add_instructor(self, instructor):
        self.instructors.append(instructor)

    def remove_instructor(self, instructor):
        self.instructors.remove(instructor)

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def print_instructors(self):
        for instructor in self.instructors:
            print(f"Instructor ID: {instructor.instructor_id}, Name: {instructor.first_name} {instructor.last_name}")

    def print_students(self):
        for student in self.students:
            print(f"Student ID: {student.student_id}, Name: {student.first_name} {student.last_name}")
