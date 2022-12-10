# Import necessary packages
import requests
import mysql.connector
from getpass import getpass

# Define the main function
def main():
    while True:
        # Print the menu
        print("HELP\n\nversion - Shows you the current version\nstatuscode - Get the current status code of a website\nconnectdb - Connect to a MySQL database")

        # Ask the user for a command
        command = input("Enter a command: ")

        # Execute the command
        if command == "help":
            print("HELP\n\nversion - Shows you the current version\nstatuscode - Get the current status code of a website\n")
        elif command == "version":
            print("Current version is 1.0 ALPHA. This tool is still in development")
        elif command == "statuscode":
            # Ask the user for a URL
            url = input("Enter a URL: ")

            # Try to get the status code of the website
            try:
                status_code = requests.get(url).status_code
                print("The status code of the website is:", status_code)
            except:
                print("The website could not be reached. Please try again.")
        elif command == "connectdb":
            # Ask the user for the database URL and credentials
            url = input("Enter the database URL: ")
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")

            # Try to connect to the MySQL database
            try:
                conn = mysql.connector.connect(user=username, password=password, host=url)
                print("Successfully connected to the MySQL database.")
            except:
                print("Could not connect to the MySQL database. Please try again.")

# Call the main function
if __name__ == "__main__":
    main()
