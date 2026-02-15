class Student:
    counter = 1000

    def __init__(self, name):
        Student.counter += 1
        self.student_id = Student.counter
        self.name = name


class Course:
    counter = 500

    def __init__(self, course_name):
        Course.counter += 1
        self.course_id = Course.counter
        self.course_name = course_name


class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.marks = 0


class CourseManagementSystem:
    def __init__(self):
        self.students_list = []
        self.courses_list = []
        self.enrollments_list = []

    def add_student(self, name):
        student = Student(name)
        self.students_list.append(student)
        return student

    def add_course(self, course_name):
        course = Course(course_name)
        self.courses_list.append(course)
        return course

    def enroll_student(self, student_id, course_id):
        student = None
        course = None

        # Find student
        for s in self.students_list:
            if s.student_id == student_id:
                student = s
                break

        # Find course
        for c in self.courses_list:
            if c.course_id == course_id:
                course = c
                break

        if student and course:
            # Check if already enrolled
            for e in self.enrollments_list:
                if e.student.student_id == student_id and e.course.course_id == course_id:
                    return False

            enrollment = Enrollment(student, course)
            self.enrollments_list.append(enrollment)
            return True

        return False

    def assign_marks(self, student_id, course_id, marks):
        for e in self.enrollments_list:
            if e.student.student_id == student_id and e.course.course_id == course_id:
                e.marks = marks
                return True
        return False

    def generate_report(self, student_id):
        total = 0
        count = 0

        for e in self.enrollments_list:
            if e.student.student_id == student_id:
                total += e.marks
                count += 1

        if count == 0:
            return False

        average = total / count

        print("\nReport")
        print("Student ID:", student_id)
        print("Average Marks:", average)

        if average >= 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")

        return average


# ------------------------
# Testing the Program
# ------------------------

cms = CourseManagementSystem()

# Add students
s1 = cms.add_student("Atharva")
s2 = cms.add_student("Rahul")

# Add courses
c1 = cms.add_course("Python")
c2 = cms.add_course("Data Science")

# Enroll students
cms.enroll_student(s1.student_id, c1.course_id)
cms.enroll_student(s1.student_id, c2.course_id)
cms.enroll_student(s2.student_id, c1.course_id)

# Assign marks
cms.assign_marks(s1.student_id, c1.course_id, 85)
cms.assign_marks(s1.student_id, c2.course_id, 35)
cms.assign_marks(s2.student_id, c1.course_id, 50)

# Generate report
cms.generate_report(s1.student_id)
cms.generate_report(s2.student_id)
