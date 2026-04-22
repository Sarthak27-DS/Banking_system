from db import connect_db

class BankSystem:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor()
        self.current_user = None



    def register(self,name,pin):
        query = "INSERT INTO users(name,pin) VALUES (%s,%s)"
        self.cursor.execute(query,(name,pin))
        self.conn.commit()

        user_id = self.cursor.lastrowid

        # Creating account-->

        self.cursor.execute("INSERT INTO accounts (user_id,balance) VALUES (%s,%s)", (user_id,0))
        self.conn.commit()

        print("✅ Registration was successful!")
        print(f"👉 Your User ID is: {user_id}")



    def login(self,user_id,pin):
        query = "SELECT * FROM users WHERE id=%s AND pin=%s"
        self.cursor.execute(query,(user_id,pin))
        user = self.cursor.fetchone()

        if user:
            self.current_user = user_id
            print("✅ Login Successful!")
        else:
            print("❌Invalid Credentials")

    def deposit(self,amount):
        query = "UPDATE accounts SET balance = balance + %s WHERE user_id = %s"
        self.cursor.execute(query,(amount,self.current_user))

        self.cursor.execute(
            "INSERT INTO transactions (user_id,type,amount) VALUES (%s,%s,%s)",(self.current_user,"deposit",amount)
            )

        self.conn.commit()
        print("✅ Deposit successful!")
    
    def withdraw(self,amount):
        self.cursor.execute("SELECT balance FROM accounts WHERE user_id=%s", (self.current_user,))
        balance = self.cursor.fetchone()[0]

        if amount > balance:
            print("❌ Insufficient balance!")
            return
        
        self.cursor.execute("UPDATE accounts SET balance = balance - %s WHERE user_id=%s", (amount,self.current_user,))

        self.cursor.execute(
            "INSERT INTO transactions (user_id,type,amount) VALUES (%s,%s,%s)", (self.current_user,"withdraw",amount)
        )

        self.conn.commit()
        print("Withdrawal successful!")

    def check_balance(self):
        self.cursor.execute("SELECT balance FROM accounts WHERE user_id=%s", (self.current_user,))
        balance = self.cursor.fetchone()[0]
        print(f"Current balance: {balance}")

    def transaction_history(self):
        self.cursor.execute("SELECT type,amount,date FROM transactions WHERE user_id=%s", (self.current_user,))
        data = self.cursor.fetchall()

        for t in data:
            print(t)

    def delete_all_data(self):
        confirm = input("⚠️ Are you sure you want to delete ALL data? (yes/no): ")


        if confirm.lower() != "yes":
            print("❌ Operation cancelled.")
            return

        try:
         # delete in correct order
            self.cursor.execute("DELETE FROM transactions")
            self.cursor.execute("DELETE FROM accounts")
            self.cursor.execute("DELETE FROM users")

            self.conn.commit()
            print("🧹 All data deleted successfully!")

        except Exception as e:
         print("❌ Error:", e)



        