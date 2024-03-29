import csv
import basic
from cryptography import *

key = basic.load_key()

def read_credentials_from_csv(file_path):
    credentials = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            credentials.append((row[0], basic.decrypt_message(row[1], key)))
    return credentials

def write_credentials_to_csv(file_path, username, password):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, basic.encrypt_message(password, key)])

def login():
    max_attempts = 3
    attempts = 0
    correct_credentials = read_credentials_from_csv('credentials.csv')

    while attempts < max_attempts - 1:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if (username, password) in correct_credentials:
            print("Login successful!")
            return  # Exit the function if login is successful
        else:
            print("Incorrect username or password. Please try again.")
            attempts += 1

    if attempts == max_attempts - 1:
        print("Warning: This is your final attempt. Please ensure your credentials are correct.")
        username = input("Enter username: ")
        password = input("Enter password: ")

        if (username, password) in correct_credentials:
            print("Login successful!")
        else:
            print("Max attempts reached. Exiting program.")

def create_new_credentials():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    # Write the new credentials to the CSV file
    write_credentials_to_csv('credentials.csv', username, password)
    print("New credentials saved successfully.")
