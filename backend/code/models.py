from __init__ import db
from datetime import datetime

student_assessment = db.Table(
    'student_assessment',
    db.Column('id', db.Integer, nullable=False, primary_key=True),
    db.Column('student_id', db.Integer, db.ForeignKey('students.id')),
    db.Column('assessment_id', db.Integer, db.ForeignKey('assessments.id')),
    db.Column('score', db.Integer)

)


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
    assessments = db.relationship('Assessment', secondary=student_assessment, backref=db.backref(
        'students', cascade="all, delete-orphan", single_parent=True))


class Subject(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


class Assessment(db.Model):
    __tablename__ = 'assessments'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTiem, default=datetime.utcnow)
    subject_id = db.column(db.Integer, db.ForeignKey('subjects.id'))
