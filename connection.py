import mysql.connector
import shortuuid


class login_table:
    def __init__(self):
        self.host = "localhost"
        self.database = "marketPlace"
        self.user = "root"
        self.password = "loba"
        self.data = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        

    def sign_up(self, username, passwd, email, status):
        try:
            # username = input("Enter Username: ")
            # passwd = input("Enter Password: ")
            # Email = input("Enter Email: ")
            uid = shortuuid.ShortUUID().random(length=15)
            print(uid)

            mycursor = self.data.cursor()

            sql = "INSERT INTO login_table (username, passwd, email, user_id) VALUES (%s, %s, %s, %s, %s)"
            val = (username, passwd, email, uid, status)
            mycursor.execute(sql, val)

            self.data.commit()
            print("log in successfull")

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
            if not record:
                print("Not found")
                return False
            else:
                print("found")
                return True
        except mysql.connector.Error as error:
            print("Failed to get record from MySQL table: {}".format(error))


#test = login_table("localhost")
#test.log_in("loba@gmail.com", "123456")
#test.sign_up("daveLedder", "123qwe", "daveled@gmail.com", 1)
#test.log_in("daveled@gmail.com", "123qwe")
