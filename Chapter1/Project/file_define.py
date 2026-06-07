from data_define import Record


class FileReader:
    def read_data(self):
        pass

class TextFileReader(FileReader):
    path = None

    def __init__(self, path):
        self.path = path

    def read_data(self):
        f = open(self.path, "r", encoding="utf-8")

        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()
            line = line.split(",")
            date = line[0]
            order_id = line[1]
            money = line[2]
            province = line[3]
            record = Record(date, order_id, money, province)
            record_list.append(record)

        f.close()
        return record_list

class JsonFileReader(FileReader):
    pass

if __name__ == "__main__":
    text_file_reader = TextFileReader("January2023SalesData.txt")
    text_file_reader.read_data()