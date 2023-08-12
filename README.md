# Bank Management System

The Bank Management System is a web application developed using Flask and MySQL that facilitates efficient management of banking operations. This repository contains the source code and resources required to run, customize, and deploy the system.

## Features

- **User-Friendly Interface:** The system offers an intuitive web-based interface for both customers and administrators to perform various banking tasks seamlessly.

- **Account Management:** Customers can make deposits, withdrawals, and transfer funds. Administrators can manage customer accounts, open accounts, and view transaction histories.


## Installation

To set up the Bank Management System, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/Ravisxcr/Bank-Management.git
   cd Bank-Management
   ```

2. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```


4. Create the necessary database tables by running the provided SQL script:

   ```bash
   mysql -u your_username -p < database_setup.sql
   ```

## Usage

1. Start the Flask development server:

   ```bash
   python main.py
   ```

   The application will be accessible at `http://localhost:5000`.

2. Customers can log in to their accounts, perform transactions, and view their balances.

3. Administrators can log in to manage customer accounts, view transaction logs, and perform administrative tasks.

## Customization

- To customize the application's appearance or behavior, refer to the templates in the `templates` directories.

- For database schema changes, update the SQL script and modify the corresponding models in the `database.py` file.


---

Simplify banking operations with the Bank Management System developed using Flask and MySQL. Whether you're managing customer accounts or overseeing transactions, this application provides a comprehensive solution for efficient banking management.

![Bank Management](images/bank_management.jpg)
