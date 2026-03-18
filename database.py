import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",  # CHANGE THIS
        database="event_system"
    )

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # USERS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(100) UNIQUE,
        password VARCHAR(255),
        role VARCHAR(20)
    )
    """)

    # VENUES
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS venues (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        capacity INT
    )
    """)

    # EVENTS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        type VARCHAR(50),
        date DATE,
        venue VARCHAR(100),
        planned_budget FLOAT,
        created_by VARCHAR(100)
    )
    """)

    # EXPENSES
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INT AUTO_INCREMENT PRIMARY KEY,
        event_id INT,
        vendor VARCHAR(100),
        amount FLOAT
    )
    """)

    # PARTICIPANTS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS participants (
        id INT AUTO_INCREMENT PRIMARY KEY,
        event_id INT,
        name VARCHAR(100),
        attended BOOLEAN
    )
    """)

    # FEEDBACK
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INT AUTO_INCREMENT PRIMARY KEY,
        event_id INT,
        comment TEXT,
        rating INT
    )
    """)

    # Add Pune venues if empty
    cursor.execute("SELECT COUNT(*) FROM venues")
    if cursor.fetchone()[0] == 0:
        venues = [
            ("Balewadi Stadium Convention Hall", 2000),
            ("MIT World Peace University Auditorium", 1500),
            ("Symbiosis Auditorium Lavale", 1000),
            ("JW Marriott Pune Conference Hall", 500),
            ("The Orchid Hotel Pune Banquet Hall", 400)
        ]
        for v in venues:
            cursor.execute("INSERT INTO venues (name,capacity) VALUES (%s,%s)", v)

    conn.commit()
    conn.close()