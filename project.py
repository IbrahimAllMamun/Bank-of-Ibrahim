import mysql.connector
from mysql.connector import Error
from datetime import date
import re
import sys
import random
import string



def main():
    while True:
        print(
            '''
    1. Sign In
    2. Sign Up
    3. Exit'''
        )
        while True:
            try:
                opt = int(input("Enter (1, 2 or 3): "))
                print()
                if opt not in [1, 2, 3]:
                    raise ValueError("Invalid Input. Try again.")
            except ValueError:
                print("Invalid Input. Try again.")
            else:
                break

        match opt:
            case 1:
                signedin()
                break
            case 2:
                signup()
            case 3:
                sys.exit("Thank you")


def signedin():
    id = signin()
    query = (f'SELECT pd.person_id, pd.full_name, pd.dob, pd.email, pd.phone_number, '
             f'acc.current_balance, acc.date_opened FROM personal_data pd '
             f'INNER JOIN account acc ON acc.person_id = pd.person_id '
             f'WHERE pd.person_id = {id}')

    account = [{
        'person_id': person_id,
        'full_name': full_name,
        'dob': dob,
        'email': email,
        'phone_number': phone_number,
        'balance': current_balance,
        'date_opened': date_opened
    } for (person_id, full_name, dob, email, phone_number, current_balance, date_opened)
        in query_manager(get_sql_connection(), query)][0]

    bank = Bank(**account)

    while True:
        print('''
    1. Check Balance
    2. Deposit 
    3. Withdraw
    4. View Transaction History
    5. Account Details
    6. Exit''')
        while True:
            try:
                opt = int(input("Enter (1, 2, 3, 4, 5 or 6): "))
                print()
                if opt not in [1, 2, 3, 4, 5, 6]:
                    raise ValueError("Invalid Input. Try again.")
            except ValueError:
                print("Invalid Input. Try again.")
            else:
                break

        match opt:
            case 1:
                print(f"Your balance is ${bank.balance:.2f}")
            case 2:
                while True:
                    try:
                        amount = int(input("How much you want to diposit? $"))
                        break
                    except ValueError:
                        print("Invalid amount")
                bank.diposit(amount=amount)
                make_transaction(
                    get_sql_connection(),
                    amount=amount,
                    trx_type=1,
                    person_id=bank._id
                )
            case 3:
                while True:
                    try:
                        amount = int(input("How much you want to withdraw? $"))
                        break
                    except ValueError:
                        print("Invalid amount")
                try:
                    bank.withdraw(amount=amount)
                    make_transaction(
                        get_sql_connection(),
                        amount=amount,
                        trx_type=2,
                        person_id=bank._id
                    )
                except Exception as e:
                    print(e)
            case 4:
                q = (f'SELECT transaction_id, amount, transaction_type.transaction_type, transaction_date FROM transactions '
                     f'INNER JOIN transaction_type ON transaction_type.transaction_type_id = transactions.transaction_type '
                     f'WHERE person_id={bank._id} ORDER BY transaction_date DESC')
                txns = [[transaction_id, amount, transaction_type, f'{transaction_date.day}-{transaction_date.month}-{transaction_date.year}']
                        for (transaction_id, amount, transaction_type, transaction_date) in query_manager(get_sql_connection(), q)]
                print("Transactions made by you.")
                print(f'{"TxnID":<10}{"Amount":>10}   {"Txn Type":<12}{"Txn Date":<12}')
                for txn in txns:
                    print(f'{txn[0]:<10}{txn[1]:>10.2f}   {txn[2]:<12}{txn[3]:<12}')

            case 5:
                print(bank)
            case 6:
                sys.exit("Thank you")



# Bank Class
class Bank:
    def __init__(self, person_id, full_name, dob, email, phone_number, balance, date_opened):
        self._id = person_id
        self._name = full_name
        self._dob = dob
        self._email = email
        self._phone = phone_number
        self._balance = balance
        self._date_opened = date_opened

    def __str__(self):
        return  (f'\nAccount Details '
                 f'\n{"Name":<14}: {self._name} '
                 f'\n{"Date of Birth":<14}: {self._dob} '
                 f'\n{"E-Mail":<14}: {self._email} '
                 f'\n{"Phone":<14}: {self._phone} '
                 f'\n{"Account Opened":<14}: {self._date_opened}')

    def diposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

        else:
            raise ValueError(f"Failed! Insufficient balance.")

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance
        try:
            update_balance(get_sql_connection(), self.balance, self._id)
        except Error as e:
            pass



# SQL Connection
__cnx = None
def get_sql_connection():
    global __cnx
    hostname = "fkw.h.filess.io"
    database = "atm_silvermany"
    port = "3307"
    username = "atm_silvermany"
    password = "582413bded5216fd78f78dc680a3052d458fa33c"
    if __cnx is None or not __cnx.is_connected():
        try:
            __cnx = mysql.connector.connect(
                host=hostname, 
                database=database, 
                user=username, 
                password=password, 
                port=port
                )
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            __cnx = None
    return __cnx




# Backend
def query_manager(cnx, query):
    cursor = cnx.cursor()
    cursor.execute(query)

    return cursor

