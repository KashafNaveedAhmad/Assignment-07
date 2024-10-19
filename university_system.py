# Base "University" class
class University:
    def __init__(self, name, campus, location, contact_no):
        self.name = name
        self.campus = campus
        self.location = location
        self.contact_no = contact_no
        self.departments = []  # Store department objects
    
    def univ_info(self):
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        print("\nINSTITUTE NAME:", self.name)
        print("CAMPUS:", self.campus)
        print("CITY:", self.location)
        print("CONTACT US ON:", self.contact_no)
        print("NO OF FACULTIES:", 7)
        print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    
    def add_department(self, department):
        self.departments.append(department)
        print("-----------------------------------------------------------------------")
        print(f"\nDEPARTMENT ADDED: {department.name}")
        print("NOTE: THIS DEPARTMENT WILL DEAL WITH CS COURSES.")
        print("\n-----------------------------------------------------------------------")
    

# 'Department 'class (no inheritance from University)
class Department:
    def __init__(self, name, campus):
        self.name = name
        self.campus = campus
        self.courses = []


#'Degree'class (no inheritance from Department)
class Degree:
    def __init__(self, name):
        self.name = name
        self.courses = []
        print(f"DEGREE ADDED: {self.name}")  
        print("\n-----------------------------------------------------------------------\n")
    
    def add_course(self, course):
        self.courses.append(course)
        print(f"COURSE ADDED TO {self.name}: {course}")

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

    def list_courses(self):
        return self.courses


# Base class Person
class Person:
    def __init__(self, name, age, contact, role):
        self.name = name
        self.age = age
        self.contact = contact
        self.role = role


# 'Teacher' class inheriting from Person
class Teacher(Person):
    def __init__(self, name, age, contact, role, departments):
        super().__init__(name, age, contact, role)
        self.departments = departments  # A list of departments the teacher is associated with.
    
    def get_departments_teacher(self):
        return self.departments


# 'Student' class inheriting from Person
class Student(Person):
    def __init__(self, name, age, contact, role, department, semester, ag_no, degree):
        super().__init__(name, age, contact, role)
        self.department = department  # The department the student belongs to
        self.semester = semester
        self.ag_no = ag_no
        self.degree = degree  # Pass the degree object
        self.courses = []  # Will hold the courses based on the degree and semester
        
        if self.semester == "5th":
            self.courses = self.degree.list_courses()  # Get courses from the degree
        else:
            self.courses = ["Courses not available for this semester"]
    
    def list_student_courses(self):
        return self.courses


# Value Assigning

# Create a university object
univ = University("THE UNIVERSITY OF AGRICULTURE", "MAIN CAMPUS", "FAISALABAD", "(041)9200161")
univ.univ_info()

# Create a department
cs_department = Department("COMPUTER SCIENCE", "MAIN CAMPUS")

# Add the department to the university
univ.add_department(cs_department)

# Add some courses to the SE degree
degree_dep = Degree("SOFTWARE ENGINEERING")
degree_dep.add_course("Software Metrics")
degree_dep.add_course("Natural Language Processing")
degree_dep.add_course("Web Programming")

print("-----------------------------------------------------------------------\n")

# Create a student and assign them to a department and courses
student1 = Student("ASFANDYAR", 20, "031-874", "Student", cs_department.name, "5th", "2024-ag-8063", degree_dep)
student2 = Student("ZAHRA", 19, "032-587", "Student", cs_department.name, "5th", "2024-ag-8078", degree_dep)

# List courses in the CS department for the student
print(f"Courses in {degree_dep.name} for {student1.semester} semester:\n{student1.list_student_courses()}")
print("\n-----------------------------------------------------------------------") 

# Create a teacher and assign them to a department
teacher1 = Teacher("MUHAMMAD MUSTAFA", 35, "034-154", "Professor", [cs_department.name])
print(f"Professor {teacher1.name} teaches in department:\nDEPARTMENT:{teacher1.get_departments_teacher()}\nDEGREE:{degree_dep.name}")
print("\n-----------------------------------------------------------------------") 

# Print student information
print(f"Student: {student1.name}\nContact no:{student1.contact}\nRole in university:{student1.role}\nDegree:{student1.degree.name}\nSemester:{student1.semester}\nDepartment:{student1.department}\nEnrolled in courses:\n{student1.list_student_courses()}\n")
print(f"Student: {student2.name}\nContact no:{student2.contact}\nRole in university:{student2.role}\nDegree:{student2.degree.name}\nSemester:{student2.semester}\nDepartment:{student2.department}\nEnrolled in courses:\n{student2.list_student_courses()}")

print("\n-----------------------------------------------------------------------") 
