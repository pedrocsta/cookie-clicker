from json_manager import JsonManager


class DataBase:

    def __init__(self, filepath):
        self.manager = JsonManager(filepath)

    def create_id(self, id_: str): 
        if not self.manager.read_json().get(id_):
            self.manager.update_json({id_: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]})
            
            return self.manager[id_]
        
        return print('ID existente.')
        
    def select_id(self, id_: str):
        dada = self.manager.read_json()
            
        if dada.get(id_):
            return dada[id_]

        return print("ID inválido.")
