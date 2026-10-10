import pymysql

connection = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="MySQL@2026!",
    database="class4"
)

try:
    cursor = connection.cursor()
    # 1. Nous écrivons directment les valeurs dans la requête SQL
    # sql = "insert into student (id, name, age, gender) values (10001, 'Leo', 18, 'Homme');"
    # 2. Nous remplaçons les valeurs par %s.
    # Nous séparons la requête SQL des données que nous voulons insérer.
    # requête paramétrée
    sql = "insert into student (id, name, age, gender) values (%s, %s, %s, %s);"
    cursor.execute(sql, (10006, "Luna", 25, "Femme"))
    # Permet d'enregistrer définitivement les modifications de la transaction
    connection.commit()
    cursor.close()
finally:
    # Fermer la connexion
    connection.close()