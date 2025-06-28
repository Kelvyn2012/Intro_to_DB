import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (not to a specific database yet)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Jenifer2012%"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Try to create the database
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as db_err:
                print(f"❌ Failed to create database: {db_err}")

    except Error as conn_err:
        print(f"❌ Error connecting to MySQL server: {conn_err}")

    finally:
        # Close the connection if it was opened
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("✅ MySQL connection closed.")

if __name__ == "__main__":
    create_database()
