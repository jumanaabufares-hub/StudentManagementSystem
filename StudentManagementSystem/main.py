from webbrowser import get

import psycopg
import os
#for password security
from dotenv import load_dotenv
load_dotenv()

#connect code to Student postegreSQL db:
print("Starting DB connection...", flush=True)
connect=psycopg.connect(
    dbname="student_management",
    user="postgres", 
    password=os.environ["PASSWORD"], 
    host= "localhost", 
    port= "5433",
    connect_timeout=5
    )
print("DB Connected!")


#retreive table 
def getAllStudents(connect):
    #used cursor to allow python to send sql queries to db
    cursor=connect.cursor()
    cursor.execute("SELECT * FROM students")
    #fetchall stores the result in a list
    records=cursor.fetchall();
    #print each student record (row) to read data
    for record in records: print (record)
    cursor.close()

#add a student record
def addStudent(connect, first_name, last_name, email, enrollment_date):
    cursor = connect.cursor()

    cursor.execute(
        """
        INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);
        """, (first_name, last_name, email, enrollment_date)
    )
    connect.commit() #permanently adds row
    cursor.close()


# edit an email
def updateStudentEmail(connect,student_id, email):
    cursor=connect.cursor()
    cursor.execute(
        """
        UPDATE students
        SET email= %s
        WHERE student_id= %s
        """, (email, student_id)
    )
    connect.commit()
    cursor.close()

    
# delete a student record
def deleteStudent(connect, student_id):
    cursor = connect.cursor()
    cursor.execute(
        """
        DELETE FROM students 
        WHERE student_id = %s;
        """, (student_id,)
    )
    connect.commit()
    cursor.close()


#test create
#print("\nTesting create and read:")
#addStudent(connect, "Jumana", "Ab", "jumana.ab@example.com", "2026-11-13")
#getAllStudents(connect)

# test update
#print("\nTesting update:")
#updateStudentEmail(connect, 4, "jumana.abufares@example.com")
#getAllStudents(connect)

#test delete
print("\nTesting delete:")
deleteStudent(connect, 4)
getAllStudents(connect)

connect.close()
