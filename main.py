import sqlite3
import re
import pandas as pd

def ask_password():
    password = input("Please, Enter your Password :")
    temp = ''

    file_con = pd.read_excel('chyper-code.xlsx')
    df = pd.DataFrame(file_con)
    data = df.values.tolist()
    for ch in password:
        value_change = 0
        for row in data:
            if row[0] == ch.upper():
                temp += (row[1])
                value_change = 1
        if value_change ==0:
            temp += ch

    return temp


wrong_ans = "false"
lst = []
connection = sqlite3.connect("USER.DB")
count=1
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

"""--------     For finding how many row entered in user-backup file  ---------------
   --------      if file not exist it will create new one         ----------------"""
try:
    file = open('user-backup.csv')
except FileNotFoundError:
    file = open('user-backup.csv', mode='w+')
for file_row in file:
    count= count+1

def type_mail():
    mail=input("Enter your mail ID : ")
    if(re.fullmatch(regex,mail)):
        return mail
    else:
        print("OPPS ! YOUR MAIL ID IS INVALID TRY AGAIN\n")
        return 0

while wrong_ans:
    options=[1,2,0]
    print("1) Create New Account \n2) LOG IN  \n0) Exit")
    try:
        choise = int(input("PLEASE CHOOSE OPTION:"))
        print()
        if choise not in options:
            print("!!! Opps, you select wrong option  !!! ")
            print("Please try again \n")
            continue
        elif choise == 0:
            print()            # in order to exit if loop

    except ValueError:
        print("!!!  Opps, You are not selected Correct number  !!!")
        print("Please, try again \n")
        continue
    else:
        wrong_ans = "true"

    if choise == 1:
        login = type_mail() # -------email check
        if login == 0:
            continue
        password = ask_password() # ---- password check

        cursor = connection.cursor()
        cursor.execute(f"SELECT LOGIN FROM TB_USER WHERE LOGIN='{login}';")
        if cursor.fetchone():
            print("Opps! THIS LOGIN ID IS ALREADY INSERT IN DATABSE PLEASE TRY TO LOGIN\n ")
        else:
            # -------------   INSERT  QUERY   --------------------

            try:
                # ------------       for SQLITE DATABSE file       ---------------
                cursor = connection.cursor()
                cursor.execute("INSERT INTO TB_USER (LOGIN,PASSWORD) values ('{}','{}');".format(login,password))
                cursor.execute("COMMIT;")
                cursor.close()

                # ------------       for user-backup file       ---------------
                file = open('user-backup.csv', mode='a')
                new_row = f'{count},{login},{password},0\n'
                file.write(new_row)
                file.close()  # as close file after writing is completed, there is no need to use flush
                count = count+1

            except (FileExistsError, AttributeError):
                print("Opps ! SOMTHING IS WRONG PLEASE TRY AFTER SOMETIME \n")

            else:
                print("WELCOME TO DATABASE\n")


    if choise == 2:
        login = input("Please, Enter Mail Id :") # -------email check
        password = ask_password() # ---- password check

        cursor = connection.cursor()
        cursor.execute(f"SELECT LOGIN FROM TB_USER WHERE LOGIN='{login}' AND PASSWORD = '{password}';")
        if not cursor.fetchone():
            print("Opps! LOGIN ID AND PASSWORD IS INCORRECT IF YOU HAVE NOT CREATED ACCOUNT, PLEASE CREATE FIRST TO ACCESS\n ")
        else:
            print("welcome")
            cursor.execute("UPDATE TB_USER SET ACCESS_COUNT = ACCESS_COUNT + 1 WHERE LOGIN='{}' AND PASSWORD = '{}';".format(login,password))
            cursor.execute("COMMIT;")
            print("YOU ACCESS THE ACCOUNT")

    if choise == 0:
        print("*****       Thank you for visit        *****")
        print("*****         Have a nice day!         *****")
        break
