
import psycopg2

def creation():
    conn = psycopg2.connect(database="postgres", user="postgres",password = "test", host="localhost", port = "5432")
    cursor = conn.cursor()
    cursor.execute("SELECT 1") #sample test without table creation
    print(cursor.fetchone())

    cursor = conn.cursor()
    cursor.execute(''"create table employees (Name Text, ID int, Age Int);"'')
    print("table created successfully")

    conn.commit()
    conn.close()
def data():
    conn = psycopg2.connect(database="postgres", user="postgres", password="test", host="localhost", port="5432")
    cursor = conn.cursor()
    cursor.execute("insert into employees (Name,ID,Age) values (%s, %s, %s);", ("John", "1234", "34"))
    print("Data inserted successfully")
    conn.commit()
    conn.close()
def extract():
    conn = psycopg2.connect(database="postgres", user="postgres", password="test", host="localhost", port="5432")
    cursor = conn.cursor()
    cursor.execute("SELECT * from employees;")
    print("Data retrieved successfully")
    show = cursor.fetchall()
    print(show)
    conn.commit()
    conn.close()

data()
extract()