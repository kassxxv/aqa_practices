import pytest
from pony.orm import db_session, select
from homework_29 import db, Student, Course, add_student_and_enroll, update_student_email, delete_student, init_db

@pytest.fixture(scope="session", autouse=True)
def setup_db():
    init_db()

def test_db_connection():
    assert db.provider_name == 'postgres'
    assert db.schema is not None

@db_session
def test_insert_student_and_course():
    course_title = "Docker Test Course"
    if not Course.get(title=course_title):
        Course(title=course_title, description="Course for testing Docker integration")
    
    test_name = "Docker Test Student"
    test_email = "docker.test@example.com"

    existing = Student.get(email=test_email)
    if existing:
        existing.delete()
        db.flush()

    add_student_and_enroll(test_name, test_email, course_title)
    
    student = Student.get(email=test_email)
    assert student is not None
    assert student.name == test_name
    assert any(c.title == course_title for c in student.courses)

@db_session
def test_select_data():
    students = select(s for s in Student)[:]
    assert len(students) >= 0
    
    courses = select(c for c in Course)[:]
    assert len(courses) >= 0

@db_session
def test_update_student():
    test_name = "Update Me"
    old_email = "old@example.com"
    new_email = "new@example.com"
    
    # Setup
    if not Student.get(name=test_name):
        Student(name=test_name, email=old_email)
    else:
        s = Student.get(name=test_name)
        s.email = old_email
    db.flush()

    update_student_email(test_name, new_email)
    
    student = Student.get(name=test_name)
    assert student.email == new_email

@db_session
def test_delete_student():
    test_name = "Delete Me"
    test_email = "delete.me@example.com"

    if not Student.get(name=test_name):
        Student(name=test_name, email=test_email)
    db.flush()

    delete_student(test_name)
    
    student = Student.get(name=test_name)
    assert student is None
