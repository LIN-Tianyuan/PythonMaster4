from file_define import TextFileReader, JsonFileReader
from data_define import Record
from pymysql import Connection

text_file_reader = TextFileReader("January2023SalesData.txt")
json_file_reader = JsonFileReader("February2023SalesData.txt")

jan_data: list = text_file_reader.read_data()
feb_data: list = json_file_reader.read_data()
all_data: list = jan_data + feb_data

for data in all_data:
    print(data)

conn = Connection(
    host="localhost",
    port=3306,
    user='root',
    password='MySQL@2026!',
    autocommit=True
)

try:
    cursor = conn.cursor()
    conn.select_db("py_sql")
    for record in all_data:
        sql = "insert into orders(order_date, order_id, money, province) values (%s, %s, %s, %s);"
        cursor.execute(sql, (record.date, record.order_id, record.money, record.province))
finally:
    conn.close()