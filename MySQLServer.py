import mysql.connector

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Jenifer2012%"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except mysql.connector.Error as db_err:
                print(f"❌ Failed to create database: {db_err}")

    except mysql.connector.Error as conn_err:
        print(f"❌ Error connecting to MySQL server: {conn_err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("✅ MySQL connection closed.")

if __name__ == "__main__":
    create_database()
