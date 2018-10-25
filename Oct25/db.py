import sqlite3

def createTable(conn):
      conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY
            (ID INT PRIMARY KEY     NOT NULL,
            NAME           TEXT    NOT NULL,
            AGE            INT     NOT NULL,
            ADDRESS        CHAR(50),
            SALARY         REAL);''')
      print("Table created successfully")

def action(conn):
      conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES (1, 'Paul', 32, 'California', 20000.00 )")

      conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

      conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

      conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

      id = int(input("Enter the id: "))
      name = input("Enter a name: ")
      age = int(input("Enter the age: "))
      address = input("Enter the address: ")
      salary = int(input("Enter a salary: "))
      conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES(?, ?, ?, ?, ?)", (id, name, age, address, salary))
      conn.commit()
      print("Records created successfully")

      cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
      for row in cursor:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("ADDRESS = ", row[2])
            print ("SALARY = ", row[3],"\n")


conn = sqlite3.connect('test.db')
print("Opened database successfully")
createTable(conn)
action(conn)
conn.close()
