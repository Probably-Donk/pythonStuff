import csv

def read_credentials_from_csv(file_path):
    credentials = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            credentials.append((row[0], row[1]))  # Assuming username is in column 0 and password in column 1
    return credentials

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

# Test the login function
login()
