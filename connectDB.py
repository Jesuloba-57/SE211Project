import mysql.connector
import shortuuid


class mkDB:
    def __init__(self):
        self.host = "localhost"
        self.database = "marketPlace"
        self.user = "root"
        self.password = "loba"
        self.data = mysql.connector.connect(
            host=self.host, database=self.database, user=self.user, password=self.password)

    def login(self, passwd, email, status):
        try:
            # username = input("Enter Username: ")
            # passwd = input("Enter Password: ")
            # Email = input("Enter Email: ")
            # uid = shortuuid.ShortUUID().random(length=15)
            # print(uid)

            mycursor = self.data.cursor()

            sql = "INSERT INTO login_table (u_id, email, passwd, status) VALUES (%s, %s, %s, %s, %s)"
            val = (username, passwd, email, uid, status)
            mycursor.execute(sql, val)

            self.data.commit()
            print(mycursor.rowcount, "record inserted.")

        except mysql.connector.Error as error:
            print("Failed to insert record into Laptop table {}".format(error))

    def signup_buyer(self, ID, fname, lname, Pay, address, phone):
        try:
            mycursor = self.data.cursor()

            sql = "INSERT INTO login_table (ID, fname, lname, Payment_ID, address, phone) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (ID, fname, lname, Pay, address, phone)
            mycursor.execute(sql, val)

            self.data.commit()
            print(mycursor.rowcount, "record inserted.")

        except mysql.connector.Error as error:
            print("Failed to insert record into Laptop table {}".format(error))
