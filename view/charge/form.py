from view.widgets.menu import Menu
from datetime import date
import PySimpleGUI as sg


class Form(Menu):
    """Inicialização da interface do formulário de registro de cobranças"""
    def layout(self, ticket_list: list = []) -> list[list[sg.Element]]:
        """Constroi layout único NÃO REUTILIZÁVEL da interface"""
        form = [
            [sg.Column([
                [sg.Text('Cliente')],
                [sg.Text('Valor')],
                [sg.Push()],
                [sg.Text('Data de emissão')],
                [sg.Push()],
                [sg.Text('Data de vencimento')]
            ]), sg.Column([
                [
                    sg.Input(),
                    sg.Button('Buscar', key='-CLIENT SEARCH PAGE-')
                ],
                [sg.Input('0', key='-VALOR-')],
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

        button_size = 15
        interface = [
            sg.Button('Excluir', key='-EXCLUIR_BOLETO-', size=button_size),
            sg.Push(),
            sg.Button('Editar', key='-EDITAR_BOLETO-', size=button_size),
            sg.Push(),
            sg.Button('Adicionar', key='-ADICIONAR_BOLETO-', size=button_size)
        ]

        table = [
            sg.Table(
                ticket_list,
                [
                    'Vencimento',
                    'valor',
                    'N. Boleto'
                ],
                key='-TABELA_BOLETOS-',
                auto_size_columns=False,
                def_col_width=15,
                justification='center',
                row_height=25,
                header_background_color='lightblue',
                row_colors=[(0, 'white'), (1, 'lightgrey')],
                expand_x=True
            )
        ]

        return [
            [sg.Menu(self.menu_bar)],
            [sg.Text('Novo boleto', text_color='green')],
            form,
            interface,
            table
        ]
