import os
import json


class Score:
    """
    Clase para gestionar y mantener el puntaje del juego.
    """

    def __init__(self):
        """
        Inicializa la instancia de Score con un puntaje inicial de cero y carga los registros existentes desde 'score.json'.
        """
        self.score = 0
        self.load_records()

    def load_records(self):
        """
        Carga los registros existentes desde el archivo 'score.json'. Si el archivo no existe, crea una estructura inicial.
        """
        self.records = {"scores": []}
        try:
            current_directory = os.path.dirname(__file__)
            file_path = os.path.join(current_directory, "score.json")
            with open(file_path, "r") as f:
                self.records = json.load(f)
        except FileNotFoundError:
            print("El archivo 'score.json' no fue encontrado.")
        except json.JSONDecodeError as e:
            print(f"Error al decodificar el archivo JSON: {e}")

    def save_records(self):
        """
        Guarda los registros actualizados en el archivo 'score.json'.
        """
        try:
            current_directory = os.path.dirname(__file__)
            file_path = os.path.join(current_directory, "score.json")
            with open(file_path, "w") as f:
                json.dump(self.records, f, indent=2)
        except json.JSONDecodeError as e:
            print(f"Error al codificar el archivo JSON: {e}")

    def get_high_score(self):
        """
        Obtiene el puntaje más alto registrado.
        """
        max_record = (
            max(score_data["high_score"] for score_data in self.records["scores"])
            if self.records["scores"]
            else 0
        )
        return max_record

    def delete_record(self, username):
        """
        Elimina un registro específico basado en el nombre de usuario y guarda los cambios.

        Parameters:
        - username (str): El nombre de usuario asociado al registro que se eliminará.
        """
        self.records["scores"] = [
            score_data
            for score_data in self.records["scores"]
            if score_data["username"] != username
        ]
        self.save_records()
        print(f"Record eliminado: {self.records}")

    def add_new_record(self, new_score, username="player_1"):
        """
        Agrega un nuevo registro al puntaje y guarda los cambios.

        Parameters:
        - new_score (int): El nuevo puntaje que se agregará.
        - username (str): El nombre de usuario asociado al nuevo registro.
        """
        self.records["scores"].append({"username": username, "high_score": new_score})
        self.save_records()
        print(f"Nuevo record agregado: {self.records}")

    def compare_and_update_record(self):
        """
        Compara el puntaje actual con el puntaje más alto registrado y actualiza los registros si es necesario.
        """
        current_record = self.get_high_score()
        if self.score > current_record:
            self.delete_record("player_1")
            self.add_new_record(self.score)

    def update_score(self, lines_cleared):
        """
        Actualiza el puntaje según el número de líneas eliminadas.

        Parameters:
        - lines_cleared (int): El número de líneas eliminadas en el juego.
        """
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500

        self.compare_and_update_record()
