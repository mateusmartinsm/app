from .table import Table


class ClientTable:
    def __init__(self):
        self.clients_register = []
        self.column_visibility = []

    def table(self):
        table = Table()
        return table.shape(self.clients_register,
                           [
                               'id',
                               'Nome Fantasia',
                               'Nome',
                               'Bairro',
                               'Telefone',
                               'Pagamentos'
                           ],
                           '-CLIENT_TABLE-')
