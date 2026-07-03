from collections import defaultdict

memory = defaultdict(list)

class SessionMemory:
    def __init__(self):
        self.data = {}

    def set(self, session_id, key, value):
        if session_id not in self.data:
            self.data[session_id] = {}
        self.data[session_id][key] = value

    def get(self, session_id, key):
        return self.data.get(session_id, {}).get(key)

    def get_all(self, session_id):
        return self.data.get(session_id, {})