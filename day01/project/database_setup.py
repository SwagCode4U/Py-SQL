"""
================================================================================
CodeArena Day 1 - Project: Database and Tables Setup
================================================================================
Topic: Python Basics + MySQL Database Creation
Description: Pehla din hai! Hum CodeArena ka foundation daal rahe hain.
             MySQL mein database aur tables create karenge.
================================================================================
"""

# MySQL connector library import karo
# Yeh library Python ko MySQL se baat karne deti hai
import mysql.connector
from mysql.connector import Error

# Database connection ke liye credentials
# Yeh aapke MySQL server ke details hain
DB_CONFIG = {
    'host': 'localhost',        # MySQL server ka address (local machine pe)
    'user': 'root',             # MySQL username (default: root)
    'password': ''              # MySQL password (aapna password daalo)
}

# Database ka naam jisko hum create karenge
DATABASE_NAME = 'codearena_db'

def create_database():
    """
    Yeh function MySQL mein naya database create karta hai
    Agar database pehle se exist karta hai, toh koi error nahi aayega
    """
    try:
        # Step 1: MySQL server se connect karo (without database)
        # Pehle sirf server se connect karna hai, database select nahi karna
        print("MySQL server se connect kar rahe hain...")
        connection = mysql.connector.connect(**DB_CONFIG)
        
        # Step 2: Cursor object create karo
        # Cursor SQL queries execute karne ke liye use hota hai
        cursor = connection.cursor()
        print("Connection successful!")
        
        # Step 3: Database create karne ki SQL query
        # IF NOT EXISTS matlab agar database pehle se hai toh dubara nahi banayega
        create_db_query = f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"
        
        # Step 4: Query execute karo
        cursor.execute(create_db_query)
        print(f"✓ Database '{DATABASE_NAME}' create ho gaya!")
        
        # Step 5: Saari databases dikhayo
        cursor.execute("SHOW DATABASES")
        print("\nAvailable Databases:")
        print("-" * 30)
        for db in cursor:
            print(f"  • {db[0]}")  # db[0] se database ka naam milta hai
        
        # Step 6: Cursor aur connection close karo
        # Resources free karne ke liye important hai
        cursor.close()
        connection.close()
        print("\n✓ Database creation complete!")
        
        return True
        
    except Error as e:
        # Agar koi error aata hai, toh yeh block execute hoga
        print(f"\n✗ Error aaya: {e}")
        print("Tips:")
        print("  1. Check karo MySQL server chalu hai ya nahi")
        print("  2. Username aur password sahi hain ya nahi")
        print("  3. MySQL installed hai ya nahi")
        return False

