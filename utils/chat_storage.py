import json
import os

CHAT_FILE = 'chat_history.json'
def load_chat():
    if not os.path.exists(CHAT_FILE):
        return []
    with open(CHAT_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)
def save_chat(messages):
    with open(CHAT_FILE, 'w', encoding='utf-8') as file:
        json.dump(messages, file, indent=4)