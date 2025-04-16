from scripts.utilitaries.constants import SAVE_FILE
import json
import os


def load_saves():
    if not os.path.exists(SAVE_FILE):
        return [None, None, None]
    with open(SAVE_FILE, "r") as f:
        return json.load(f)
    

def load_upgrades():
    with open("data/upgrades.json", "r") as f:
        return json.load(f)["upgrades"]
    

def save_to_file(slot_index, data):
    saves = load_saves()
    saves[slot_index] = data
    with open(SAVE_FILE, "w") as f:
        json.dump(saves, f)


def load_default_save():
    with open("data/default_save.json", "r") as f:
        return json.load(f)


def delete_save(slot_index):
    if not os.path.exists(SAVE_FILE):
        return
    saves = load_saves()
    saves[slot_index] = None
    with open(SAVE_FILE, "w") as f:
        json.dump(saves, f)


def update_stats(slot_index, data):
    saves = load_saves()
    saves[slot_index]["player_stats"] = data
    with open(SAVE_FILE, "w") as f:
        json.dump(saves, f)