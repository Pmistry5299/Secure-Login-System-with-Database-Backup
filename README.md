# Secure-Login-System-with-Database-Backup
The "Secure Login System with Database Backup" is a Python project that aims to provide a secure login system using a combination of email-based authentication and a password encrypted with a specific cipher. The project also incorporates a mechanism to back up user account data into a CSV file for data redundancy and recovery purposes.

## Project Overview:
The project consists of three main files:

**Main Python Script (secure_login_system.py):**
This file contains the main logic for creating a new account, logging in, and managing user access. The script interacts with the user to input their email and password, encrypts the password using a cipher, and handles authentication and database operations.

**Cipher Code File (chyper-code.xlsx):**
This file is used to store the cipher code that encrypts the password. The cipher is employed to enhance the security of user passwords during the authentication process.

**Database File (USER.DB):**
An SQLite database file is utilized to store user account information securely. It contains tables to store login information and track user access counts.

## Features and Functionality:

**User Account Creation:**
Users can create a new account by providing their email address. The system validates the email format and prompts the user to create a password. The password is then encrypted using a cipher, enhancing security.

**Login and Access:**
Registered users can log in by providing their email and password. The system decrypts the password using the cipher and verifies the login credentials. Successful login results in an increment of the user's access count in the database.

**Database Backup:**
The system maintains a backup of user account data in a CSV file (user-backup.csv). This backup mechanism ensures that user account information is preserved even if there are issues with the main database. The CSV file contains user account details, including login credentials and access counts.

**Why CSV Backup:**
A CSV (Comma-Separated Values) file is chosen for backup due to its simplicity and ease of use. It provides a structured format to store data and can be easily read, written, and accessed using various programming languages and tools. Additionally, CSV files are human-readable, making it convenient for manual inspection and data recovery in case of database issues.

This project focuses on providing a secure and user-friendly login system while ensuring data integrity through a backup mechanism, making it a valuable tool for managing user authentication securely.
