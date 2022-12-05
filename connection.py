import mysql.connector
import shortuuid

class login_table:
    def __init__(self):
        self.host = "localhost"
        self.database = "marketPlace"
        self.user = "root"
        self.password = "loba"
        self.data = mysql.connector.connect(self.host, self.database, self.user, self.password)
        

    def sign_up(self, username, passwd, email):
        try:
            

            # username = input("Enter Username: ")
            # passwd = input("Enter Password: ")
            # Email = input("Enter Email: ")
            uid = shortuuid.ShortUUID().random(length=15)
            print(uid)

            mycursor = self.data.cursor()

            sql = "INSERT INTO login_table (username, passwd, email, user_id) VALUES (%s, %s, %s, %s)"
            val = (username, passwd, email, uid)
            mycursor.execute(sql, val)

            self.data.commit()

            print(mycursor.rowcount, "record inserted.")

        except mysql.connector.Error as error:
            print("Failed to insert record into Laptop table {}".format(error))
    
    def log_in(self, email, passwd):
        try:
            mycursor = self.data.cursor()
            record = "placeholder"
            sql = "SELECT user_id FROM login_table WHERE email = %s AND passwd = %s"
            mycursor.execute(sql, (email, passwd))
            record = mycursor.fetchall()
            print(record)
            print("done")
        except mysql.connector.Error as error:
            print("Failed to get record from MySQL table: {}".format(error))

