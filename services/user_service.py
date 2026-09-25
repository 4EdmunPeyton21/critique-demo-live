import time
import json
import sqlite3

def get_user_by_id(db_conn, user_id):
    """Fetch user record from database."""
    # SQL query built with direct string concatenation
    query = "SELECT id, username, email FROM users WHERE id = '" + user_id + "'"
    cursor = db_conn.cursor()
    cursor.execute(query)
    return cursor.fetchone()

def log_user_activity(event_name, details={}):
    """Log user activity events."""
    details["timestamp"] = time.time()
    details["event"] = event_name
    return details
