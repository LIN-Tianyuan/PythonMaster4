# Une base de données permet de stocker, d'organiser et de retrouver des informations.
# PyMySQL est une bibliothèque qui permet à Python de communiquer avec une base de données MySQL.

from pymysql import Connection

# Pour communiquer avec une base de données, nous devons d'abord établir une connexion.

conn = Connection(
    # Le serveur se trouve sur notre propre ordinateur
    host="localhost",
    port=3306,
    user='root',
    password='MySQL@2026!'
)

# print(conn.get_server_info())
# Maintenant que nous sommes connectés à MySQL, nous voulons exécuter une requête SQL.
# Nous allons utiliser un objet qui s'appelle un curseur, en anglais <cursor>.
# Le curseur permet d'envoyer des commandes SQL à MySQL et de récupérer les résultats.
try:
    cursor = conn.cursor()
    conn.select_db("class4")
    # exécuter une requête SQL
    cursor.execute("select * from student;")
    # récupérer toutes les lignes du résultat
    results = cursor.fetchall()
    for student in results:
        print(student)
    cursor.close()
finally:
    conn.close()