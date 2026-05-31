class Record:
    date = None
    order_id = None
    money = None
    province = None

    def __init__(self, date, order_id, money, province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):
        return f"date={self.date}, order_id={self.order_id}, money={self.money}, province={self.province}"

if __name__ == "__main__":
    record = Record("2023-01-01", "4b34218c-9f37-4e66-b33e-327ecd5fb897", 1689, "湖南省")
    print(record)
