import mysql.connector

conn = mysql.connector.connect(
    host="192.168.1.100",
    user="user1",
    password="abc321",
    database="myappdb"
)

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS USUARIOS (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), console VARCHAR(255))")
cursor.execute("CREATE TABLE IF NOT EXISTS JOGOS (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), data_lancamento DATE)")

insert_record = lambda table, values: cursor.execute(f"INSERT INTO {table} VALUES (NULL, %s, %s)", values)

remove_record = lambda table, id: cursor.execute(f"DELETE FROM {table} WHERE id = %s", (id,))

get_all_records = lambda table: cursor.execute(f"SELECT * FROM {table}")

insert_record("USUARIOS", ("Usuário 1", "Console 1"))
insert_record("USUARIOS", ("Usuário 2", "Console 2"))
insert_record("JOGOS", ("Jogo 1", "2023-01-01"))
insert_record("JOGOS", ("Jogo 2", "2023-02-01"))

conn.commit()

get_all_records("USUARIOS")
print("Tabela USUARIOS:")
for row in cursor.fetchall():
    print(row)

get_all_records("JOGOS")
print("Tabela JOGOS:")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
