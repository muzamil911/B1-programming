import json
import os

class UserStore:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        """Requirement: Returns list of user dicts & handles FileNotFoundError."""
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []

    def save(self, users):
        """Requirement: Writes users as formatted JSON."""
        with open(self.file_path, "w") as f:
            json.dump(users, f, indent=4)

    def find_by_id(self, user_id):
        """Requirement: Returns user dict or None."""
        users = self.load()
        return next((u for u in users if u["id"] == user_id), None)

    # Extension Challenges
    def update_user(self, user_id, updated_data):
        users = self.load()
        for i, user in enumerate(users):
            if user["id"] == user_id:
                # Update fields while keeping the original ID
                users[i].update(updated_data)
                users[i]["id"] = user_id 
                self.save(users)
                return True
        return False

    def delete_user(self, user_id):
        users = self.load()
        initial_len = len(users)
        users = [u for u in users if u["id"] != user_id]
        if len(users) < initial_len:
            self.save(users)
            return True
        return False