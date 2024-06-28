-- Table: account
CREATE TABLE account (
    person_id INT PRIMARY KEY,
    current_balance DOUBLE NOT NULL,
    date_opened DATE NOT NULL,
    FOREIGN KEY (person_id) REFERENCES personal_data(person_id)
);

-- Table: personal_data
CREATE TABLE personal_data (
    person_id INT AUTO_INCREMENT PRIMARY KEY,
    password VARCHAR(100) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    dob DATE NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone_number VARCHAR(14) NOT NULL,
    user_name VARCHAR(45) NOT NULL,
    UNIQUE INDEX (user_name),
    UNIQUE INDEX (email)
);

-- Table: transactions
CREATE TABLE transactions (
    transaction_id VARCHAR(8) PRIMARY KEY,
    transaction_type INT NOT NULL,
    amount DOUBLE NOT NULL,
    transaction_date DATE NOT NULL,
    person_id INT NOT NULL,
    FOREIGN KEY (person_id) REFERENCES personal_data(person_id),
    FOREIGN KEY (transaction_type) REFERENCES transaction_type(transaction_type_id)
);

-- Table: transaction_type
CREATE TABLE transaction_type (
    transaction_type_id INT PRIMARY KEY,
    transaction_type VARCHAR(10) NOT NULL
);
