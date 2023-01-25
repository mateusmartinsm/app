from ..widgets import Menu
import PySimpleGUI as sg


class Client(Menu):
    """Inicialização da interface da tabela de registros dos clientes"""
    def __init__(self):
        self.clients = None

    def layout(self) -> list[list[sg.Element]]:
        """Constroi layout único NÃO REUTILIZÁVEL da interface"""
        self.clients = [list(i) for i in self.clients.copy()]
        column_visibility = [False] + [True] * 5
        for c in self.clients:
            c.append('OK')
        table = [
            [sg.Table(
                self.clients,
                [
                    'id',
                    'Nome Fantasia',
                    'Nome',
                    'Bairro',
                    'Telefone',
                    'Pagamentos'
                ],
                column_visibility,
                key='-TABELA_CLIENTES-',
                auto_size_columns=False,
                def_col_width=20,
                justification='center',
                row_height=25,
                header_background_color='lightblue',
                row_colors=[(0, 'white'), (1, 'lightgrey')]
            )]
        ]

        button_size = 15
        interface = [
            [sg.Button(
                'Adicionar', key='-ADICIONAR_CLIENTE-', size=button_size
            )],
            [sg.Button('Editar', key='-EDITAR_CLIENTE-', size=button_size)],
            [sg.Button('Excluir', key='-EXCLUIR_CLIENTE-', size=button_size)],
        ]

        return [
            [sg.Menu(self.menu_bar)],
            [sg.Column(table), sg.vtop(sg.Column(interface))]
        ]
