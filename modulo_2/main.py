from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

load_dotenv()


import psycopg2

def conn_db_postgresql():
    conn = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        database=os.getenv('POSTGRES_DB'),
        port=os.getenv('POSTGRES_PORT')
        )
    return conn


def user_exists(func):
    def wrapper(connect, cursor):
        mail = input("Enter the email of the user you want to update: ")
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (mail,))
        user = cursor.fetchone()
        if user:
            func(connect, cursor, mail)
        else:
            logging.info(">>> No users found")
    
    wrapper.__doc__ = func.__doc__
    return wrapper


def system_clear(func):
    def wrapper(*args):
        os.system("cls")
        func(*args)
        input("Press Enter to continue...")
        os.system("cls")
    
    wrapper.__doc__ = func.__doc__
    return wrapper

@system_clear
def create_user(connection, cursor):
    """A) Create a user in the database"""

    username = input("Enter the username: ")
    email = input("Enter the email: ")
    password = input("Enter the password: ")
    query = f"INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    values = (username, email, password)
    cursor.execute(query, values)
    connection.commit()
    logging.info(">>> User created successfully")

@system_clear
def list_users(connection, cursor):
    """B) List all users in the database"""
    cursor.execute("SELECT username, email FROM users")
    users = cursor.fetchall()
    for user in users:
        logging.info(f"Username: {user[0]} - Email: {user[1]}")

@system_clear
@user_exists
def update_user(connection, cursor, mail):
    """C) Update a user in the database"""
    

    username = input("Enter the new username: ")
    password = input("Enter the new password: ")
    query = "UPDATE users SET username = %s, password = %s WHERE email = %s"
    values = (username, password, mail)
    cursor.execute(query, values)
    connection.commit()
    logging.info(">>> User updated successfully")


@system_clear
@user_exists
def delete_user(connection, cursor, mail):
    """D) Delete a user in the database"""
    query = "DELETE FROM users WHERE email = %s"
    cursor.execute(query, (mail,))
    connection.commit()
    logging.info(">>> User deleted successfully")

@system_clear
def exit_program(*args):
    """E) Exit the program"""
    logging.info(">>> Exiting the program")
    exit()

@system_clear
def default(*args):
    logging.info(">>> Invalid option")

def main():
    try:

        logging.info("Starting the program")
        with conn_db_postgresql() as conn:
            cursor = conn.cursor()
            options = {
                    "A": create_user,
                    "B": list_users,
                    "C": update_user,
                    "D": delete_user,
                    "E": exit_program
                }

            while True:

                for func in options.values():
                    logging.info(func.__doc__)

                option = input("Choose an option: ").upper()


                function = options.get(option, default)
                function(conn, cursor)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()