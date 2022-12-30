
class Take_Notes():
    __custom__ = True
    def __init__(self) -> None:
        self.filename = "../data/notes.txt"
        
    def take_notes(self):
        # Add a note to list
        new_list = self.read_from_file(self.filename)
        note = input("you: ")
        new_list.append(note)
        self.write_to_file(self.filename, new_list)
        print(f'Alfred: I have added "{note.rstrip()}" to your notes :-)')
    
    def write_to_file(self, filename: str, data: list):
        # Generic file writing function
        with open(filename, 'w') as file:
            for item in data:
                file.write(item + "\n")


    def read_from_file(self, filename: str) -> list:
        # Generic file reading function
        new_list = []
        with open(self.filename,'r') as file:
            notes = file.readlines()
        for note in notes:
            new_list.append(note.rstrip())
        return new_list














