from json_manager import JsonManager


class DataBase:

    def __init__(self, filepath) -> None:
        self.manager = JsonManager(filepath)

    def create_id(self, id_: str): 
        if not self.manager.read_json().get(id_):
            self.manager.update_json({id_: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, True]})
            
            return self.manager[id_]
        
        return print('ID existente.')
        
    def select_id(self, id_: str):
        dados = self.manager.read_json()
            
        if dados.get(id_):
            return dados[id_] 

        return print("ID inválido.")
