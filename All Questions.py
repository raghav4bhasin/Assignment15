##Q.1- Write a python script to create a databse of students named Students.
print('\tQuestion 1')
import sqlite3

try:
    conn = sqlite3.connect('Students.db')
    cursor = conn.cursor()
    query = 'CREATE table Students(RollNo int Primary Key, Name varchar(50), \
    Marks int CHECK(Marks >= 0 AND Marks <= 100))'

    cursor.execute(query)
    print('Table created successfully!!')
    conn.commit()

except sqlite3.DatabaseError as e:
    if conn:
        conn.rollback()
        print('Problem occured: ', e)
    
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print('DONE!!')


##Q.2-Take students name and marks(between 0-100) as input from user 10 times using loops.
print(' ')
print('\tQuestion 2')    
lst_data = []

for i in range(1, 11):
    print('Student ',i)
    name = input("\tEnter Student's name: ")
    marks = int(input("\tEnter Student's marks: "))
    lst_data.append((i, name, marks))
    print(' ')


##Q.3- Add these values in two columns named "Name" and "Marks" with the appropriate data type.
print('\tQuestion 3')

import sqlite3

try:
    conn = sqlite3.connect('Students.db')
    cursor = conn.cursor()
    for i in range(10):
        query = 'Insert into Students(RollNo, Name, Marks) \
        values(?, ?, ?)'

        

        cursor.executemany(query, lst_data)
        conn.commit()

except sqlite3.IntegrityError as e:
    conn.rollback()
    print("ERROR!! Invalid Marks.")

finally:
    cursor.close()
    conn.close()
    print('DONE!!')


##Q.4- Print the names of all the students who scored more than 80 marks.

print('\tQuestion 4')

import sqlite3

try:
    conn = sqlite3.connect('Students.db')
    cursor = conn.cursor()
    qyery = 'Select Name from Students where Marks > 80'
    cursor.executemany(query)
    conn.commit()

except:
    conn.rollback()
    print("ERROR!!")

finally:
    cursor.close()
    conn.close()
    print('DONE!!')
