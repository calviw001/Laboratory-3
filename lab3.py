#lab3.py

# Starter code for lab 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Calvin Wong
# calviw8@uci.edu
# 36522374


from pathlib import Path


def open_file(notes_file):
    try:
        show_notes(notes_file)
    except FileNotFoundError:
        with notes_file.open(mode="a") as file:
            pass


def show_notes(notes_file):
    print()
    with notes_file.open(mode="r") as file:
        for note in file:
            print(note)


def write_notes(notes_file):
    with notes_file.open(mode="a") as file:
        print("Please enter a new note (enter q to exit): ",end='')
        user_note = input()
        while True:
            if user_note == 'q':
                break
            else:
                file.writelines([user_note + '\n'])
                print("Please enter a new note (enter q to exit): ",end='')
                user_note = input()


def main():
    print("Welcome to PyNote!")
    print("Here are your notes: ")
    notes_file = Path("pynotes.txt")
    open_file(notes_file)
    write_notes(notes_file)


main()
