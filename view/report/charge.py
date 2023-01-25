from ..widgets.menu import Menu
import PySimpleGUI as sg


class Charge(Menu):
    """Inicialização da interface da tabela de registros de cobranças"""
    def __init__(self):
        self.tickets = None

    def layout(self) -> list[list[sg.Element]]:
        """Constroi layout único NÃO REUTILIZÁVEL da interface"""
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
