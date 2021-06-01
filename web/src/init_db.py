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
cursor.execute("drop table if exists Classmembers;")

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

# Create a TStudents table (wrapping it in a try-except is good practice)
try:
  cursor.execute(""" CREATE TABLE Classmembers (
      id          integer  AUTO_INCREMENT PRIMARY KEY,
      name        VARCHAR(100) NOT NULL,
      link        VARCHAR(100) NOT NULL
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


query = "insert into Classmembers (name, link) values (%s, %s)"
values = [("Vladimir Altov","http://143.198.73.78/"), ("Ardebilianfard, Sepehr","http://165.232.131.14:3001"),
("Arestakesyan, Ankeen","http://144.126.210.32/"),("Bailon, Felipe","http://143.198.136.37/"),
("Bian, Jiazheng","http://www.biandavid.com/"),("Bissett, Christian","http://143.198.128.150:6543/"),
("Chen, James","http://143.198.57.119/"),("Dastider, Gourab","http://144.126.215.62/"),
("Embucado, Chaztine-Xiana","http://1143.198.59.27/"),("Guan, Tony","http://143.198.76.115/"),
("Gudetti, Jacinth","http://143.198.97.209/"),("Gustafson, Bret","http://143.110.153.51/"),
("Hanna, Aaron","http://144.126.212.235/"),("Hernandez, Andrew","http://www.cvwebring.com/"),
("Hsu, Anwar","anwarhsu.com"),("Vladimir Altov","http://143.198.73.78/"),
("Huang, Eddie","eddieh00.com"),("Vladimir Altov","http://143.198.73.78/"),
("Huang, Isis","http://64.227.107.46/"),("Huang, Hanjie","http://161.35.229.252/"),
("Johnson, Kimberly","43.198.71.181"),("Kaharudin, Jason","http://178.128.96.97/"),
("Kahr, Andrew","http://165.232.131.189/"),("Kim, Iris","http://143.198.136.173/"),
("Kim, Jake","http://128.199.3.204/"),("Kim, Stephen","http://kimsternator.games/"),
("Koshmerl, Damon","http://143.198.111.59/"),("Kragh, Mark","http://167.99.122.242/"),
("Lee, Charles","http://35.185.251.8/"),("Liu, Zhenwei","http://164.90.144.97/"),
("Malgeri, John","http://161.35.228.30/"),("Manalad, Christian","http://165.232.141.195/"),
("Nazemi, Ariane","http://143.198.236.89/"),("Noble, Emerson","http://143.110.234.12/"),
("On, Dong","http://128.199.15.251/"),("Raha, Anjuman","http://161.35.239.252/"),
("Sanchez, Manuel","http://165.232.153.255/"),("Tang, Chonghao","http://165.232.157.102/"),
("Malgeri, John","http://161.35.228.30/"),("Manalad, Christian","http://165.232.141.195/"),
("Tong, Hung","http://161.35.54.86/"),("Villegas, Carl","http://143.198.59.67/"),
("Yang, Frederick","http://143.198.232.38/"),("Yim, Aaron","http://165.232.143.129/"),
("Younessi, Kasra","http://64.227.101.230/"),
("Zhang, Hang","http://144.126.221.136/"),
("Zhang, Siyuan","http://143.198.98.101")]
cursor.executemany(query, values)
db.commit()


cursor.execute("select * from Classmembers;")
print('---------- DATABASE INITIALIZED ----------')
[print(x) for x in cursor]

db.close()