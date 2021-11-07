import mysql.connector
import time
import getpass

class mydatabase:
    mydb = mysql.connector.connect(host='localhost', user='root', password='')  # enables mysql connection
    mycursor = mydb.cursor()
    Tables = {}          # using dictionary to add all new tables and executing
    username=''         # using the username to access the respective table
    password=''

    def creating_database(self):        # a function to create a new table for a new user
        self.mycursor.execute('CREATE DATABASE passwordmanager')
        self.mycursor.execute('USE passwordmanager')

        self.Tables['master'] = (           # creating a master table to store master username & passwords
         '''CREATE TABLE `mastertable` (
            user_id varchar(20) PRIMARY KEY ,
            password varchar(30)
            );'''
            )

        table_desc = self.Tables['master']
        self.mycursor.execute(table_desc)

        self.mycursor.execute("select user_id from mastertable")
        result = self.mycursor.fetchall()
            
        while(True):                # finding whether given username already exists or not
            self.username = input('Enter a unique user_id:  ')
            self.password = input('Enter a password:  ')      
                
            try :
                insert_statement = 'INSERT INTO mastertable VALUES(%s,%s);'
                insert_values = (self.username,self.password)

                self.mycursor.execute(insert_statement, insert_values)
                    
                self.mydb.commit()
                break
                    
            except:
                print("username already exists")

            
        self.Tables[self.username] = (          # creating a new table for a new user
         '''CREATE TABLE `{}` (
            website_name varchar(20) NOT NULL ,
            url varchar(500) NOT NULL,
            email_id varchar(254) NOT NULL,
            password varchar(100) NOT NULL,
            PRIMARY KEY (email_id,url)
            );'''.format(self.username)
        )

        table_desc = self.Tables[self.username]
        self.mycursor.execute(table_desc)

    def existing_database(self) :           # fucntion defined to use the table of the existing user
        self.mycursor.execute('use passwordmanager')
        while True:
            username_entered = input('Enter your user_id:  ')
            password_entered = getpass.getpass(                 # helps to make password invisible 
                                prompt='Enter your password: ') # but it is actually being printed on console
                
            selectquery = 'SELECT * FROM mastertable'
            self.mycursor.execute(selectquery)
            record = self.mycursor.fetchall()

            correct_username = ''
            correct_password = ''

            for row in record:
                correct_username = row[0]
                correct_password = row[1]
                
            if username_entered == correct_username and password_entered == correct_password:
                self.username = username_entered            # checking whether the entered username and
                break                                       # password match with those present in master table
                
            elif username_entered != correct_username:
                print('Incorrect username')
                
            elif password_entered != correct_password:
                print('Incorrect password')

    def __init__(self):

        print('Welcome to password manager application')
        ans = input('Are you an exsiting user?(Yes/No)  ')
        
        if(ans == 'no' or ans == 'NO' or ans=='No'):
            self.creating_database()

        else :
            self.existing_database()
            
        
        text_message = ['C', 'o', 'n', 'n', 'e', 'c', 't', 'i', 'n', 'g', ' ', 't', 'o',
                         ' ', 'y', 'o', 'u', 'r', ' ', 'd', 'a', 't', 'a', 'b', 'a', 's', 'e',
                          ' ', '.', '.', '.']
        
        for i in text_message:
            if i == '.':
                print(i, end=' ', flush=True)
                time.sleep(0.5)
            else:
                print(i, end='', flush=True)
                time.sleep(0.1)
                    

        
dbobj = mydatabase()


