import random
from faker import Faker
from pony.orm import Database, Required, Set, db_session, select

fake = Faker()

db = Database()
db.bind(provider="postgres", user="postgres", password="", host="localhost", database="postgres")


class Student(db.Entity):
    name = Required(str, 100)
    email = Required(str, 150, unique=True)
    courses = Set("Course")


class Course(db.Entity):
    title = Required(str, 150)
    description = Required(str, 300)
    students = Set("Student")

db.generate_mapping(create_tables=True)


@db_session
def seed_database():
    if Student.select().count() > 0:
        return

    courses = [
        Course(title="Python Basics", description="Python for child"),
        Course(title="AQA with Python", description="Python automation"),
        Course(title="AQA with JavaScript", description="Js automation"),
        Course(title="Manual Testing", description="About testing in web and mobile"),
        Course(title="SQL Basics", description="About SQL"),
    ]

    all_courses = list(Course.select())
    for _ in range(20):
        student = Student(name=fake.name(), email=fake.unique.email())
        student.courses = set(random.sample(all_courses, k=random.randint(1, 3)))


@db_session
def add_student_and_enroll(name: str, email: str, course_title: str):
    course = Course.get(title=course_title)
    if not course:
        return
    student = Student(name=name, email=email)
    student.courses.add(course)
    print(f"Added '{student.name}' to '{course.title}'")


@db_session
def get_students_by_course(course_title: str):
    course = Course.get(title=course_title)
    if not course:
        return
    print(f"Students in '{course.title}':")
    for s in course.students:
        print(f"  {s.id}. {s.name} — {s.email}")


@db_session
def get_courses_by_student(student_name: str):
    student = Student.get(name=student_name)
    if not student:
        return
    print(f"Courses for '{student.name}':")
    for c in student.courses:
        print(f"  {c.id}. {c.title}")


@db_session
def update_student_email(student_name: str, new_email: str):
    student = Student.get(name=student_name)
    if not student:
        return
    student.email = new_email
    print(f"Updated email for '{student.name}' to {new_email}")


@db_session
def update_course_description(course_title: str, new_description: str):
    course = Course.get(title=course_title)
    if not course:
        return
    course.description = new_description
    print(f"Updated description for '{course.title}'")


@db_session
def delete_student(student_name: str):
    student = Student.get(name=student_name)
    if not student:
        return
    student.delete()
    print(f"Deleted '{student_name}'")


if __name__ == "__main__":
    seed_database()

    add_student_and_enroll("Filip Fylyp", "fylyp.filip@student", "Python Basics")

    get_students_by_course("Python Basics")
    get_courses_by_student("Filip Fylyp")

    update_student_email("Filip Fylyp", "filip.fylypio@gmail.com")
    update_course_description("Python Basics", "not only about python but also testing basics")
    delete_student("Filip Fylyp")

    get_students_by_course("Python Basics")