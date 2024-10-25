import mysql.connector 
from mysql.connector import errorcode

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
 except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
     

if __name__ == "__main__":
    main()

