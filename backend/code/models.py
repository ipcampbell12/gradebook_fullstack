from app import db
from datetime import datetime


class Teacher(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80), nullable=False)
    teacher = db.column(db.Integer, db.ForeignKey('teachers.id'))


class Subject(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


class Assessments(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTiem, default=datetime.utcnow)
    subject_id = db.column(db.Integer, db.ForeignKey('subjects.id'))


""" 

CREATE TABLE assessments (
	id SERIAL,
	name TEXT,
    date DATETIME,
	subject_id INTEGER,
	PRIMARY KEY(id),
	FOREIGN KEY(subject_id) REFERENCES subjects(id)
);

CREATE TABLE students_assessments (
	id SERIAL,
	student_id INTEGER,
    assessment_id INTEGER,
    score INTEGER,
	PRIMARY KEY(id),
	FOREIGN KEY(student_id) REFERENCES students(id),
	FOREIGN KEY(assessment_id) REFERENCES assessments(id)
); """
