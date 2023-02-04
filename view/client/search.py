import PySimpleGUI as sg
from view.widgets import ClientTable, Menu


class Search(ClientTable, Menu):
    def layout(self) -> list[list]:
        button_size = 15
        interface = [
            [sg.Button(
                'Selecionar', key='-SELECT CLIENT-', size=button_size
            )]
        ]
        return [
            [sg.Menu(self.menu_bar)],
            [
                sg.Text('Buscar por'),
                sg.Combo(['Nome fantasia', 'Nome', 'CNPJ'],
                         key='-CLIENT FILTER-',
                         enable_events=True),
                sg.Input(key='-CLIENT SEARCH BAR-', enable_events=True),
                sg.Button('Buscar', key='-SEARCH CLIENT-')
            ],
            [sg.Column(self._table()), sg.vtop(sg.Column(interface))],
            [sg.Push(), sg.Button('Voltar',
                                  key='Nova cobrança',
                                  size=button_size)]
        ]
