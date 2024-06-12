from sqlalchemy import create_engine, Column, String, Integer, CHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, first, last, gender, age):
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.ssn}) {self.firstname} {self.lastname} ({self.gender},{self.age})"


class Thing(Base):
    __tablename__="things"

    tid= Column("tid", Integer, primary_key= True)
    description= Column("description", String)
    owner= Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner):
        self.tid=tid
        self.description= description
        self.owner= owner
    
    def __repr__(self):
        return f"({self.tid}) {self.description} owned by {self.owner}"


# Create an SQLite database
engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

#Add initial data
person = Person(12312, "Mike", "Smith", "m", 35)
session.add(person)
session.commit()

p1 = Person(31234, "Anna", "Swift", "f", 40)
p2 = Person(32322, "James", "Blunt", "m", 35)
p3 = Person(45334, "Mona", "Smith", "f", 44)

session.add(p1)
session.add(p2)
session.add(p3)
session.commit()

t1= Thing(1, "Car", p1.ssn)
t2= Thing(2, "laptop", p1.ssn)
t3= Thing(3, "PS5", p2.ssn)
t4= Thing(4, "Tool", p3.ssn)
t5= Thing(5, "Book", p3.ssn)

session.add(t1)
session.add(t2)
session.add(t3)
session.add(t4)
session.add(t5)
session.commit()



