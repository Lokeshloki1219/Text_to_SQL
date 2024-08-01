import sqlite3


#connect to sql
connection=sqlite3.connect('student.db')

#Create Cursor
cursor=connection.cursor()


## Create the Table
table_info='''
CREATE TABLE Student(Name VARCHAR(25), Class VARCHAR(25),
Section VARCHAR(25), Marks INT);
'''
cursor.execute(table_info)

## Insert some more records
cursor.execute('''INSERT INFO STUDENT VALUES ('Lokeshwar','Data Science','A',90)''')
cursor.execute('''INSERT INFO STUDENT VALUES ('Priyanka','Machine Learning','B',100)''')
cursor.execute('''INSERT INFO STUDENT VALUES ('Sravani','DEVOPS','A',85)''')
cursor.execute('''INSERT INFO STUDENT VALUES ('Sandhya','DEVOPS','A',50)''')
cursor.execute('''INSERT INFO STUDENT VALUES ('Sowmya','Data Science','A',35)''')

## Display all the records
print('The inserted records are')

data=cursor.execute('''Select * From Student''')

for row in data:
    print(row)

## Close the connection
connection.commit()
connection.close()