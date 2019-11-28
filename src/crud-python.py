# imported libraries
import os
import pymysql
from time import sleep
from datetime import date

# functions
connection = pymysql.connect(host = 'localhost', database = 'people', user = 'root', passwd = '')
cursor = connection.cursor()

# main program
print('')
print('CRUD - Records List')
print('')
menu = ['records list', 'records search', 'add new record', 'change record', 'export table', 'import table']
for index, listItems in enumerate(menu):
    print(f'[{index + 1}] {listItems}')
print('[0] exit the program')
print('')
selectOption = int(input('select an option to perform: '))

# records list
if selectOption == 1:
    print('')
    print('records list')
    print('')
    nameTable = str(input('select table to view: '))
    print('')
    result = cursor.execute(f'SELECT * FROM {nameTable}')
    for result in cursor:
        print(result)

# records search

# add new record
if selectOption == 3:
    print('')
    print('fill in to add a new record')
    print('')
    numberID = str(input('ID (empty to self fill):  '))
    fullName = str(input('Full Name: '))
    profession = str(input('Profession: '))
    birth = str(input('Birth [yyyy/mm/dd]: '))
    genre = str(input('Genre [M/F]: '))
    bodyweight = str(input('Body Weight: '))
    height = str(input('Height: '))
    nationality = str(input('Nationality: '))
    cursor.execute("INSERT INTO people (id, fullname, profession, birth, genre, bodyweight, height, nationality)   \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (numberID, fullName, profession, birth, genre, bodyweight, height, nationality))
    connection.commit()

# change record

# export table

# import table

print('')