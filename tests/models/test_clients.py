import unittest
from datetime import date
from os import system
from models import Client
from connector import db
from tests.models.generator import Generate


class TesteCrudClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.current_date = str(date.today())
        cls.client = Client()
        db.modo_teste()
        generate = Generate(db)
        generate.client()

    @classmethod
    def tearDownClass(cls):
        system('rm testes.db')

    def test_create(self):
        self.client.create(
            tipo_de_cadastro='Pessoa Jurídica',
            nome='Jubileu',
            cep='12345678',
            logradouro='rua',
            numero='1',
            bairro='vila',
            cidade='vilarejo',
            uf='BH',
            situacao=1,
            cnpj='12345',
            categoria='pet shop'
        )

        dados = db.cur.execute(
            'SELECT * FROM clientes WHERE nome = "Jubileu"'
        ).fetchall()[0]

        self.assertEqual(dados, (
            2, 'Pessoa Jurídica', '12345', None, None, None, 'Jubileu', None,
            '12345678', 'rua', '1', 'vila', 'vilarejo', 'BH', None, 1,
            'pet shop', str(date.today()), None
        ))

    def test_read(self):
        self.assertEqual(self.client.read(1), {
            'id': 1,
            'tipo_de_cadastro': 'Pessoa Física',
            'cnpj': None,
            'cpf': '09876543210',
            'razao_social': None,
            'nome_fantasia': None,
            'nome': 'Laura',
            'email': None,
            'cep': '07192300',
            'logradouro': 'Avenida',
            'numero': '1100',
            'bairro': 'Bela Vista',
            'cidade': 'Guarulhos',
            'uf': 'SP',
            'complemento': None,
            'situacao': 'pendente',
            'categoria': None,
            'data_de_cadastro': self.current_date,
            'informacoes_adicionais': None
        })

    def test_update(self):
        self.client.update(1, **{
            'tipo_de_cadastro': 'Pessoa Física',
            'cnpj': None,
            'cpf': '12345678901',
            'nome': 'Raquel Almeida',
            'email': 'raquel@racoes.com',
            'cep': '09876543',
            'logradouro': 'Rua dos Cães',
            'numero': '89',
            'bairro': 'Ponte Grande',
            'cidade': 'Ribeirão Preto',
            'situacao': 'pago',
            'categoria': 'casa de ração'
        })

        client_data = db.cur.execute(
            'SELECT * FROM clientes WHERE id = ?', (1,)
        ).fetchall()[0]

        self.assertEqual(client_data, (
            1, 'Pessoa Física', None, '12345678901', None, None,
            'Raquel Almeida', 'raquel@racoes.com', '09876543', 'Rua dos Cães',
            '89', 'Ponte Grande', 'Ribeirão Preto', 'SP', None, 'pago',
            'casa de ração', self.current_date, None
        ))

    def test_delete(self):
        self.client.delete(2)
        client_data = db.cur.execute(
            'SELECT * FROM clientes WHERE id = ?', (2,)
        ).fetchall()

        self.assertEqual(client_data, [])

    # def test_read_all(self):
    #     self.assertEqual(self.report.read_all(), ({
    #         'id': 1,
    #         'tipo_de_cadastro': 'Pessoa Física',
    #         'cnpj': None,
    #         'cpf': '122345678901',
    #         'razao_social': None,
    #         'nome_fantasia': None,
    #         'nome': 'Raquel  Almeida',
    #         'email': 'raquel@racoes.com',
    #         'cep': '09876543',
    #         'logradouro': 'Rua dos Cães',
    #         'numero': '89',
    #         'bairro': 'Ponte Grande',
    #         'cidade': 'Ribeirão Preto',
    #         'uf': 'SP',
    #         'complemento': None,
    #         'situacao': 'pago',
    #         'categoria': 'case de ração',
    #         'data_de_cadastro': self.current_date,
    #         'informacoes_adicionais': None
    #     }))