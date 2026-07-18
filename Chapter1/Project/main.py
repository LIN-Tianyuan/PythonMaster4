from pyecharts.options import InitOpts, LabelOpts, TitleOpts

from file_define import TextFileReader, JsonFileReader
from data_define import Record

from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

text_file_reader = TextFileReader("January2023SalesData.txt")
json_file_reader = JsonFileReader("February2023SalesData.txt")

jan_data = text_file_reader.read_data()
feb_data = json_file_reader.read_data()
all_data = jan_data + feb_data


# {"2023-01-01": 1689}
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        # La date actuelle a déjà été enregistrée.
        # Il suffit donc de l'additionner avec les anciens enregistrements
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

print(data_dict)

bar = Bar(
    init_opts=InitOpts(
        theme=ThemeType.LIGHT,
        width="1200px",
        height="600px"
    )
)

bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("Sales", list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(title_opts=TitleOpts(title="Daily Sales"))

bar.render("Daily sales bar chart.html")
