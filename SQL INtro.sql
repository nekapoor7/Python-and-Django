SQL
1. Standard database laguage which is used to create, maintain and retrieve the relational database.

Relational Database
Data is stored as well as retrieved in the form of relations(table).
Attribute: properties that define a relation For example Roll_No, Name etc.
Tuple : Each row in a relation
Column: Set of values for a particular attributes
Cardinality: number of tuples in a relation. The Student relation defined above has cardinality 4.
Degree: number of attributes in a relation. The student relation defined as above is 4.

SQL DataTypes
1. Binary Datatypes -> binary, varbinary, varbinary(max),image
2. Numeric Datatypes -> int,bigint,smallint
3. Approximate Numeric Datatypes -> float,real
4. Character String Datatype -> char,varchar,varchar(max)
5. Unicode Character Datatype -> nchar,Nvchar
6. Data and Time Datatype -> datetime,date,time

SQL Commands 
1. DDL -> Data Definition Language- used to define the structure of the database 
example: CREATE,ALTER,DROP,RENAME,TRUNCATE,COMMENT.
2. DML -> Data Manipulation Language - used to manipulate data in the relations 
example: SELECT,INSERT,UPDATE,DELETE,MERGE.
3. TCL -> Transaction Control Language - used to manage transactions in the database. 
They are used to manage the changes made by DML statements. 
example: COMMIT,SAVEPOINT,ROLLBACK.
4. DCL -> Data Control Language - used to control access to data stored in the database(Authorization).
example: GRANT,REVOKE.

SQL Transactions
Transaction- group a set of tasks into a single execution unit. Each transactions begins with a 
specific task and ends when all the tasks in the group successfully complete.
A database transaction must be atomic,inconsistent,isolated and durable.(ACID)
1. SET TRANSACTION -> SET TRANSACTION [READ WRITE | READ ONLY];
2. COMMIT -> CHANGES ARE RECORDED TOGETHER IN A DATABASE. SAVED ALL THE TRANSACTIONS TO THE DATABASE.
3. ROLLBACK -> PROCESS OF REVERSING CHANGES. IT CAN ONLY UNDO TRANSACTIONS SINCE THE LAST COMMIT
 OR ROLLBACK.
4. SAVEPOINT -> POINT IN A TRANSACTION IN WHICH YOU CAN ROLL THE TRANSACTIONS BACK TO A CERTAIN 
POINT WITHOUT ROLLING BACK THE ENTIRE TRANSACTION.
5. RELEASE SAVEPOINT-> REMOVE SAVEPOINT THAT WE HAVE CREATED.

SQL Views
Views are kind of Virtual tables. A view has rows and columns as they are in a real table in the database.
A view can be created from a single and multiple tables.

CREATE VIEW
CREATE VIEW view_name as VIEW_TABLE Select NAME,ADDRESS FROM STUDENT WHERE ID < 5;

CREATE VIEW FROM MULTIPLE TABLES
CREATE VIEW MARKVIEW AS SELECT StudentDetails.Name,StudentDetails.Address,StudentMarks.Marks
from StudentDetails,StudentMarks
where StudentDetails.Name = Student.Marks.Name

SQL Contraints
Constraints are the rules that we can apply on the type of data in a table.
The constraints are:-
1. NOT NULL -> This constraint tells that we cannot store a null value in a column. 
2. UNIQUE -> This constraint specified with column, all the values in the column must be
unique.
3. PRIMARY KEY -> Field which can be uniquely identify each row in  table. 
4. FOREIGN KEY -> A foreign key is a field which can be uniquely identify each row in an 
another table.
5. CHECK -> Validate the values of a column to meet a particular condition.
6. DEFAULT -> Specifies a default value for the column when no value is specified by the user.

SQL Creating Roles
A role is created to ease setup and maintainence of the security model.
Some of the privileges are:
1. CONNECT -> Create table,view,session and sequence.
2. RESOURCE -> Create table,sequence,procedure.The primary usage of the resource role is to restrict
access to database objects.
3. DBA -> All system privileges.
First DBA must create the role. Then DBA can assign privileges to the role and users to the role.

CREATE ROLE manager;
Role Created

GRANT PRIVILEGES TO ROLE
Grant create table,create view
To Manager;
Grant Succeeded.

GRANT manager to SAM, STARK;
Grant Succeeded

REVOKE create table FROM manager;
DROP ROLE manager;

SQL INDEXES
1. An index is a schema object.
2. It is used by the server to speed up the retrieval of rows by using pointer.
3. An index helps to speed up select queries and where clauses but it slows down data input, with
the update and insert statements.

CREATE INDEX 
CREATE INDEX index ON TABLE column;
CREATE MULTIPLE COLUMNS
CREATE INDEX index ON TABLE(column1,column2....);
UNIQUE INDEXES
CREATE UNIQUE INDEX index ON TABLE column;

SQL SEQUENCES

1.A sequence is an user defined schema bound object that generates a sequence of numeric values.
2. Sequences are frequently used in many databases because many applications require each row in a table
to contain an unique value and sequences provides an easy way to generate them.

CREATE SEQUENCE sequence_name
START WITH initial_value
INCREMENT BY increment_value
MINVALUE minimum_value
MAXVALUE maximum_value
CYCLE | NOCYCLE;

CREATE SEQUECNE sequence_name1
START WITH 1
INCREMENT BY 1
MINVALUE 0
MAXVALUE 100
CYCLE;

SQL TRIGGER
A trigger is a stored procedure in database which automatically invoked whenever a special event in the 
database occurs.
For example, a trigger can be invoked when a row is inserted into a specified table.

create trigger [trigger_name]
[before | after]
{insert | update | delete }
on [table_name]
[for each row]
[trigger_body]

1. create trigger [trigger_name]: Creates re replaces an existing trigger with the trigger_name.
2. before|after: Specifies when trigger will be executed 
3. {insert | update | delete }: DML Operation
4. on [table_name]: specifies the name of the table associated with tigger
5. [for each row]: specifies a row level trigger,the trigger will be executed for each row
6. [trigger_body]: Operation to be performed as trigger is fixed.

TYPES OF TRIGGER