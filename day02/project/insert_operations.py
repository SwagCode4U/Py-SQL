"""
================================================================================
CodeArena Day 2 - Project: INSERT Operations
================================================================================
Topic: Functions + MySQL INSERT Queries
Description: Aaj hum functions sikhenge aur database mein data insert karenge!
             Players, tournaments, scores aur badges add karna sikhenge.
================================================================================
"""

import mysql.connector
from mysql.connector import Error

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'codearena_db'
}


def get_db_connection():
    """
    Yeh function MySQL database se connection banata hai
    Har baar jab database operation karna ho toh is function ko call karo
    
    Returns:
        connection object - successful connection
        None - agar connection fail ho
    """
    try:
        # MySQL se connect karo
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"✗ Database connection error: {e}")
        return None


def insert_player(username, email, level=1, xp=0):
    """
    Naya player database mein add karta hai
    
    Args:
        username: Player ka unique naam
        email: Player ka email address
        level: Starting level (default: 1)
        xp: Starting XP (default: 0)
    
    Returns:
        player_id: Naye player ka ID
        None: Agar insert fail ho
    """
    connection = get_db_connection()
    if not connection:
        return None
    
    try:
        cursor = connection.cursor()
        
        # INSERT query - naya record add karo
        query = """
        INSERT INTO players (username, email, level, xp)
        VALUES (%s, %s, %s, %s)
        """
        # %s placeholders hain - yahan actual values ayengi
        # Yeh SQL injection se bachata hai
        
        values = (username, email, level, xp)
        # Tuple mein values pass karo
        
        cursor.execute(query, values)
        # Query execute karo
        
        connection.commit()
        # Changes ko database mein permanently save karo
        
        player_id = cursor.lastrowid
        # Naye insert huye record ka ID le lo
        
        print(f"✓ Player '{username}' added! ID: {player_id}")
        
        return player_id
        
    except Error as e:
        print(f"✗ Error adding player: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def insert_tournament(name, description, start_date, end_date, max_players=100):
    """
    Naya tournament create karta hai
    
    Args:
        name: Tournament ka naam
        description: Tournament ki details
        start_date: Shuru hone ki date (YYYY-MM-DD)
        end_date: Khatam hone ki date (YYYY-MM-DD)
        max_players: Maximum players allowed
    
    Returns:
        tournament_id: Naye tournament ka ID
    """
    connection = get_db_connection()
    if not connection:
        return None
    
    try:
        cursor = connection.cursor()
        
        query = """
        INSERT INTO tournaments (name, description, start_date, end_date, max_players)
        VALUES (%s, %s, %s, %s, %s)
        """
        
        values = (name, description, start_date, end_date, max_players)
        
        cursor.execute(query, values)
        connection.commit()
        
        tournament_id = cursor.lastrowid
        print(f"✓ Tournament '{name}' created! ID: {tournament_id}")
        
        return tournament_id
        
    except Error as e:
        print(f"✗ Error creating tournament: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def insert_score(player_id, tournament_id, points):
    """
    Player ke match ka score record karta hai
    
    Args:
        player_id: Konsa player
        tournament_id: Konsa tournament
        points: Kitne points mile
    
    Returns:
        score_id: Naye score record ka ID
    """
    connection = get_db_connection()
    if not connection:
        return None
    
    try:
        cursor = connection.cursor()
        
        query = """
        INSERT INTO scores (player_id, tournament_id, points)
        VALUES (%s, %s, %s)
        """
        
        values = (player_id, tournament_id, points)
        
        cursor.execute(query, values)
        connection.commit()
        
        score_id = cursor.lastrowid
        print(f"✓ Score added! Player {player_id} got {points} points")
        
        return score_id
        
    except Error as e:
        print(f"✗ Error adding score: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def insert_badge(player_id, badge_name, description):
    """
    Player ko badge award karta hai
    
    Args:
        player_id: Konsa player
        badge_name: Badge ka naam
        description: Badge ki description
    
    Returns:
        badge_id: Naye badge ka ID
    """
    connection = get_db_connection()
    if not connection:
        return None
    
    try:
        cursor = connection.cursor()
        
        query = """
        INSERT INTO badges (player_id, badge_name, badge_description)
        VALUES (%s, %s, %s)
        """
        
        values = (player_id, badge_name, description)
        
        cursor.execute(query, values)
        connection.commit()
        
        badge_id = cursor.lastrowid
        print(f"✓ Badge '{badge_name}' awarded to Player {player_id}!")
        
        return badge_id
        
    except Error as e:
        print(f"✗ Error awarding badge: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def insert_multiple_players(players_list):
    """
    Ek saath multiple players insert karta hai
    Efficient for bulk inserts
    
    Args:
        players_list: List of tuples [(username, email, level, xp), ...]
    
    Returns:
        Number of players inserted
    """
    connection = get_db_connection()
    if not connection:
        return 0
    
    try:
        cursor = connection.cursor()
        
        query = """
        INSERT INTO players (username, email, level, xp)
        VALUES (%s, %s, %s, %s)
        """
        
        # executemany() se multiple records ek saath insert
        cursor.executemany(query, players_list)
        connection.commit()
        
        count = cursor.rowcount  # Kitne rows insert hue
        print(f"✓ {count} players added successfully!")
        
        return count
        
    except Error as e:
        print(f"✗ Error in bulk insert: {e}")
        return 0
    finally:
        cursor.close()
        connection.close()


def show_all_players():
    """
    Saare players dikhata hai
    SELECT query ka use karke
    """
    connection = get_db_connection()
    if not connection:
        return
    
    try:
        cursor = connection.cursor()
        
        # SELECT query - data fetch karo
        query = "SELECT id, username, email, level, xp FROM players"
        cursor.execute(query)
        
        # Saare results fetch karo
        players = cursor.fetchall()
        
        print(f"\n{'='*70}")
        print(f"{'ID':<5} {'Username':<15} {'Email':<25} {'Level':<8} {'XP':<10}")
        print(f"{'='*70}")
        
        for player in players:
            # player ek tuple hai: (id, username, email, level, xp)
            print(f"{player[0]:<5} {player[1]:<15} {player[2]:<25} {player[3]:<8} {player[4]:<10}")
        
        print(f"{'='*70}")
        print(f"Total Players: {len(players)}")
        
    except Error as e:
        print(f"✗ Error fetching players: {e}")
    finally:
        cursor.close()
        connection.close()


def main():
    """
    Main function - sab operations yahan se start hote hain
    """
    print("\n" + "=" * 70)
    print("   CodeArena Day 2: INSERT Operations")
    print("=" * 70)
    
    # Step 1: Individual players insert karo
    print("\n--- Adding Individual Players ---")
    player1_id = insert_player("Rahul Kumar", "rahul@codearena.com", 3, 1500)
    player2_id = insert_player("Priya Sharma", "priya@codearena.com", 5, 3500)
    player3_id = insert_player("Amit Patel", "amit@codearena.com", 2, 800)
    
    # Step 2: Multiple players bulk insert
    print("\n--- Bulk Insert Players ---")
    new_players = [
        ("Sonia Gupta", "sonia@codearena.com", 4, 2200),
        ("Vikram Rao", "vikram@codearena.com", 6, 4800),
        ("Neha Verma", "neha@codearena.com", 1, 300),
        ("Arjun Singh", "arjun@codearena.com", 7, 6200)
    ]
    insert_multiple_players(new_players)
    
    # Step 3: Tournaments create karo
    print("\n--- Creating Tournaments ---")
    tour1_id = insert_tournament(
        "Python Championship 2024",
        "Ek nayi tournament Python developers ke liye",
        "2024-03-01",
        "2024-03-31",
        50
    )
    
    tour2_id = insert_tournament(
        "SQL Masters League",
        "Database experts ki tournament",
        "2024-04-01",
        "2024-04-30",
        30
    )
    
    # Step 4: Scores add karo (agar player aur tournament IDs valid hain)
    if player1_id and tour1_id:
        print("\n--- Recording Scores ---")
        insert_score(player1_id, tour1_id, 250)
        insert_score(player2_id, tour1_id, 450)
        insert_score(player3_id, tour1_id, 180)
        insert_score(player1_id, tour2_id, 320)
    
    # Step 5: Badges award karo
    if player1_id:
        print("\n--- Awarding Badges ---")
        insert_badge(player1_id, "First Match", "Pehla match complete kiya")
        insert_badge(player2_id, "High Scorer", "500+ points ek match mein")
        insert_badge(player3_id, "Beginner", "CodeArena join kiya")
    
    # Step 6: Show all players
    print("\n--- All Registered Players ---")
    show_all_players()
    
    print("\n" + "=" * 70)
    print("✓ Day 2 Complete! Data successfully inserted into database!")
    print("=" * 70)


if __name__ == "__main__":
    main()


"""
================================================================================
DAY 2 SUMMARY:
================================================================================

Python Concepts:
✓ Functions definition using def
✓ Parameters and Arguments
✓ Return values
✓ Default parameters
✓ *args aur **kwargs
✓ Lambda functions
✓ Variable scope (global vs local)

MySQL Concepts:
✓ INSERT INTO table VALUES (...)
✓ executemany() for bulk inserts
✓ %s placeholders (SQL injection prevention)
✓ connection.commit() - changes save karna
✓ cursor.lastrowid - last inserted ID
✓ SELECT queries to fetch data

Key Functions:
✓ get_db_connection() - Reusable connection
✓ insert_player() - Single insert
✓ insert_multiple_players() - Bulk insert
✓ insert_tournament() - Tournament create
✓ insert_score() - Score record
✓ insert_badge() - Badge award

SQL Queries Covered:
1. INSERT INTO table (col1, col2) VALUES (%s, %s)
2. INSERT INTO table VALUES (%s, %s, %s)
3. executemany() for multiple records
4. SELECT * FROM table

Next: Day 3 - Modules aur separate DB connection file
================================================================================
"""
