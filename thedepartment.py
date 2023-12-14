import sqlite3

conn = sqlite3.connect("thedepartment.db")
cursor = conn.cursor()
conn.execute("PRAGMA foreign_keys = 1")
sql = ""
values = []
value = ()

#Strings to create each table
createEmployeeTableQuery = """CREATE TABLE IF NOT EXISTS [employees] (
    [id] integer PRIMARY KEY AUTOINCREMENT,
    [last_name] nvarchar(255),
    [first_name] nvarchar(255),
    [middle_name] nvarchar(255))"""

createDivisionTableQuery = """CREATE TABLE IF NOT EXISTS [division] (
  [id] integer PRIMARY KEY AUTOINCREMENT,
  [division_name] nvarchar(255),
  [manager_employee_id] integer,
  FOREIGN KEY(manager_employee_id) REFERENCES employees(id))"""

createDepartmentTableQuery = """CREATE TABLE IF NOT EXISTS [department] (
  [id] integer PRIMARY KEY AUTOINCREMENT,
  [department_name] nvarchar(255),
  [division_id] integer,
  [manager_employee_id] integer,
  FOREIGN KEY(division_id) REFERENCES division(id),
  FOREIGN KEY(manager_employee_id) REFERENCES employees(id))"""

createProjectTableQuery = """CREATE TABLE IF NOT EXISTS [project] (
  [id] integer PRIMARY KEY AUTOINCREMENT,
  [project_name] nvarchar(255))"""

createDepartmentAssignmentTableQuery = """CREATE TABLE IF NOT EXISTS [department_assignment] (
  [assigned_employee_id] integer,
  [assigned_department_id] integer,
  FOREIGN KEY(assigned_employee_id) REFERENCES employees(id),
  FOREIGN KEY(assigned_department_id) REFERENCES department(id))"""

createProjectAssignmentTableQuery = """CREATE TABLE IF NOT EXISTS [project_assignment] (
  [assigned_employee_id] integer,
  [assigned_project_id] integer,
  FOREIGN KEY(assigned_employee_id) REFERENCES employees(id),
  FOREIGN KEY(assigned_project_id) REFERENCES project(id))"""
  
#Create Tables
cursor.execute(createDivisionTableQuery)
cursor.execute(createEmployeeTableQuery)
cursor.execute(createDepartmentTableQuery)
cursor.execute(createProjectTableQuery)
cursor.execute(createDepartmentAssignmentTableQuery)
cursor.execute(createProjectAssignmentTableQuery)

#Insert Sample Data to Employee Table
sql = "INSERT INTO employees (last_name, first_name, middle_name) \
  values (:values(0), :values(1), :values(2))"
values = [
  ("Escolar", "Ferdinand", "Camba"),
  ("Danganan", "Duvall", "Q"),
  ("Bonggal", "Arvin", "W"),
  ("Loma", "Mark", "Y"),
  ("Leonardo", "Rico", "M"),
  ("Bernardo", "Kathryn", "A"),
  ("Padilla", "Daniel", "J"),
  ("Diaz", "Ogie", "M")
  ]
cursor.executemany(sql,values)
conn.commit()
print(f"Employee Table: {cursor.rowcount} records inserted")

#Insert Sample Data to Project Table
sql = "INSERT INTO project (project_name) values (:values(0))"
values = [
  ("Building Renovation",),
  ("Chistmas Decoration",)
  ]
cursor.executemany(sql,values)
conn.commit()
print(f"Project Table: {cursor.rowcount} records inserted")

#Insert Sample Data to Division Table
sql = "INSERT INTO division (division_name, manager_employee_id) \
  values (:values(0), :values(1))"
values = [
  ("Services",1),
  ("Finance",2)
  ]
cursor.executemany(sql,values)
conn.commit()
print(f"Divison Table: {cursor.rowcount} records inserted")

#Insert Sample Data to Department Table
sql = "INSERT INTO department (department_name, division_id, manager_employee_id) \
  values (:values(0), :values(1), :values(2))"
values = [
  ("IT",1,3),
  ("Sales",1,4),
  ("Accounting",2,5)
  ]
cursor.executemany(sql,values)
conn.commit()
print(f"Department Table: {cursor.rowcount} records inserted")

#Insert Sample Data to Department Assignment Table
sql = "INSERT INTO department_assignment \
  values (:values(0), :values(1))"
values = [
  (6,1),
  (7,2),
  (8,2)
  ]
cursor.executemany(sql,values)
conn.commit()
print(f"Department Assignment Table: {cursor.rowcount} records inserted")

#Insert Sample Data to  Project Assignment Table
sql = "INSERT INTO project_assignment \
  values (:values(0), :values(1))"
values = (6,1)
cursor.execute(sql,values)
conn.commit()
print(f"Project Assignment Table: {cursor.rowcount} records inserted")