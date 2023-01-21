from models.ticket import Ticket
from connector import db
from datetime import date, timedelta
from tests.models.generator import Generate
from os import system
import unittest

class TestTicket(unittest.TestCase):
    def setUp(self):
        db.modo_teste()
        self.current_date = str(date.today())
        self.due_date = str(date.today() + timedelta(days=15))
        self.ticket = Ticket()
        self.generate = Generate(db)
        self.generate.client()
        self.generate.ticket()

    def tearDown(self):
        system('rm testes.db')

    def test_create(self):
        due_date = str(date.today() + timedelta(days=15))
        self.ticket.create(
            id_cliente=2,
            numero='123420987123234',
            valor=1500,
            data_de_emissao=str(date.today()),
            data_de_vencimento=due_date,
            situacao='pendente'
        )

        client = db.cur.execute(
            'SELECT * FROM boletos WHERE id_boleto = 2',
        ).fetchall()[0]

        self.assertEqual(client, (
            2, 2, '123420987123234', 1500.0, str(date.today()),
            due_date, 'pendente'
        ))

    def test_read(self):
        self.assertEqual(self.ticket.read(1), {
            'id_cliente': 1,
            'id_boleto': 1,
            'numero': '098712340987',
            'valor': 2100.50,
            'data_de_emissao': self.current_date,
            'data_de_vencimento': self.due_date,
            'situacao': 'pendente'
        })

    def test_update(self):
        self.ticket.update(1, valor=1600)
        ticket_data = db.cur.execute(
            'SELECT * FROM boletos WHERE id_boleto = 1'
        ).fetchall()[0]

        self.assertEqual(ticket_data, (
            1, 1, '098712340987', 1600, self.current_date, self.due_date,
            'pendente'
        ))

    def test_4read_all(self):
        self.assertEqual(self.ticket.read_all(), [
            None, 'Laura', None, '2023-02-04', 2100.5, '098712340987'
        ])

    def test_delete(self):
        self.ticket.delete(1)
        empty_data_list = db.cur.execute(
            'SELECT * FROM boletos WHERE id_boleto = 1',
        ).fetchall()
        self.assertEqual(empty_data_list, [])
