from datetime import date, timedelta

class Generate:
    def __init__(self, db: object):
        self.db = db
        self.current_date = str(date.today())

    def client(self):
        self.db.cur.execute('''
            INSERT INTO clientes VALUES(
                NULL, "Pessoa Física", NULL, "09876543210", NULL, "L Rações",
                "Laura", "11966667777", NULL, "07192300", "Avenida", "1100",
                "Bela Vista", "Guarulhos", "SP", NULL, "pendente", NULL, ?,
                NULL
            )
        ''', (self.current_date,))
        self.db.con.commit()

    def ticket(self):
        due_date = str(date.today() + timedelta(days=15))
        self.db.cur.execute(
            '''INSERT INTO boletos VALUES(
                1, NULL, "098712340987", 2100.50, ?, ?, "pendente"
            )''', (self.current_date, due_date,)
        )
        self.db.con.commit()