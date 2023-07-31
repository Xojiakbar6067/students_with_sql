import sqlite3
connection=sqlite3.connect('mydatabase.db')
sql=connection.cursor()
sql.execute('CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY, name TEXT, age INTEGER, grade TEXT);')
def add_student(name, age, grade):
    sql.execute(f'INSERT INTO students(name, age, grade) VALUES ("{name}", {age}, "{grade}");')
    connection.commit()
    print(f'студент {name} добавлен в таблицу')
def get_student_by_name(name):
    check = sql.execute('SELECT name FROM students WHERE name=?;', (name,))
    if check.fetchone():
        print(sql.execute(f'SELECT name, age, grade FROM students WHERE name="{name}";').fetchall())
    # j = []
    # for i in sql.execute('SELECT name FROM students').fetchall():
    #     j += i
    # if name in j:
    #     print(sql.execute(f'SELECT name, age, grade FROM students WHERE name="{name}";').fetchall())
    else:
        print(f'студент под именем {name} нету в таблице')
def update_student_grade(new_grade, name):
    j = []
    for i in sql.execute('SELECT name FROM students').fetchall():
        j += i
    if name in j:
        sql.execute(f'UPDATE students SET grade="{new_grade}" WHERE name="{name}";')
        connection.commit()
        print(f"оценка студента {name} изменен на {new_grade}")
    else:
        print(f'студент под именем {name} нету в таблице')
def delete_student(name):
    j = []
    for i in sql.execute('SELECT name FROM students').fetchall():
        j += i
    if name in j:
        sql.execute(f'DELETE FROM students WHERE name="{name}";')
        connection.commit()
        print(f'студент по имени {name} удален из таблицы')
    else:
        print(f'студент под именем {name} нету в таблице')
def show_students():
    s=sql.execute('SELECT * FROM students')
    for i in s:
        print(list(i))

while True:
    print('--------------------------','\n''1-добавит студента в таблицу','\n''2-поиск студента','\n''3-изменит оценку студента','\n''4-удалит студента с таблицы','\n''5-показать всех студентов','\n''6-остонавит программу')
    operator=int(input('выбирайте: '))
    if operator==1:
        add_student(name=input('имя студента: ').title(), age=int(input('возраст студента: ')), grade=input("оценка студента: "))
    elif operator==2:
        get_student_by_name(input('имя кого хотите найти: ').title())
    elif operator==3:
        update_student_grade(name=input("имя студента для изменения оценки: ").title(), new_grade=input("новая оценка: "))
    elif operator==4:
        delete_student(input("имя студента которого хотите удалит").title())
    elif operator==5:
        show_students()
    elif operator==6:
        break
    else:
        print("не верное команда!","\n""проверте и ведите заново")
