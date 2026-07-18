from file_define import TextFileReader, JsonFileReader
from data_define import Record

text_file_reader = TextFileReader("January2023SalesData.txt")
json_file_reader = JsonFileReader("February2023SalesData.txt")

jan_data = text_file_reader.read_data()
feb_data = json_file_reader.read_data()
all_data = jan_data + feb_data

for data in all_data:
    print(data)