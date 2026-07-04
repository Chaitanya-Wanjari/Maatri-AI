from collections import defaultdict

MAX_HISTORY = 6

history = defaultdict(list)


def get_history(session_id):
    return history[session_id]


def add_message(session_id, role, content):

    history[session_id].append(
        {
            "role": role,
            "content": content,
        }
    )

    history[session_id] = history[session_id][-MAX_HISTORY:]