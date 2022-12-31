from skills import A_Skill

class Read_Notes(A_Skill):
    __custom__ = True

    def read_from_file(self, filename: str) -> list:
        # Generic file reading function
        new_list = []
        with open(filename,'r') as file:
            notes = file.readlines()
        for note in notes:
            new_list.append(note.rstrip())
        return new_list

    def read_notes(self):
        # List all notes in file
        notes = self.read_from_file("data/notes.txt")
        for count, value in enumerate(notes):
            print(f"{count + 1}: {value}")
