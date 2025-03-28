# **Mealy Machine Simulator**

| Nama                             | NRP        | Kelas     |
| -------------------------------- | ---------- | --------- |
| Alvin Zanua Putra                | 5025231064 | Otomata E |
| Pramudtya Faiz Ardiansyah        | 5025231108 | Otomata E |
| Christoforus Indra Bagus Pratama | 5025231124 | Otomata E |
| Muhammad Azhar Aziz              | 5025231131 | Otomata E |

## **Pengaplikasian**
**Simulator Mealy Machine**, sebuah jenis finite state machine yang menghasilkan output berdasarkan **state saat ini** dan **input yang diberikan**.  
Simulator ini membaca **file JSON eksternal** yang berisi konfigurasi Mealy Machine, kemudian menjalankan simulasi berdasarkan **urutan input**, mencatat jalur transisi, dan mencetak output sesuai aturan transisi.

---

## **Struktur Proyek**
```bash
/mealy-simulator
│── mealy_simulator.py # Program utama untuk simulasi Mealy Machine 
│── mealy_machine.json # File konfigurasi Mealy Machine dalam format JSON 
│── README.md # Dokumentasi proyek
```
---

## Persyaratan
- **Python 3.x**
- **File konfigurasi Mealy Machine dalam format JSON** 

---

## Instalasi & Menjalankan Program
### 1. Clone atau Unduh Proyek
```bash
git clone https://github.com/alvinzanuaputra/mealyMachine-simulator.git
cd mealyMachine-simulator
```

### 2. Jalankan Program
```bash
python mealy_simulator.py
```

---

## Format Input (JSON)
File **`dfa_config.json`** berisi contoh konfigurasi DFA.
```json
{
    "states": [
        "q0",
        "q1",
        "q2"
    ],
    "transitions": {
        "q0": {
            "0": {
                "next_state": "q1",
                "output": "A"
            },
            "1": {
                "next_state": "q2",
                "output": "B"
            }
        },
        "q1": {
            "0": {
                "next_state": "q0",
                "output": "B"
            },
            "1": {
                "next_state": "q2",
                "output": "C"
            }
        },
        "q2": {
            "0": {
                "next_state": "q1",
                "output": "C"
            },
            "1": {
                "next_state": "q0",
                "output": "A"
            }
        }
    },
    "initial_state": "q0",
    "input_sequence": "011001"
}
```
**Keterangan:**
- **states**: Daftar semua state dalam Mealy Machine.
- **transitions**: Aturan transisi berdasarkan state saat ini dan input yang diberikan.
- **initial_state**: State awal Mealy Machine.
- **input_sequence**: Urutan input yang akan diuji.


---

## Kode Program
### `mealy_simulator.py`
```python
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
```

---

## Contoh Output

### **Kasus: `input_sequence = "011001"`**

```bash
=== SIMULASI MEALY MACHINE ===
Path: q0 → q1 → q2 → q0 → q1 → q0 → q2
Output: ACAABB
```

Pada Kasus ini dengan input "011001", mesin dimulai di state q0 dan bergerak melalui state q1, q2, kembali ke q0, lalu ke q1 dan akhirnya ke q2. Proses ini menghasilkan output "ACAABB". Dalam hal ini, setiap simbol input (0 atau 1) memicu transisi antar state, dan output yang sesuai dihasilkan pada setiap langkah.

---

## Overview Output

```bash
ASUS@ASUSTUF-ALVINZP MINGW64 ~/Desktop/Project/Semester 4/Otomata/W5
$ "D:/Data Aplikasi/Python/python.exe" "c:/Users/ASUS/Desktop/Project/Semester 4/Otomata/W5/mealy_simulator.py"

=== SIMULASI MEALY MACHINE ===
Path: q0 → q1 → q2 → q0 → q1 → q0 → q2
Output: ACAABB

ASUS@ASUSTUF-ALVINZP MINGW64 ~/Desktop/Project/Semester 4/Otomata/W5
$
```


## Kesimpulan 

Secara keseluruhan, ini menggambarkan bagaimana Mealy Machine memproses input berdasarkan aturan transisi yang ada, menghasilkan jalur transisi yang berbeda-beda, dan akhirnya menghasilkan output yang sesuai dengan setiap langkah transisi yang dilalui.

---
# Terima Kasih 🤝🤝
# mealyMachine-simulator
