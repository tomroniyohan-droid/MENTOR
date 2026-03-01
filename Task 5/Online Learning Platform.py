from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration
    @abstractmethod
    def course_details(self):
        pass

class ProgrammingCourse(Course):
    def course_details(self):
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)
        print("Category: Programming")
        print("Includes coding practice and projects.\n")

class DesignCourse(Course):
    def course_details(self):
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)
        print("Category: Design")
        print("Includes creative tools and design principles.\n")

class MarketingCourse(Course):
    def course_details(self):
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)
        print("Category: Marketing")
        print("Includes digital marketing and branding strategies.\n")
course1 = ProgrammingCourse("Python Basics", "3 Months")
course2 = DesignCourse("Graphic Design", "2 Months")
course3 = MarketingCourse("Digital Marketing", "4 Months")

courses = [course1, course2, course3]
for course in courses:
    course.course_details()