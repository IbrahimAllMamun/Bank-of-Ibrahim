# Bank of Ibrahim
#### Video Demo:  [Watch the video](https://youtu.be/Kp7FpzJzVNM)
#### Description:
Bank of Ibrahim is a Python-based banking application that allows users to manage their accounts through a command-line interface. It provides functionalities for user authentication, banking operations, and transaction management using a MySQL database backend.

## Features

- **User Authentication**:

  - Sign Up: New users can register by providing their details including full name, email, phone number, date of birth, username, and password.
  - Sign In: Registered users can log in using their email or username along with their password.
- **Banking Operations**:

  - Check Balance: Users can view their current account balance.
  - Deposit: Users can deposit money into their account.
  - Withdraw: Users can withdraw money from their account, provided they have sufficient balance.
  - View Transaction History: Users can view their transaction history including details like transaction ID, amount, type, and date.
  - View Account Details: Users can view their personal account details including full name, date of birth, email, phone number, and account opening date.
- **Security**:

  - Password Requirements: Passwords must be at least 8 characters long and include at least one uppercase letter, one number, and one special character.
  - Data Validation: Validates user input for email, phone number, and username to ensure uniqueness and correct format.
- **Database Integration**:

  - Uses MySQL database (`atm`) to store user information, account details, and transaction records.
  - Tables include `personal_data` for user information, `account` for account balances and dates, `transactions` for transaction records, and `transaction_type` for transaction types.

## Requirements

- Python 3.x
- MySQL Server
- Python packages: `mysql-connector-python`

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd Bank-of-Ibrahim
   ```
2. Install dependencies:

   ```bash
   pip install mysql-connector-python
   ```
3. Set up the MySQL database:

   - Create a MySQL database named `atm`.
   - Run the SQL queries provided in `create_tables.sql` to create the necessary tables and insert sample data.
4. Update database connection details:

   - Modify the database connection parameters (`user`, `password`, `host`, `database`) in the `project.py` file to match your MySQL configuration.
5. Run the application:

   ```bash
   python project.py
   ```

## Usage

- Upon running `project.py`, you will be presented with options to Sign In, Sign Up, or Exit.
- Follow the prompts to perform banking operations once signed in.

## License

This project is licensed under the [MIT License](LICENSE).