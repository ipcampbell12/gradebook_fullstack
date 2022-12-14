CREATE TABLE teachers (
	id SERIAL,
	first TEXT,
	last TEXT,
	email TEXT,
	password TEXT,
	PRIMARY KEY(id)
);

CREATE TABLE students (
	id SERIAL,
	first TEXT,
	last TEXT,
	teacher_id INTEGER, 
	PRIMARY KEY(id),
    FOREIGN KEY(teacher_id) REFERENCES teachers(id)
);

CREATE TABLE subjects (
	id SERIAL,
	name TEXT,
	PRIMARY KEY(id)
);

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
);

-- Teacher Data
INSERT INTO teachers (first,last,email,password)
VALUES ('Jane','Harper','jharper@school.edu','Iamjane23')
       ('Daniel','Calderon','dcalderon@school.edu','Daniel246')
       ('Fabiola','Velasquez','fvelasquez@school.edu','FabVas345');


--Student Data
INSERT INTO students (first, last, teacher_id)
VALUES  ('Brian','Smithy',1),
        ('Stephanie','Walker',2),
        ('Stacy','Perez',3),
        ('Dacia','San Juan',1),
        ('Milly','Bobby Brown',2),
        ('Dustin','Rodrigues',3),
        ('Antoine','Vincente',1),
        ('Leslie','Hernandez',2),
        ('Veronica','Miller',3),
        ('Seville','Hanson',1),
        ('Maria','Guadalupe',2),
        ('Harry','Potter',3);

--Subject Data
INSERT INTO subjects (name)
VALUES ('Mathematics'),
        ('Language Arts'),
        ('Science'),
        ('Social Studies'),
        ('Music');

INSERT INTO assessments (name, date, subject_id )
VALUES ('Mdule 1 Test','9/25/22',1),
        ('Mdule 2 Test','10/15/22',1),
        ('Mdule 3 Test','11/19/22',1),
        ('Mdule 4 Test','12/13/22',1),
        ('Unit 1 Test','10/01/22',2),
        ('Unit 2 Test','11/21/22',2),
        ('Earth Test', '10/15/22',3),
        ('Oregon Trail Test', '12/19/22',4),
        ('Multiplication Text','10/20/22',1);

--subjects = 9, students = 12 
INSERT INTO students_assessments (student_id, assessment_id,score)
VALUES(1,1,3),
    (2,1,1),
    (3,1,2),
    (4,1,3),
    (6,1,3),
    (6,1,1),
    (7,1,3),
    (8,1,2),
    (9,1,2),
    (10,1,3),
    (11,1,4),
    (12,1,2),
    (1,2,1),
    (2,2,1),
    (3,2,1),
    (4,2,1),
    (6,2,3),
    (6,2,1),
    (7,2,4),
    (8,2,2),
    (9,2,2),
    (10,2,3),
    (11,2,4),
    (12,2,3);
 
--Get the scores and and student names and teacher anmes for the first test
SELECT CONCAT(s.first,' ', s.last), s.id AS student, t.last, sa.score, a.name FROM students s
JOIN teachers t
ON s.teacher_id = t.id
JOIN students_assessments sa
ON s.id = sa.student_id
JOIN assessments a 
ON a.id = sa.assessment_id
WHERE a.name LIKE '%1%';

--SELECT all the assessments and their subjects
SELECT a.name, a.date, s.name FROM assessments a
JOIN subjects s 
ON s.id = a.subject_id;

--SELECT all the math assessments
SELECT a.name, a.date, s.name FROM assessments a
JOIN subjects s 
ON s.id = a.subject_id
WHERE s.name LIKE 'Math%';


--SELECT all the students and their teachers 
SELECT s.first, s.last, t.last AS teacher FROM students s
JOIN teachers t 
ON t.id = s.teacher_id;

--SELECT all students who's teacher is Calderon
--Should return Stephanie, Milly, Leslie, Maria
SELECT s.first, s.last, t.last AS teacher FROM students s
JOIN teachers t 
ON t.id = s.teacher_id
WHERE t.last = 'Calderon'; 

--Get the scores and and student names and teacher names for the first test
SELECT CONCAT(s.first,' ', s.last) AS student, t.last AS teacher, sa.score, a.name FROM students s
JOIN teachers t
ON s.teacher_id = t.id
JOIN students_assessments sa
ON s.id = sa.student_id
JOIN assessments a 
ON a.id = sa.assessment_id
WHERE a.name LIKE '%1%';

