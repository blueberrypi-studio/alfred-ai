import wikipedia
from skills import A_Skill

class Wikipedia(A_Skill):
    __custom__ = True
    
    def wikipedia(self, query):
        
        query_list = wikipedia.search(f"{query}", 10)
        summary = wikipedia.summary(query_list[0], 2, auto_suggest=False)
        return summary