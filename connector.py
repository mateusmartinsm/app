from sql_table_scripts import TableConstructorScripts
from sqlite3 import connect

def setup(self):
    self.cur = self.con.cursor()
    scripts = TableConstructorScripts()

    self.cur.execute(scripts.clients())
    self.cur.execute(scripts.tickets())

class Database:
    def __init__(self):
        self.con = connect('database.db')
        setup(self)

    def modo_teste(self):
        self.con = connect('testes.db')
        setup(self)

db = Database()