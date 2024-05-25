import json
from keyboard import record, wait

# Funktion zum Aufzeichnen der Tastensequenz


def record_sequence():
    print("Press key sequence to initiate the battle (ESC to stop)")
    recorded = record(until='esc')
    sequence = [{'name': e.name, 'event_type': e.event_type, 'time': e.time}
                for e in recorded]
    with open('sequence.json', 'w') as f:
        json.dump(sequence, f)
    print("Sequenz recorded and saved.")


if __name__ == "__main__":
    record_sequence()
