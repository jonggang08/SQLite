import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

#create a table
#c.execute('''CREATE TABLE meals(sandwich TEXT, fruit TEXT, tablenumber INT)''')

#data to insert
sandwich = 'egg'
fruit = 'apple'
tablenum = 21

#insert and commit to database
c.execute('''INSERT INTO meals VALUES(?,?,?)''', (sandwich, fruit, tablenum))
conn.commit()

#select all data from table and print
c.execute('''SELECT sandwich FROM meals''')
results = c.fetchall()
print(results)