import json

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
            money = int(line[2])
            province = line[3]
            record = Record(date, order_id, money, province)
            record_list.append(record)

        f.close()
        return record_list

class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self):
        f = open(self.path, "r", encoding="utf-8")

        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], data_dict["money"], data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list

if __name__ == "__main__":
    text_file_reader = TextFileReader("January2023SalesData.txt")
    record_list = text_file_reader.read_data()
    for record in record_list:
        print(record)

    json_file_reader = JsonFileReader("February2023SalesData.txt")
    record_list2 = json_file_reader.read_data()
    for record in record_list2:
        print(record)