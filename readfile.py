from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Connection string
connection_string = "sqlite:///mydb2.db"

# Create the engine
engine = create_engine(connection_string)

# Define the base class using declarative_base
Base = declarative_base()

# Define the Student class
class Student(Base):
    __tablename__ = 'student'
    student_id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    date_of_birth = Column(Date, nullable=False)

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Read Operations

# 1. Query all students
students = session.query(Student).all()
print("All Students:")
for student in students:
    print(f"ID: {student.student_id}, Name: {student.name}, Date of Birth: {student.date_of_birth}")

# 2. Query a student by student_id
student = session.query(Student).filter_by(student_id=101).first()
if student:
    print(f"\nStudent with ID 101: Name: {student.name}, Date of Birth: {student.date_of_birth}")
else:
    print("\nStudent with ID 101 not found")

# 3. Query students born after 2000
students = session.query(Student).filter(Student.date_of_birth > datetime.strptime('2000-01-01', '%Y-%m-%d').date()).all()
print("\nStudents born after 2000:")
for student in students:
    print(f"ID: {student.student_id}, Name: {student.name}, Date of Birth: {student.date_of_birth}")
