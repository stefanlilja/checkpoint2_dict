import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="dict",
   user="postgres",
   password="continuousimpliesintegrable"
)

def read_dict(connection):
    #reads the dictionary from the database
    cur = connection.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_word(connection, word, translation):
    cur = connection.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
def delete_word(connection, ID):
    #deletes a word from the dictionary
    cur = connection.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
def save_dict(connection):
    #commits all changes to the database
    cur = connection.cursor()
    cur.execute("COMMIT;")
    cur.close()

def insert_word(connection, word, translation):
    #inserts a word into the database
    print('word inserted into database')

print("""Welcome to the dictionary program!
Available commands are list, add, delete and quit""")
while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ")
    if cmd == "list":
        print(read_dict(conn))
    elif cmd == "add":
        name = input("  Word: ")
        phone = input("  Translation: ")
        add_word(conn, name, phone)
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
    elif cmd == "quit":
        save_dict(conn)
        exit()
