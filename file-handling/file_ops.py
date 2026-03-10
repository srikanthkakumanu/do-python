
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{file_name}'.")
    except IOError as e:
        print(f"Error: I/O error occurred while reading '{file_name}': {e}")

def write_file(file_name):
    actors = ["Leonardo DiCaprio",
    "Scarlett Johansson",
    "Tom Hanks",
    "Natalie Portman",
    "Denzel Washington",
    "Emma Stone",
    "Brad Pitt",
    "Meryl Streep",
    "Robert Downey Jr.",
    "Jennifer Lawrence"]

    try:
        with open(file_name, 'w+') as file:
            for line in actors:
                file.write(f'{line}\n')
            file.seek(0, 0)
            content = file.read()
            print(content)
    except PermissionError:
        print(f"Error: Permission denied to write '{file_name}'.")
    except IOError as e:
        print(f"Error: I/O error occurred while writing '{file_name}': {e}")

def append_file(file_name):
    more_actors = [
        "Chris Hemsworth",
        "Viola Davis",
        "Keanu Reeves",
        "Zendaya",
        "Christian Bale",
        "Halle Berry",
        "Matt Damon",
        "Gal Gadot"
    ]

    try:
        with open(file_name, 'a+') as file:
            for line in more_actors:
                file.write(f'{line}\n')
            file.seek(0, 0)
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found. Cannot append.")
    except PermissionError:
        print(f"Error: Permission denied to append to '{file_name}'.")
    except IOError as e:
        print(f"Error: I/O error occurred while appending to '{file_name}': {e}")

def main():
    read_file('actors.txt')
    write_file('hollywood_actors.txt')
    append_file( 'hollywood_actors.txt')

if __name__ == "__main__":
    main()