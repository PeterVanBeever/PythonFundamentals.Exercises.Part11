import unittest
from gradebook import AliveStatus, Person, Instructor, Student, ZipCodeStudent, PreKStudent, Classroom

class TestGradebook(unittest.TestCase):
    def test_alive_status(self):
        person_alive = Person("Peter", "Parker", "2000-06-15")
        person_alive.check_alive_status()
        self.assertEqual(person_alive.alive, AliveStatus.Alive)

        person_deceased = Person("Jimothy", "Scott", "1900-01-01")
        person_deceased.check_alive_status()
        self.assertEqual(person_deceased.alive, AliveStatus.Deceased)


    def test_person(self):
        person = Person("Peter", "Parker", "2000-06-15")
        self.assertEqual(person.first_name, "Peter")
        self.assertEqual(person.last_name, "Parker")
        self.assertEqual(person.dob, "2000-06-15")
        self.assertEqual(person.alive, AliveStatus.Alive)

    def test_instructor(self):
        instructor = Instructor("Tony", "Stark", "1970-06-15")
        self.assertTrue(instructor.instructor_id.startswith("Instructor_"))

    def test_student(self):
        student = Student("Miles", "Morales", "2024-06-15")
        self.assertTrue(student.student_id.startswith("Student_"))

    def test_zipcode_student(self):
        zipcode_student = ZipCodeStudent("Clark", "Kent", "2010-06-15")
        self.assertTrue(zipcode_student.student_id.startswith("Student_"))

    def test_prek_student(self):
        prek_student = PreKStudent("Bruce", "Wayne", "2015-06-15")
        self.assertTrue(prek_student.student_id.startswith("Student_"))

    def test_classroom(self):
        classroom = Classroom()
        instructor = Instructor("Tony", "Stark", "1970-06-15")
        student = Student("Miles", "Morales", "2024-06-15")

        classroom.add_instructor(instructor)
        classroom.add_student(student)

        self.assertIn(instructor, classroom.instructors)
        self.assertIn(student, classroom.students)

        classroom.remove_instructor(instructor)
        classroom.remove_student(student)

        self.assertNotIn(instructor, classroom.instructors)
        self.assertNotIn(student, classroom.students)

if __name__ == '__main__':
    unittest.main()
