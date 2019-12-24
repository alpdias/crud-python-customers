# -*- coding: utf-8 -*-
'''
Created in 12/2019
@Author: Paulo https://github.com/alpdias
'''

# imported libraries
import os
import pymysql
from time import sleep
from datetime import date 
import csv

# connection
try:
    connection = pymysql.connect(host = 'localhost', database = 'people', user = 'root', passwd = '')
    cursor = connection.cursor()
    print(' ')
    print('\033[0;32mCONNECTION ESTABLISHED\033[m')
    established = 1
    sleep(2)
    os.system('cls')
except:
    print(' ')
    print('\033[0;31mERROR CONNECTING DATABASE...\033[m')
    sleep(1)
    established = 0


# if connection is established
if established == 1:
    
    # main program
    while True:
        os.system('cls')
        print(' ')
        print('CRUD - RECORDS LIST')
        print(' ')
        menu = ['VIEW RECORDS LIST', 'RECORDS SEARCH', 'ADD NEW RECORD', 'CHANGE RECORD', 'DELETE RECORD', 'EXPORT TABLE', 'IMPORT TABLE']
        for index, listItems in enumerate(menu):
            print(f'\033[0;36m[{index + 1}]\033[m {listItems}')
        print('\033[0;31m[0]\033[m EXIT PROGRAM')
        print(' ')
        selectOption = int(input('SELECT AN OPTION TO PERFORM: '))

        # Options
        if selectOption in [0, 1, 2, 3, 4, 5, 6, 7]:

            # records list
            if selectOption == 1:
                os.system('cls')
                print(' ')
                try:
                    result = cursor.execute('SELECT * FROM people')
                    for result in cursor:
                        print(result)
                except:
                    print('\033[0;31mTABLE NOT FOUND CHECK CONNECTION\033[m')
                print(' ')
                listBreak = str(input('TO EXIT PRESS [e]: '))
                if listBreak == 'E':
                    break

            # records search
            if selectOption == 2:
                os.system('cls')
                print(' ')
                searchRecord = int(input('SELECT ID TO SEARCH: '))
                print(' ')
                try:
                    searchID = cursor.execute(f'SELECT * FROM people WHERE id = {searchRecord}')
                    connection.commit()
                    resultSearch = cursor.fetchone()
                    if resultSearch == None:
                        print('\033[0;31mRECORD NOT FOUND SEE RECORD LIST\033[m')      
                    else:
                        print(resultSearch)
                except:
                    print('\033[0;31mRECORD NOT FOUND, CHECK YOUR INPUT OR CONNECTION\033[m')
                print(' ')
                searchBreak = str(input('TO EXIT PRESS [e]: '))
                if searchBreak == 'E':
                    break

            # add new record
            if selectOption == 3:
                os.system('cls')
                print(' ')
                print('FILL IN TO ADD A NEW RECORD...')
                print(' ')
                numberID = str(input('ID (empty to self fill):  '))
                fullName = str(input('FULL NAME: '))
                profession = str(input('PROFESSION: '))
                birth = str(input('BIRTH [yyyy-mm-dd]: '))
                genre = str(input('GENRE [M/F]: '))
                bodyweight = str(input('BODY WEIGHT: '))
                height = str(input('HEIGHT: '))
                nationality = str(input('NATIONALITY: '))
                print(' ')
                confirmInclusion = str(input('CONFIRM INCLUSION OF RECORDS \033[0;31m[Y/N]\033[m? ')).strip().upper()
                if confirmInclusion == 'Y':
                    try:
                        cursor.execute("INSERT INTO people (id, fullname, profession, birth, genre, bodyweight, height, nationality)   \
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (numberID, fullName, profession, birth, genre, bodyweight, height, nationality))
                        connection.commit()
                        print(' ')
                        print('\033[0;32mSUCCESSFUL INCLUSION\033[m')
                    except:
                        print(' ')
                        print('\033[0;31mNOT DONE INCLUSION, CHECK YOUR INPUT OR CONNECTION\033[m')
                else:
                    print(' ')
                    print('\033[0;31mUNREALIZED INCLUSION\033[m')
                print(' ')
                sleep(2)

            # change record
            if selectOption == 4:
                os.system('cls')
                print(' ')
                changeID = int(input('REGISTRATION ID FOR CHANGE: ')) 
                print(' ')
                print('LOOKING FOR RECORD...') 
                print(' ')
                sleep(2)
                try:
                    searchChangeID = cursor.execute(f'SELECT * FROM people WHERE id = {changeID}')
                    connection.commit()
                    resultChangeSearch = cursor.fetchone()
                    if resultChangeSearch == None:
                        print('\033[0;31mRECORD NOT FOUND SEE RECORD LIST\033[m')
                        changeIDConnection = 0      
                    else:
                        print(resultChangeSearch)
                        changeIDConnection = 1
                except:
                    print('\033[0;31mRECORD NOT FOUND, CHECK YOUR INPUT OR CONNECTION\033[m')
                    changeIDConnection = 0
                if changeIDConnection == 1:
                    print(' ')
                    listOptions = ['ID', 'FULL NAME', 'PROFESSION', 'BIRTH', 'GENRE', 'BODY WEIGHT', 'HEIGHT', 'NATIONALITY']
                    for index, listItems in enumerate(listOptions):
                        print(f'[{index + 1}] {listItems}')
                    print(' ')
                    changeColumn = int(input('SELECT THE COLUMN NUMBER YOU WISH TO MODIFY: '))
                    if changeColumn == 1:
                        changeColumn = 'id'
                    elif changeColumn == 2:
                        changeColumn = 'fullname'
                    elif changeColumn == 3:
                        changeColumn = 'profession'
                    elif changeColumn == 4:
                        changeColumn = 'birth'
                    elif changeColumn == 5:
                        changeColumn = 'genre'
                    elif changeColumn == 6:
                        changeColumn = 'bodyweight'
                    elif changeColumn == 7:
                        changeColumn = 'height'
                    elif changeColumn == 8:
                        changeColumn = 'nationality'
                    print(' ')
                    newChange = str(input('NEW INPUT: '))
                    try:
                        changeModify = cursor.execute(f"UPDATE people SET {changeColumn} = '{newChange}' WHERE id = {changeID}")
                        connection.commit()
                        print(' ')
                        print('\033[0;32mSUCCESSFUL MODIFICATION\033[m')
                    except:
                        print(' ')
                        print('\033[0;31mERROR TRYING TO MODIFY, CHECK TABLE OR CONNECTION\033[m')
                print(' ')
                sleep(2)

            # delete record
            if selectOption == 5:
                os.system('cls')
                print(' ')
                deleteID = int(input('ID TO DELETE: '))
                print(' ')
                try:
                    deletedID = cursor.execute(f'SELECT * FROM people WHERE id = {deleteID}')
                    connection.commit()
                    resultDeleteSearch = cursor.fetchone()
                    deleteRecordConnection = 1
                    if resultDeleteSearch == None:
                        deleteRecordConnection = 0
                        print('\033[0;31mRECORD NOT FOUND SEE RECORD LIST\033[m')     
                    else:
                        print(resultDeleteSearch)
                        print(' ')
                except:
                    deleteRecordConnection = 0
                    print('\033[0;31mRECORD NOT FOUND, CHECK YOUR INPUT OR CONNECTION\033[m')
                if deleteRecordConnection == 1:
                    confirmDelete = str(input('DO YOU REALLY WANT TO DELETE THIS RECORD? \033[0;31m[Y/N]\033[m ')).strip().upper()
                    if confirmDelete == 'Y':
                        try:
                            deletedID = cursor.execute(f'DELETE FROM people WHERE id = {deleteID}')
                            connection.commit()
                            print('')
                            print('\033[0;32mSUCCESSFULLY DELETE RECORD, SEE LIST OF RECORDS TO VIEW\033[m')
                        except:
                            print('')
                            print('\033[0;31mERROR DELETING RECORD, CHECK INPUT OR CONNECTION\033[m')
                    else:
                        print('')
                        print('\033[0;31mREGISTRATION NOT DELETED\033[m')
                print(' ')
                sleep(2)
            
            # export table
            if selectOption == 6:
                os.system('cls')
                print('')
                nameExport = str(input('EXPORT FILE NAME: '))
                try:
                    result = cursor.execute('SELECT * FROM people')
                    wayExport = ('C:' + os.sep + 'Users' + os.sep + os.getlogin() + os.sep + 'Desktop' + os.sep)
                    newFile = wayExport + f'{nameExport}.txt'
                    with open(newFile, 'w', newline='') as lines:
                        writerFile = csv.writer(lines)
                        for row in cursor:
                            writerFile.writerow(row)
                    print('')
                    print('\033[0;32mFILE SUCCESSFULLY EXPORTED\033[m')
                    sleep(2)
                except:
                    print('')
                    print('\033[0;31mUNEXPECTED ERROR, FILE NOT EXPORTED\033[m')
                    sleep(2)
                print(' ')
                
            # import table
            if selectOption == 7:
                pass

            # exit program
            if selectOption == 0:
                print(' ')
                print('\033[0;31mPROGRAM FINISHED\033[m')
                print(' ')
                sleep(1)
                break
            
        # invalid option
        else:
            print(' ')
            print('\033[0;31mINVALID OPTION TRY AGAIN\033[m')
            sleep(1)

# if connection is not established
elif established == 0:
        print('\033[0;31mCHECK DATABASE CONNECTION AND TRY AGAIN\033[m')
        print(' ')