def insert_new_user(cnx, user_detail):
    cursor = cnx.cursor()
    q1 = ("INSERT INTO personal_data"
          "(password, full_name, dob, email, phone_number, user_name)"
          "VALUES (%s, %s, %s, %s, %s, %s)")
    data = (
        user_detail['password'],
        user_detail['full_name'],
        user_detail['dob'],
        user_detail['email'],
        user_detail['phone_number'],
        user_detail['user_name']
    )
    cursor.execute(q1, data)
    cnx.commit()

    person_id = cursor.lastrowid
    cursor.close()

    cursor = cnx.cursor()
    q2 = ("INSERT INTO account"
            "(person_id,current_balance, date_opened)" 
            "VALUES (%s, %s, %s)")
    cursor.execute(q2, (person_id, 0, date.today()))
    cnx.commit()
    cursor.close()
    cnx.close()

def make_transaction(cnx, amount, trx_type, person_id):
    trxid = get_trxid()
    cursor = cnx.cursor()
    q = ("INSERT INTO transactions"
            "(transaction_id, transaction_type, amount, transaction_date, person_id)" 
            "VALUES (%s, %s, %s, %s, %s)")
    cursor.execute(q, (trxid, trx_type, amount, date.today(), person_id))
    cnx.commit()
    cursor.close()
    cnx.close()

def update_balance(cnx, balance, person_id):
    cursor = cnx.cursor()
    q = f'UPDATE account SET current_balance = {balance} WHERE (person_id = {person_id})'
    cursor.execute(q)
    cnx.commit()
    cursor.close()
    cnx.close()

def get_trxid():
    query = f"SELECT transaction_id FROM transactions"
    trxids = [a for (a, ) in query_manager(get_sql_connection(), query)]
    while True:
        letters = random.choice(list(string.ascii_uppercase)) + random.choice(list(string.ascii_uppercase))
        nums = random.randint(100000, 999999)
        trxid = f'{letters}{nums}'
        if trxid not in trxids:
            return trxid




# Authentiction
def signup():
    name = input("Enter your full name: ")
    while True:
        email = input("Enter your e-mail: ")
        if valid(email, "email"):
            break
        print("This e-mail is already been used.")
        print("Try a new one.")

    while True:
        phone = input("Enter your phone number: ")
        if len(phone) in [10, 11, 13, 14]:
            if re.match(r"^(\+8801)", phone) and len(phone)==14:
                pass
            elif re.match(r"^(8801)", phone) and len(phone)==13:
                phone = f"+{phone}"
            elif re.match(r"^(01)", phone) and len(phone)==11:
                phone = f"+88{phone}"
            elif re.match(r"^1", phone) and len(phone)==10:
                phone = f"+880{phone}"
            else:
                print("Enter a valid phone number.")
                continue
        else:
            print("Enter a valid phone number.")
            continue
        
        if valid(phone, "phone_number"):
            break
        else:
            print("This phone number is already been used.")
            print("Try a new one.")



    while True:
        dob = input("Enter your date of birth (DD-MM-YYYY): ")
        if matches:=re.match(r"(\d\d)-(\d\d)-(\d\d\d\d)", dob):
            day, month, year = matches.groups()
            if int(day)>31 or int(month)>12:
                pass
            else:
                dob = date.fromisoformat(f"{year}-{month}-{day}")
                break

    while True:
        user = input("Create username: ")
        if valid(user, "user_name"):
            break
        print("This username is taken.")
        print("Try something else.")

    print('''Your password must have at least 8 charecter, 
                        at least one uppercase letter, 
                        at least one number, 
                        at least one special charecter''')
    while True:
        password = input("Enter a password: ")
        if len(password)<8:
            print("Use at least 8 charecter.")

        elif not re.search(r"[A-Z]",password):
            print("Use at least one uppercase letter.")
            
        elif not re.search(r"[0-9]",password):
            print("Use at least one number.")
            
        elif not re.search(r"[\W]",password):
            print("Use at least one special charecter.")
            
        else:
            while True:
                con = input("Confirm password: ")
                if con == password:
                    break
                else:
                    print("Password didn't match.")
            break
    
    data = {
       'password' : password,
       'full_name' : name,
       'dob' : dob,
       'email' : email,
       'phone_number' : phone,
       'user_name' : user
    }

    insert_new_user(get_sql_connection(), data)


def signin():
    while True:
        token = input("Enter your e-mail or username: ")
        if not valid(token, "email"):
            break
        elif not valid(token, "user_name"):
            break
        else:
            print("You are not registered.")
            res = input("Sign Up(Yes/No): ")
            match res.lower():
                case "yes":
                    signup()
                case "no":
                    sys.exit("Thank you")
                case _:
                    sys.exit("Invalid Option")

    
    query = f'SELECT password, person_id FROM personal_data WHERE email="{token}" OR user_name="{token}"'
    person = [
        {"password":password, "person_id":person_id} 
        for (password, person_id) in query_manager(get_sql_connection(), query)][0]
    attempt = 3
    while attempt > 0:
        password = input("Enter your password: ")
        if password == person["password"]:
            print("Succesfully Signed In.")
            return person["person_id"]
        else:
            print("Invalid Password. Try again.")
            attempt -= 1
    sys.exit("You have entered your password incorrectly 3 times.")

def valid(value,type):
    columns = ["email", "phone_number", "user_name"]
    query = f"SELECT {type} FROM personal_data"
    types = [a for (a, ) in query_manager(get_sql_connection(), query)]
    if type not in columns:
        raise ValueError("Use defined data types: email, phone_number or user_name")
    if value in types:
        return False
    return True






if __name__ == "__main__":
    main()
