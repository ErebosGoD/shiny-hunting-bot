import json
from keyboard import record, wait

# Funktion zum Aufzeichnen der Tastensequenz


def record_sequence():
    print("Drücke die Tasten für die Sequenz zum Starten des Kampfes (ESC zum Beenden)")
    recorded = record(until='esc')
    sequence = [{'name': e.name, 'event_type': e.event_type, 'time': e.time}
                for e in recorded]
    with open('sequence.json', 'w') as f:
        json.dump(sequence, f)
    print("Sequenz aufgezeichnet und gespeichert.")


if __name__ == "__main__":
    record_sequence()
