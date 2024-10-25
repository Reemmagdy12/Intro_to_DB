import mysql.connector 
def main():
 try:
        # Connect to MySQL server
        my_db = mysql.connector.connect(
            host='Popoi',
            user='root',  # replace with your MySQL username
            password='Entpteez@12'  # replace with your MySQL password
        )
        my_cursor = my_db.cursor()
        my_cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
        my_cursor.close()
        my_db.close()
 except Exception as e:
     print("Database does not exist")

if __name__ == "__main__":
    main()

