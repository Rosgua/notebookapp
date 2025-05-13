import datetime

class Nota:
    ''' classe che rapp una nota in un notebook. Offre la possibilità di 
verificare se una stringa data in input matcha con il memo o il tag della nota stessa'''

    last_id = 0

    def __init__(self, memo, tags= ''):
        self.memo = memo
        self.creation_memo = datetime.date.today()
        self.tags= tags
        self.id = Nota.last_id
        Nota.last_id +=1

    def match(self, search_filter):
        if search_filter in self.memo or search_filter in self.tags:
            return True
        return False
class Notebook:
    ''' rapp una collezione di note. permette la gestione di note,
    quindi, modifica, aggiunta e ricerca'''

    def __init__(self):
        'inizializza il notebook come una lista vuota'
        self.notebook= []

    def add_note(self,memo, tags= ''):
        self.nota = Nota(memo= memo, tags = tags)
        self.notebook.append(self.nota)

    def find_id(self,id):
        for nota in self.notebook:
            if str(id) == str(nota.id):
                return nota
        return None

    def update_memo(self, id, new_memo):
        note = self.find_id(id)
        if note:
            note.memo = new_memo
            return f"modifica avvenuta"
        return f"modifica non avvenuta a causa di id non corretto"
            

    def update_tags(self, id, new_tags):
        note = self.find_id(id)
        if note:
            note.tags = new_tags
            return f"modifica avvenuta"
        return f"modifica non avvenuta a causa di id non corretto"
    
    def search(self, filter):
        note_matchate = []
        for nota in self.notebook:
            if nota.match(filter)== True:
                note_matchate.append(nota)
        return note_matchate



                
