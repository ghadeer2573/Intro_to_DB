import mysql.connector

# Try to connect to the MySQL server
try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456'  # <-- Replace with your MySQL root password
    )

    # Check if the connection was successful
    if connection.is_connected():
        cursor = connection.cursor()
        # Create the database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

# Always close the cursor and connection
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed.")