def create_tables():
    """
    Yeh function database ke andar tables create karta hai
    CodeArena ke 4 main tables banayenge:
    1. players - Player information store hoga
    2. tournaments - Tournament details store honge
    3. scores - Match scores store honge
    4. badges - Player badges store honge
    """
    try:
        # Database select karke connection karo
        db_config_with_db = DB_CONFIG.copy()  # Original config copy karo
        db_config_with_db['database'] = DATABASE_NAME  # Database naam add karo
        
        print(f"\n'{DATABASE_NAME}' database se connect kar rahe hain...")
        connection = mysql.connector.connect(**db_config_with_db)
        cursor = connection.cursor()
        print("Connection successful!")
        
        # ================================================================
        # TABLE 1: PLAYERS
        # ================================================================
        print("\n" + "=" * 60)
        print("Creating TABLE: players")
        print("=" * 60)
        
        create_players_table = """
        CREATE TABLE IF NOT EXISTS players (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            email VARCHAR(100) NOT NULL UNIQUE,
            xp INT DEFAULT 0,
            level INT DEFAULT 1,
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        # Query explanation:
        # id - Unique player ID, automatically increment hota hai
        # username - Player ka naam (max 50 chars), UNIQUE matlab same naam do baar nahi
        # email - Player ka email (max 100 chars), UNIQUE matlab same email do baar nahi
        # xp - Experience points, default 0 se start
        # level - Player level, default 1 se start
        # is_active - Account active hai ya nahi, default True
        # created_at - Account kab create hua, automatic timestamp
        
        cursor.execute(create_players_table)
        print("✓ Table 'players' create ho gaya!")
        
        # ================================================================
        # TABLE 2: TOURNAMENTS
        # ================================================================
        print("\n" + "=" * 60)
        print("Creating TABLE: tournaments")
        print("=" * 60)
        
        create_tournaments_table = """
        CREATE TABLE IF NOT EXISTS tournaments (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description TEXT,
            start_date DATE,
            end_date DATE,
            status ENUM('upcoming', 'active', 'completed') DEFAULT 'upcoming',
            max_players INT DEFAULT 100,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        # Query explanation:
        # name - Tournament ka naam (max 100 chars)
        # description - Tournament ki details (TEXT type = bada text)
        # start_date - Tournament kab shuru hoga
        # end_date - Tournament kab khatam hoga
        # status - ENUM matlab sirf 3 values allowed: upcoming/active/completed
        # max_players - Kitne players join kar sakte hain
        
        cursor.execute(create_tournaments_table)
        print("✓ Table 'tournaments' create ho gaya!")
        
        # ================================================================
        # TABLE 3: SCORES
        # ================================================================
        print("\n" + "=" * 60)
        print("Creating TABLE: scores")
        print("=" * 60)
        
        create_scores_table = """
        CREATE TABLE IF NOT EXISTS scores (
            id INT AUTO_INCREMENT PRIMARY KEY,
            player_id INT NOT NULL,
            tournament_id INT NOT NULL,
            points INT DEFAULT 0,
            match_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (player_id) REFERENCES players(id) ON DELETE CASCADE,
            FOREIGN KEY (tournament_id) REFERENCES tournaments(id) ON DELETE CASCADE
        )
        """
        # Query explanation:
        # player_id - Konsa player (players table ka id reference)
        # tournament_id - Konsa tournament (tournaments table ka id reference)
        # points - Kitne points mile match mein
        # match_date - Match kab khela gaya

        # FOREIGN KEY - Relationship establish karti hai do tables ke beech
        # ON DELETE CASCADE - Agar player/tournament delete ho toh scores bhi delete ho
        
        cursor.execute(create_scores_table)
        print("✓ Table 'scores' create ho gaya!")
        
        # ================================================================
        # TABLE 4: BADGES
        # ================================================================
        print("\n" + "=" * 60)
        print("Creating TABLE: badges")
        print("=" * 60)
        
        create_badges_table = """
        CREATE TABLE IF NOT EXISTS badges (
            id INT AUTO_INCREMENT PRIMARY KEY,
            player_id INT NOT NULL,
            badge_name VARCHAR(50) NOT NULL,
            badge_description VARCHAR(255),
            unlocked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (player_id) REFERENCES players(id) ON DELETE CASCADE
        )
        """
        # Query explanation:
        # badge_name - Badge ka naam jaise 'First Win', 'Level 10', etc.
        # badge_description - Badge ki description
        # unlocked_at - Kab badge mila
        
        cursor.execute(create_badges_table)
        print("✓ Table 'badges' create ho gaya!")
        
        # ================================================================
        # SHOW ALL TABLES
        # ================================================================
        print("\n" + "=" * 60)
        print("All Tables in Database")
        print("=" * 60)
        
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()  # Saare results fetch karo
        
        for i, table in enumerate(tables, 1):
            print(f"{i}. {table[0]}")  # table[0] mein table name hai
        
        # ================================================================
        # CLEANUP
        # ================================================================
        cursor.close()
        connection.close()
        
        print("\n" + "=" * 60)
        print("✓ CODEARENA DATABASE SETUP COMPLETE!")
        print("=" * 60)
        print(f"\nDatabase Name: {DATABASE_NAME}")
        print(f"Total Tables Created: {len(tables)}")
        print("\nReady for Day 2!")
        
        return True
        
    except Error as e:
        print(f"\n✗ Table creation mein error: {e}")
        return False

def main():
    """
    Main function jo database aur tables create karta hai
    """
    print("\n" + "=" * 60)
    print("   CodeArena - Day 1: Database Setup")
    print("=" * 60)
    print("\nGoal: MySQL database aur tables create karna")
    print("\nStep 1: Database create karo")
    print("Step 2: Tables create karo")
    print("\n" + "-" * 60)
    
    # Pehle database create karo
    if create_database():
        # Phir tables create karo
        create_tables()
    else:
        print("\nDatabase create nahi hua. Tables nahi ban payenge.")
        print("Pehle MySQL server check karo aur phir dobara try karo.")

# Program yahan se shuru hota hai
if __name__ == "__main__":
    main()

"""
================================================================================
DAY 1 SUMMARY:
================================================================================
✓ MySQL se connection banana sikha
✓ Database create karna sikha (CREATE DATABASE)
✓ Tables create karna sikha (CREATE TABLE)
✓ Data types sikhe (INT, VARCHAR, TEXT, DATE, TIMESTAMP, BOOLEAN, ENUM)
✓ Primary Key aur Foreign Key sikhe
✓ Constraints sikhe (NOT NULL, UNIQUE, DEFAULT)

SQL Queries Covered:
1. CREATE DATABASE IF NOT EXISTS database_name
2. SHOW DATABASES
3. CREATE TABLE table_name (columns...)
4. SHOW TABLES
5. PRIMARY KEY, FOREIGN KEY, AUTO_INCREMENT

Next: Day 2 - Functions aur INSERT queries
================================================================================
"""
