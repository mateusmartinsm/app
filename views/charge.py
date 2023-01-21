from .widgets.menu import Menu
from datetime import date
import PySimpleGUI as sg

class Charge(Menu):
    def __init__(self):
        self.form = [
            [sg.Menu(self.menu_bar)],
            [sg.Column([
                [sg.Text('Cliente')],
                [sg.Text('Valor')],
                [sg.Push()],
                [sg.Text('Data de emissão')],
                [sg.Push()],
                [sg.Text('Data de vencimento')]
            ]), sg.Column([
                [sg.DropDown(['Topam', 'PC', 'Rogério'])],
                [sg.Input('0')],
                [
                    sg.Input(str(date.today().__format__('%d/%m/%Y'))),
                    sg.CalendarButton('Calendário', format='%d/%m/%Y')
                ],
                [
                    sg.Input(),
                    sg.CalendarButton('Calendário', format='%d/%m/%Y')
                ],
            ])]
        ]

    def report(self, tickets):
        return [
            [sg.Menu(self.menu_bar)],
            [sg.Table(
                [tickets],
                [
                    'Nome Fantasia',
                    'Nome',
                    'CNPJ',
                    'Data de Vencimento',
                    'valor',
                    'N. Boleto'
                ],
                auto_size_columns=False,
                def_col_width=20,
                justification='center',
                row_height=25,
                header_background_color='lightblue',
                row_colors=[(0, 'white'), (1, 'lightgrey')]
            )]
        ]