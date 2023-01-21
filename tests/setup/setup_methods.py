from abc import ABCMeta
from connector import db
from datetime import date
from models import Client, Ticket
from os import system
from tests.models.generator import Generate


class Setup(metaclass=ABCMeta):
    @classmethod
    def setUpClass(cls):
        db.modo_teste()
        cls.current_date = str(date.today())
        cls.client = Client()
        cls.ticket = Ticket()
        generate = Generate(db)
        generate.client()
        generate.ticket()

    @classmethod
    def tearDownClass(cls):
        system('rm testes.db')
