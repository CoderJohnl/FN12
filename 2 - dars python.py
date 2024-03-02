import sqlite3 as sql
db = sql.connect("FN12.db")
cursor = db.cursor()
cursor.executescript("""
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS courses;
create table if not exists courses(
   course_id integer primary key autoincrement,
   course_name varchar(20)
);
create table if not exists students(
   student_id integer primary key autoincrement,
   first_name varchar(20),
   last_name varchar(20),
   course_id integer references courses(course_id)
);
insert into courses(course_name) values ("Python"), ("Java"), ("C#")
""")
cursor.execute("""
INSERT INTO students(first_name, last_name, course_id) Values ("Muhammadqodir", "To'xtanazarov", 1);
""")
name = "Sobir"
lastname = "Toxirov"
course_id = 3
cursor.execute(f"""
INSERT INTO students(first_name, last_name, course_id) VALUES ("{name}", "{lastname}", {course_id});
""")
name = "Akram"
lastname = "Sobirov"
course_id = 2
cursor.execute(f"""
INSERT INTO students(first_name, last_name, course_id) VALUES (?, ?, ?);
""", (name, lastname, course_id))
cursor.execute("""
SELECT * FROM courses
""")
courses = cursor.fetchall()
print("Jami kurslar: ")
for course in courses:
    print(course[0], course[1])
cursor.execute("""
SELECT * FROM students
""")
students = cursor.fetchall()
print("Jami studentlar: ")
for student in students:
    print(student[0], student[1])
db.commit()
db.close()