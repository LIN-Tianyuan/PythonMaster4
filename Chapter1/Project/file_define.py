class FileReader:
    def read_data(self):
        pass

class TextFileReader(FileReader):
    def read_data(self):
        # Réaliser:
        # 1. Lire et récuperer des données en 'January2023'
        # 2. Chaque ligne: 2023-01-01,4b34218c-9f37-4e66-b33e-327ecd5fb897,1689,湖南省
        # -> record = Record("2023-01-01", "4b34218c-9f37-4e66-b33e-327ecd5fb897", 1689, "湖南省")
        #     print(record)
        # 3. Afficher tous les records
        pass