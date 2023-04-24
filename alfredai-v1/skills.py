import wikipedia

class Skills:
    def __init__(self):
        # super(Skills, self).__init__()
        self.notes_file = "notes.txt"
        self.skill_list = ["take_notes", "read_notes", "wikipedia"] # add new skills here
        
    
    def choose_skill(self, skill: str):
        """choose which skill to use"""
        # skill = "notes"
        if skill == "take_notes":
            self.take_note()
        if skill == "read_notes":
            self.read_notes()
        if skill == "wikipedia":
            self.wikipedia()

    def get_skills(self):
        "return skill list"
        return self.skill_list

    def write_to_file(self, filename: str, data: list):
        # Generic file writing function
        with open(filename, 'w') as file:
            for item in data:
                file.write(item + "\n")
    
    def read_from_file(self, filename: str) -> list:
        # Generic file reading function
        new_list = []
        with open(self.notes_file,'r') as file:
            notes = file.readlines()
        for note in notes:
            new_list.append(note.rstrip())
        return new_list

    def take_note(self):
        # Add a note to list
        new_list = self.read_from_file(self.notes_file)
        note = input("you: ")
        new_list.append(note)
        self.write_to_file(self.notes_file, new_list)
        print(f'Alfred: I have added "{note.rstrip()}" to your notes :-)')

    def read_notes(self):
        # List all notes in file
        notes = self.read_from_file(self.notes_file)
        for count, value in enumerate(notes):
            print(f"{count + 1}: {value}")

    def wikipedia(self):
        query = input("you: ")

        query_list = wikipedia.search(f"{query}", 10)
        summary = wikipedia.summary(query_list[0], 2, auto_suggest=False)
        print(summary)


if __name__ == "__main__":
    skill = Skills()
    skill.choose_skill("notes")