# 💳 Smart Banking System (CLI)

A command-line based banking system built using **Python, MySQL, and OOP concepts**.
This project simulates real-world banking operations like user authentication, transactions, and account management.

---

## 🚀 Features

* 🔐 User Registration & Login (PIN-based authentication)
* 💰 Deposit Money
* 💸 Withdraw Money (with balance validation)
* 📊 Check Account Balance
* 📜 Transaction History
* 🧹 Delete All Records (Admin utility)

---

## 🧠 Concepts Used

* Object-Oriented Programming (OOP)
* MySQL Database Integration
* Exception Handling
* Modular Code Structure
* CLI-based User Interaction

---

## 🏗️ Project Structure

```bash
bank-system/
│
├── main.py          # CLI interface
├── bank.py          # Core banking logic
├── db.py            # Database connection
├── README.md
```

---

## 🗄️ Database Schema

### Users Table

* id (Primary Key)
* name
* pin

### Accounts Table

* id
* user_id (Foreign Key)
* balance

### Transactions Table

* id
* user_id
* type (deposit/withdraw)
* amount
* date

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/bank-system.git
cd bank-system
```

---

### 2. Install Dependencies

```bash
pip install mysql-connector-python
```

---

### 3. Setup MySQL Database

Run the following SQL:

```sql
CREATE DATABASE bank_system;

USE bank_system;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    pin VARCHAR(10)
);

CREATE TABLE accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    balance FLOAT DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    type VARCHAR(20),
    amount FLOAT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

---

### 4. Configure Database

Update `db.py` with your MySQL credentials:

```python
host="localhost"
user="root"
password="your_password"
database="bank_system"
```

---

### 5. Run the Application

```bash
python main.py
```

---

## 📌 Future Improvements

* 🌐 Web Interface using Flask
* 🖥️ GUI using Tkinter
* 🔒 Password Hashing (Security Enhancement)
* 💳 Money Transfer Between Users
* 📈 Analytics Dashboard

---

## 📸 Demo

CLI-based interaction showing banking operations.

---

## 🧑‍💻 Author

**Guddu**
Aspiring Software Engineer | Python Developer

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
