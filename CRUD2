# Create Operations
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Correct the variable name
connection_string = "sqlite:///mydb2.db"

# Create the engine
engine = create_engine(connection_string)

# Define the base class using declarative_base
Base = declarative_base()

# Define the Student class with a proper class definition
class Student(Base):
    __tablename__ = 'student'
    student_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Convert date_of_birth from string to date
student = Student(student_id=101, name='Ann', date_of_birth=datetime.strptime('1985-04-12', '%Y-%m-%d').date())
session.add(student)
session.commit()

# Convert date_of_birth from string to date for other students
s1 = Student(student_id=202, name='Elena', date_of_birth=datetime.strptime('2001-02-10', '%Y-%m-%d').date())
s2 = Student(student_id=303, name='Mona', date_of_birth=datetime.strptime('2003-04-11', '%Y-%m-%d').date())
s3 = Student(student_id=404, name='Robert', date_of_birth=datetime.strptime('2002-05-22', '%Y-%m-%d').date())
session.add(s1)
session.add(s2)
session.add(s3)
session.commit()

# Read Operations

# 1. Query all students
students = session.query(Student).all()
print("All Students:")
for student in students:
    print(f"ID: {student.student_id}, Name: {student.name}, Date of Birth: {student.date_of_birth}")

print()

student = session.query(Student).filter(Student.name.like("A%")).first()
print(student.name)
student.name= "Simona"
print(student.name)
session.commit()
# 3. Query students born after 2000
students = session.query(Student).filter(Student.date_of_birth > datetime.strptime('2000-01-01', '%Y-%m-%d').date()).all()
print("\nStudents born after 2000:")
for student in students:
    print(f"ID: {student.student_id}, Name: {student.name}, Date of Birth: {student.date_of_birth}")
