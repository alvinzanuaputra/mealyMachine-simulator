import json

def load_mealy_machine(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' tidak ditemukan.")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' memiliki format JSON yang tidak valid.")
        return None

def simulate_mealy_machine(mealy_machine):
    current_state = mealy_machine["initial_state"]
    input_sequence = mealy_machine["input_sequence"]
    transitions = mealy_machine["transitions"]

    output_sequence = ""
    path = [current_state]

    for symbol in input_sequence:
        if current_state in transitions and symbol in transitions[current_state]:
            transition = transitions[current_state][symbol]
            current_state = transition["next_state"]
            output_sequence += transition["output"]
            path.append(current_state)
        else:
            print(f"Transisi tidak valid dari state '{current_state}' dengan input '{symbol}'")
            return

    # Menampilkan hasil simulasi
    print("Path:", " → ".join(path))
    print("Output:", output_sequence)

# Load Mealy Machine dari file JSON
mealy_machine = load_mealy_machine("mealy_machine.json")

if mealy_machine:
    print("\n=== SIMULASI MEALY MACHINE ===")
    simulate_mealy_machine(mealy_machine)
