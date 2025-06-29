import mysql.connector

def create_database():
    try:
        
        connection = mysql.connector.connect(
            host="localhost",
            user="root",          
            password="Jenifer2012%"
        )

        if connection.is_connected():
            print("✅ Connected to MySQL!")
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("🎉 Database 'alx_book_store' created!")

    except mysql.connector.Error as error:
        print("❌ Error:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 MySQL connection closed.")

if __name__ == "__main__":
    create_database()
