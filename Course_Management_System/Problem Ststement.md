# Problem Ststement

Design a system to manage an online learning platform.


# class Diagram

                           +-----------------------------------+
                           |     CourseManagementSystem         |
                           +-----------------------------------+
                           | - students : list[Student]        |
                           | - courses : list[Course]          |
                           | - enrollments : list[Enrollment]  |
                           +-----------------------------------+
                           | + add_student()                   |
                           | + add_course()                    |
                           | + enroll_student()                |
                           | + assign_marks()                  |
                           | + generate_report()               |
                           +-----------------------------------+
                                      |
          -------------------------------------------------------------
          |                           |                              |
          | Composition               | Composition                   | Composition
          v                           v                              v

+----------------------+     +----------------------+     +----------------------+
|        Student       |     |        Course        |     |      Enrollment      |
+----------------------+     +----------------------+     +----------------------+
| - student_id         |     | - course_id          |     | - student : Student  |
| - name               |     | - course_name        |     | - course : Course    |
+----------------------+     +----------------------+     | - marks              |
                                                          +----------------------+

                          Association Relationship:
             Enrollment links one Student to one Course.













# Class description

## Student class:

1. Initialize static variable `counter` to 1000  
2. Include the following attributes:  
   - `student_id`  
   - `name`  
3. Auto-generate `student_id` starting from 1001 whenever a new student object is created  

---

## Course class:

1. Initialize static variable `counter` to 500  
2. Include the following attributes:  
   - `course_id`  
   - `course_name`  
3. Auto-generate `course_id` starting from 501 whenever a new course object is created  

---

## Enrollment class:

1. Include the following attributes:  
   - `student` (reference to Student object)  
   - `course` (reference to Course object)  
   - `marks` (initialize to 0)  
2. Store the association between a student and a course  

---

## CourseManagementSystem class:

1. `students_list`: List of Student objects  
2. `courses_list`: List of Course objects  
3. `enrollments_list`: List of Enrollment objects  

4. `add_student(name)`:
   1. Create a new Student object  
   2. Add the student object to `students_list`  
   3. Return the created student object  

5. `add_course(course_name)`:
   1. Create a new Course object  
   2. Add the course object to `courses_list`  
   3. Return the created course object  

6. `enroll_student(student_id, course_id)`:
   1. Check whether the student exists in `students_list`  
   2. Check whether the course exists in `courses_list`  
   3. If both exist,  
      - Check if the student is already enrolled in the same course  
      - If not enrolled,  
        - Create an Enrollment object  
        - Add it to `enrollments_list`  
        - Return True  
      - Else, return False  
   4. Else, return False  

7. `assign_marks(student_id, course_id, marks)`:
   1. Find the matching Enrollment object  
   2. If found,  
      - Assign marks  
      - Return True  
   3. Else, return False  

8. `generate_report(student_id)`:
   1. Find all enrollments of the given student  
   2. If enrollments found,  
      - Calculate average marks  
      - If average marks ≥ 40, display "PASS"  
      - Else, display "FAIL"  
      - Return average marks  
   3. Else, return False  

---

Perform case-sensitive comparison wherever required.  
Create objects of `CourseManagementSystem` class, invoke appropriate methods and test your program.