 
import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "",
    database = "codearena_db"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE codearena")
#mycursor.execute("SHOW DATABASES")


#for db in mycursor:
#    print(db)


print("\n" + "=" * 60)
print("Creating TABLE: tournaments")
print("=" * 60)
mycursor.execute("""CREATE TABLE IF NOT EXISTS tournaments (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL, description TEXT,start_date DATE,end_date DATE, status ENUM('upcoming', 'active', 'completed') DEFAULT 'upcoming', max_players INT DEFAULT 100, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP) """)

mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)
