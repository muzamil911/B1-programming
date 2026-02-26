import sqlite3

class UserStore:
    def __init__(self, db_path):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        """Creates the users table if it doesn't exist."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    full_name TEXT
                )
            """)
            conn.commit()

    def load(self):
        """Returns all users as a list of dictionaries."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row  # This allows us to access data by column name
            cursor = conn.execute("SELECT * FROM users")
            return [dict(row) for row in cursor.fetchall()]

    def find_by_id(self, user_id):
        """Returns a single user dictionary or None."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            row = cursor.fetchone()
            return dict(row) if row else None

    def save_new_user(self, user_data):
        """Inserts a new user and returns the new ID."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "INSERT INTO users (username, email, full_name) VALUES (?, ?, ?)",
                (user_data['username'], user_data['email'], user_data.get('full_name'))
            )
            conn.commit()
            return cursor.lastrowid

    def update_user(self, user_id, updated_data):
        """Extension: Updates user by ID using SQL."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "UPDATE users SET username = ?, email = ?, full_name = ? WHERE id = ?",
                (updated_data['username'], updated_data['email'], updated_data['full_name'], user_id)
            )
            conn.commit()
            return cursor.rowcount > 0

    def delete_user(self, user_id):
        """Extension: Removes user by ID using SQL."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()
            return cursor.rowcount > 0