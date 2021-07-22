#import sqlite 3 and establish a connection
import sqlite3

conn = sqlite3.connect("bank.db") #error 3
c = conn.cursor()
print("Connection Established")

# create a table user
c.execute(''' CREATE TABLE IF NOT EXISTS user (
            id integer primary key,
            name text,
            age integer,
            gender text,
            city text
)
''');

#c.execute(f"DROP TABLE account")

# create account table
c.execute("""CREATE TABLE IF NOT EXISTS account
(
    id integer,
    balance integer default 1500 ,
    amount_withdrawn integer default 0,
    amount_deposited integer default 0,
    FOREIGN KEY(id)
    REFERENCES user(id)
)
 """);

# c.execute(f"DELETE FROM account")
conn.commit()
# PRAGMA foreign_keys=on;

#make user class
class user:
    
    def __init__(self,id,name,age,gender,city):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.city = city
        # self.store()

    def signup(self):
        global c
        c.execute(f"SELECT * FROM user WHERE id={self.id}") #error 1. plz refer the last pages of my coding diary to know abt the blunder i was commiting
        if c.fetchall():
            print("id already exists,  kindly login to continue")
        else:
            c.execute(f'INSERT INTO user VALUES ({self.id},"{self.name}",{self.age},"{self.gender}","{self.city}")') #error 2
            conn.commit()
    # def deleteacc(self,id):
    #     del = self.admin()
    #     del.delete(id)

class admin:
    global c
    def delete(self,id):
        c.execute(f"DELETE FROM user WHERE id={id}")
        conn.commit()


class Account():
    def __init__(self,id):
        self.id=id
        c.execute(f"SELECT * FROM account WHERE id={self.id}") #error 1. plz refer the last pages of my coding diary to know abt the blunder i was commiting
        if not c.fetchall():
            c.execute(f'INSERT INTO account VALUES ({self.id},1500,0,0)')
            conn.commit()
    def deposit(self,amount):
        c.execute(f"UPDATE account SET balance=balance+{amount},amount_deposited={amount} where id={self.id} ")
        conn.commit()
        c.execute(f"SELECT balance from account where id={self.id}")
        balance_updated = c.fetchone()[0]
        print(f"updated balance after depositing rs {amount} is {balance_updated}")
    
    def withdraw(self,amount):
        c.execute(f"UPDATE account SET balance=balance-{amount},amount_withdrawn={amount} where id={self.id} ")
        conn.commit()
        c.execute(f"SELECT balance from account where id={self.id}")
        balance_updated = c.fetchone()[0][0]
        print(f"updated balance after withdrawing rs {amount} is {balance_updated}")



print("1. Signup")
print("2. Show Details of any user")
print("3. Deposit in Bank")
print("4. Withdraw from bank")
print("5. Delete account")
choice=int(input("Select any option"))
if choice==2:
    id2=int(input("Enter id of the person"))
    c.execute(f"SELECT * FROM user WHERE id={id2}")
    print(c.fetchall())
elif choice==1:
    id=int(input("Enter id"))
    name=input("Enter name")
    age=int(input("Enter age"))
    gender=input("Enter gender")
    city=input("enter city")
    b=user(id,name,age,gender,city)
    b.signup()
elif choice==3:
    id=int(input("Enter ID"))
    amt=int(input("Enter Amount"))
    a=Account(id)
    a.deposit(amt)
elif choice==4:
    id=int(input("Enter ID"))
    amt=int(input("Enter Amount"))
    a=Account(id)
    a.withdraw(amt)
elif choice==5:
    id=int(input("Enter ID of the person you want to remove"))
    x=admin()
    x.delete(id)
    


# a = user(1,"swati", 20,"f","mumbai")
c.execute("SELECT * FROM user")
print(c.fetchall())
c.execute("SELECT * FROM account")
print(c.fetchall())
