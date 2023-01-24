from .widgets.menu import Menu
from datetime import date
import PySimpleGUI as sg


class Charge(Menu):
    def form(self):
        form = [
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

        table = [
            sg.Table(
                [['28/02/2023', 2000, '948234189014']],
                [
                    'Vencimento',
                    'valor',
                    'N. Boleto'
                ],
                auto_size_columns=False,
                def_col_width=15,
                justification='center',
                row_height=25,
                header_background_color='lightblue',
                row_colors=[(0, 'white'), (1, 'lightgrey')],
                expand_x=True
            )
        ]

        button_size = 15
        interface = [
            sg.Button('Excluir', key='-EXCLUIR_BOLETO-', size=button_size),
            sg.Push(),
            sg.Button('Editar', key='-EDITAR_BOLETO-', size=button_size),
            sg.Push(),
            sg.Button('Adicionar', key='-ADICIONAR_BOLETO-', size=button_size)
        ]

        return [
            [sg.Menu(self.menu_bar)],
            form,
            interface,
            table
        ]

    def report(self):
        table = [
            [sg.Table(
                [self.tickets],
                [
                    'Nome Fantasia',
                    'Nome',
                    'CNPJ',
                    'Data de Vencimento',
                    'valor',
                    'N. Boleto'
                ],
                auto_size_columns=False,
                def_col_width=15,
                justification='center',
                row_height=25,
                header_background_color='lightblue',
                row_colors=[(0, 'white'), (1, 'lightgrey')]
            )]
        ]

        button_size = 15
        interface = [
            [sg.Button(
                'Adicionar', key='-ADICIONAR_BOLETO-', size=button_size
            )],
            [sg.Button('Editar', key='-EDITAR_BOLETO-', size=button_size)],
            [sg.Button('Excluir', key='-EXCLUIR_BOLETO-', size=button_size)],
        ]

        return [
            [sg.Menu(self.menu_bar)],
            [sg.Column(table), sg.vtop(sg.Column(interface))]
        ]
