
from pathlib import Path

directors = [
    "Steven Spielberg",
    "Christopher Nolan",
    "Martin Scorsese",
    "Quentin Tarantino",
    "James Cameron",
    "Ridley Scott",
    "Francis Ford Coppola",
    "Clint Eastwood",
    "Peter Jackson",
    "Kathryn Bigelow"
]

file_path = Path('directors.txt')

try:
    if not file_path.exists():
        file_path.touch()
except PermissionError:
    print(f"Error: Permission denied to create file '{file_path}'.")
except OSError as e:
    print(f"Error: OS error occurred while creating file: {e}")

try:
    with file_path.open('w') as file:
        for director in directors:
            file.write(f'{director}\n')
except PermissionError:
    print(f"Error: Permission denied to write to '{file_path}'.")
except IOError as e:
    print(f"Error: I/O error occurred while writing: {e}")

try:
    with file_path.open('r') as file:
        print(file.read())
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except PermissionError:
    print(f"Error: Permission denied to read '{file_path}'.")
except IOError as e:
    print(f"Error: I/O error occurred while reading: {e}")


