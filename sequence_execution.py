import time
import pyautogui
import json

# Funktion zur Ausführung einer Tastensequenz


def execute_sequence(filename):
    with open(filename, 'r') as file:
        sequence = json.load(file)

    start_time = sequence[0]['time']  # Startzeit der Sequenz

    for i, event in enumerate(sequence):
        current_time = event['time']
        time_since_start = current_time - start_time
        # Verzögerung entsprechend der Zeit seit dem Start
        time.sleep(time_since_start)
        start_time = current_time  # Aktualisierung der Startzeit für die nächste Iteration

        if event['event_type'] == 'down':
            pyautogui.keyDown(event['name'])
        elif event['event_type'] == 'up':
            pyautogui.keyUp(event['name'])

        # Wenn es nicht das letzte Event in der Sequenz ist, lass die vorherige Taste los
        if i < len(sequence) - 1:
            previous_event = sequence[i - 1]
            pyautogui.keyUp(previous_event['name'])
        # print(event)
