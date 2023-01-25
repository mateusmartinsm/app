from abc import ABCMeta


class Menu(metaclass=ABCMeta):
    menu_bar = [
        ['Visualizar', ['Dashboard']],
        ['Detalhes do cliente', ['Novo cliente', 'Todos os clientes']],
        ['Cobranças', ['Nova cobrança', 'Relatório cobranças']],
    ]