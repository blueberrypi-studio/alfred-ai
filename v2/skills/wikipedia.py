import wikipedia

class Wikipedia():
    __custom__ = True
    def __init__(self) -> None:
        pass
    
    def wikipedia(self, query):
        query_list = wikipedia.search(f"{query}", 10)
        summary = wikipedia.summary(query_list[0], 2, auto_suggest=False)
        return summary