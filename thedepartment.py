import sqlite3

conn = sqlite3.connect("thedepartment.db")
cursor = conn.cursor()
conn.execute("PRAGMA foreign_keys = 1")

createEmployeeTableQuery = """CREATE TABLE IF NOT EXISTS [employees] (
    [id] integer PRIMARY KEY,
    [last_name] nvarchar(255),
    [first_name] nvarchar(255),
    [middle_name] nvarchar(255))"""

createDivisionTableQuery = """CREATE TABLE IF NOT EXISTS [division] (
  [id] integer PRIMARY KEY,
  [division_name] nvarchar(255),
  [manager_employee_id] integer,
  FOREIGN KEY(manager_employee_id) REFERENCES employees(id))"""

createDepartmentTableQuery = """CREATE TABLE IF NOT EXISTS [department] (
  [id] integer PRIMARY KEY,
  [department_name] nvarchar(255),
  [division_id] integer,
  [manager_employee_id] integer,
  FOREIGN KEY(division_id) REFERENCES division(id),
  FOREIGN KEY(manager_employee_id) REFERENCES employees(id))"""

createProjectTableQuery = """CREATE TABLE IF NOT EXISTS [project] (
  [id] integer PRIMARY KEY,
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
  

print(f"{createDivisionTableQuery}")
print(f"{createEmployeeTableQuery}")
print(f"{createDepartmentTableQuery}")
print(f"{createProjectTableQuery}")
print(f"{createDepartmentAssignmentTableQuery}")
print(f"{createProjectAssignmentTableQuery}")


cursor.execute(createDivisionTableQuery)
cursor.execute(createEmployeeTableQuery)
cursor.execute(createDepartmentTableQuery)
cursor.execute(createProjectTableQuery)
cursor.execute(createDepartmentAssignmentTableQuery)
cursor.execute(createProjectAssignmentTableQuery)
#conn.commit()