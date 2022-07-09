from os.path import isfile
from json import dump, load


class JsonManager:
    """Manusear .jsons"""

    def __init__(self, filepath):  # filepath é o nome do .json
        self.filepath = filepath
    
    def __getitem__(self, items):
        return self.read_json()[items]

    def create_json(self):  # cria o .json
        data = {}

        with open(self.filepath, 'w', encoding='utf-8') as f:
            dump(data, f, indent=2, separators=(',', ': '))

    def read_json(self):  # retorna o json em dicionário
        if isfile(self.filepath):
            with open(self.filepath, encoding='utf-8') as f:
                data = load(f)
            return data

    def update_json(self, data):  # reescreve o json
        with open(self.filepath, 'w', encoding='utf-8') as f:
            dump(data, f, indent=2, separators=(',', ': '))
