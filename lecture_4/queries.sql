.timer ON
-- Table of students with basic personal information
CREATE TABLE IF NOT EXISTS students(
	id INTEGER PRIMARY KEY,
	name TEXT,
	birth_year INTEGER
);

-- Table of grades, linked to students by foreign key
CREATE TABLE IF NOT EXISTS grades (
	id INTEGER PRIMARY KEY,
	student_id INTEGER NOT NULL REFERENCES students(id),
	grade INTEGER,
    subject TEXT
);
GO
-- Clear existing data to keep inserts simple
DELETE FROM students;
DELETE FROM grades;
GO

-- Seed example students
INSERT INTO students (name, birth_year) VALUES
('John Doe', 1990),
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);

-- Seed example grades for different subjects
INSERT INTO grades (student_id, subject, grade) VALUES
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75),
(2, 'History', 83),
(2, 'English', 79),
(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 89),
(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88),
(6, 'Science', 72),
(6, 'Math', 78),
(6, 'English', 81),
(7, 'Art', 94),
(7, 'Science', 87),
(7, 'Math', 90),
(8, 'History', 77),
(8, 'Math', 83),
(8, 'Science', 80),
(9, 'English', 96),
(9, 'Math', 89),
(9, 'Art', 92),
(10, 'Math', 86),
(10, 'English', 88),
(10, 'Science', 85);

CREATE INDEX IF NOT EXISTS grade_Idx ON grades (grade);
CREATE INDEX IF NOT EXISTS student_name_Idx ON students (name);
CREATE INDEX IF NOT EXISTS student_birth_year_Idx ON students (birth_year);
CREATE INDEX IF NOT EXISTS grade_student_id_Idx ON grades (student_id);
            
-- Find all grades for a specific student
SELECT grade FROM grades JOIN students ON grades.student_id = students.id
WHERE students.name = 'Alice Johnson';

-- Average grade per student
SELECT name, ROUND(AVG(grade), 2)
FROM grades JOIN students ON grades.student_id = students.id
GROUP BY name;

-- List all students born after 2004
SELECT *
FROM students
WHERE birth_year > 2004;

-- Average grade per subject
SELECT subject,
       ROUND(AVG(grade), 2)
FROM grades
GROUP BY subject;

-- Top 3 students with the highest average grade
SELECT name,
       ROUND(AVG(grade), 2)
FROM grades
JOIN students ON grades.student_id = students.id
GROUP BY name
ORDER BY AVG(grade) DESC
LIMIT 3;

-- Students with at least one grade below 80
SELECT name
FROM grades
JOIN students ON grades.student_id = students.id
WHERE grade < 80
GROUP BY name;

.timer OFF