# Import MySQL Connector Driver
import mysql.connector as mysql

# Load the credentials from the secured .env file
import os
from dotenv import load_dotenv
load_dotenv('credentials.env')

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST'] # must 'localhost' when running this script outside of Docker

# Connect to the database
db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
cursor = db.cursor()

# # CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!!
cursor.execute("drop table if exists Personal;")
cursor.execute("drop table if exists Education;")
cursor.execute("drop table if exists Project;")
cursor.execute("drop table if exists Link;")
cursor.execute("drop table if exists Users;")

# Create a TStudents table (wrapping it in a try-except is good practice)
try:
  cursor.execute(""" CREATE TABLE Personal (
    id          integer  AUTO_INCREMENT PRIMARY KEY,
    first_name  VARCHAR(50) NOT NULL,
    last_name   VARCHAR(50) NOT NULL,
    email       VARCHAR(50) NOT NULL
    );
  """)
except:
  print("Personal table already exists. Not recreating it.")

# Create a TStudents table (wrapping it in a try-except is good practice)
try:
  cursor.execute(""" CREATE TABLE Education (
    id      integer  AUTO_INCREMENT PRIMARY KEY,
    school  VARCHAR(50) NOT NULL,
    degree  VARCHAR(50) NOT NULL,
    major   VARCHAR(50) NOT NULL,
    date    integer NOT NULL
  );
  """)
except:
  print("Education table already exists. Not recreating it.")

# Create a TStudents table (wrapping it in a try-except is good practice)
try:
  cursor.execute(""" CREATE TABLE Project (
    id           integer  AUTO_INCREMENT PRIMARY KEY,
    title        VARCHAR(50) NOT NULL,
    description  VARCHAR(50) NOT NULL,
    link         VARCHAR(50) NOT NULL,
    image_src    VARCHAR(50) NOT NULL
  );
  """)
except:
  print("Education table already exists. Not recreating it.")

# Create a TStudents table (wrapping it in a try-except is good practice)
try:
  cursor.execute(""" CREATE TABLE Link (
    id  integer  AUTO_INCREMENT PRIMARY KEY,
    teamURL VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL
    );
  """)
except:
  print("Links table already exists. Not recreating it.")


# Create a TStudents table (wrapping it in a try-except is good practice)
try:
  cursor.execute(""" CREATE TABLE Users (
      id          integer  AUTO_INCREMENT PRIMARY KEY,
      first_name  VARCHAR(50) NOT NULL,
      last_name   VARCHAR(50) NOT NULL,
      email       VARCHAR(50) NOT NULL,
      comment    VARCHAR(50) NOT NULL,
      created_at  TIMESTAMP
    );
  """)
except:
  print("Users table already exists. Not recreating it.")

# Insert Records
query = "insert into Personal (first_name, last_name, email) values (%s, %s, %s)"
values = ("Myo Myint","Htoo","mhtoo@ucsd.edu")
cursor.execute(query, values)
db.commit()

# Selecting Records
cursor.execute("select * from Personal;")
print('---------- DATABASE INITIALIZED ----------')
[print(x) for x in cursor]


query = "insert into Education (school, degree, major, date) values (%s, %s, %s, %s)"
values = ('UC San Diego','Bachelor','Computer Engineering', '2021')
cursor.execute(query, values)
db.commit()

cursor.execute("select * from Education;")
print('---------- DATABASE INITIALIZED ----------')
[print(x) for x in cursor]

query = "insert into Project(title, description, link, image_src) value (%s, %s, %s, %s)"
value = ('EZTrader','A educational trading platform', 'IN PROGRESS', 'IN PROGRESS')
cursor.execute(query, value)
db.commit()

cursor.execute("select * from Project;")
print('---------- DATABASE INITIALIZED ----------')
[print(x) for x in cursor]

query = "insert into Link(teamURL, name) values (%s, %s)"
values = ('128.199.10.10', "Tan")
cursor.execute(query, values)
db.commit()

query = "insert into Link(teamURL, name) values (%s, %s)"
values = ("165.232.152.55", "Hector")
cursor.execute(query, values)
db.commit()

query = "insert into Link(teamURL, name) values (%s, %s)"
values = ("161.35.232.250", "Adib")
cursor.execute(query, values)
db.commit()

cursor.execute("select * from Link;")
print('---------- DATABASE INITIALIZED ----------')
[print(x) for x in cursor]

db.close()