CREATE TABLE [employees] (
  [id] integer PRIMARY KEY,
  [last_name] nvarchar(255),
  [first_name] nvarchar(255),
  [middle_name] nvarchar(255)
)
GO

CREATE TABLE [division] (
  [id] integer PRIMARY KEY,
  [division_name] nvarchar(255),
  [manager_employee_id] integer
)
GO

CREATE TABLE [department] (
  [id] integer PRIMARY KEY,
  [department_name] nvarchar(255),
  [division_id] integer,
  [manager_employee_id] integer
)
GO

CREATE TABLE [project] (
  [id] integer PRIMARY KEY,
  [project_name] nvarchar(255)
)
GO

CREATE TABLE [department_assignment] (
  [assigned_employee_id] integer,
  [assigned_department_id] integer
)
GO

CREATE TABLE [project_assignment] (
  [assigned_employee_id] integer,
  [assigned_project_id] integer
)
GO

ALTER TABLE [department] ADD FOREIGN KEY ([division_id]) REFERENCES [division] ([id])
GO

ALTER TABLE [department] ADD FOREIGN KEY ([manager_employee_id]) REFERENCES [employees] ([id])
GO

ALTER TABLE [division] ADD FOREIGN KEY ([manager_employee_id]) REFERENCES [employees] ([id])
GO

ALTER TABLE [project_assignment] ADD FOREIGN KEY ([assigned_employee_id]) REFERENCES [employees] ([id])
GO

ALTER TABLE [project_assignment] ADD FOREIGN KEY ([assigned_project_id]) REFERENCES [project] ([id])
GO

ALTER TABLE [department_assignment] ADD FOREIGN KEY ([assigned_employee_id]) REFERENCES [employees] ([id])
GO

ALTER TABLE [department_assignment] ADD FOREIGN KEY ([assigned_department_id]) REFERENCES [department] ([id])
GO
