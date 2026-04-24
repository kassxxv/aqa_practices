import allure
import pytest
from pony.orm import db_session
from lesson_29.homework_29 import db, Student, Course, add_student_and_enroll, update_student_email, delete_student, init_db


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    init_db()


@allure.feature("Database Connection")
def test_db_connection():
    with allure.step("Check that provider is postgres"):
        assert db.provider_name == 'postgres'
    with allure.step("Check that schema is not None"):
        assert db.schema is not None


@allure.feature("Student Enrollment")
@db_session
def test_insert_student_and_course():
    with allure.step("Create course if it does not exist"):
        course_title = "Docker Test Course"
        if not Course.get(title=course_title):
            Course(title=course_title, description="Course for testing Docker integration")

    with allure.step("Remove existing test student if present"):
        test_name = "Docker Test Student"
        test_email = "docker.test@example.com"
        existing = Student.get(email=test_email)
        if existing:
            existing.delete()
            db.flush()

    with allure.step("Add student and enroll in course"):
        add_student_and_enroll(test_name, test_email, course_title)

    with allure.step("Assert student exists and is enrolled in the course"):
        student = Student.get(email=test_email)
        assert student is not None
        assert student.name == test_name
        assert any(c.title == course_title for c in student.courses)


@allure.feature("Data Retrieval")
@db_session
def test_select_data():
    with allure.step("Select all students from the database"):
        students = Student.select()[:]
        assert len(students) >= 0

    with allure.step("Select all courses from the database"):
        courses = Course.select()[:]
        assert len(courses) >= 0


@allure.feature("Student Update")
@db_session
def test_update_student():
    with allure.step("Create test student with old email"):
        test_name = "Update Me"
        old_email = "old@example.com"
        new_email = "new@example.com"

        if not Student.get(name=test_name):
            Student(name=test_name, email=old_email)
        else:
            Student.get(name=test_name).email = old_email
        db.flush()

    with allure.step("Update student email"):
        update_student_email(test_name, new_email)

    with allure.step("Assert email was updated correctly"):
        student = Student.get(name=test_name)
        assert student.email == new_email


@allure.feature("Student Deletion")
@db_session
def test_delete_student():
    with allure.step("Create test student to be deleted"):
        test_name = "Delete Me"
        test_email = "delete.me@example.com"
        if not Student.get(name=test_name):
            Student(name=test_name, email=test_email)
        db.flush()

    with allure.step("Delete the student"):
        delete_student(test_name)

    with allure.step("Assert student no longer exists in the database"):
        student = Student.get(name=test_name)
        assert student is None