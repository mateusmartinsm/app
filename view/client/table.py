from view.widgets import Menu
import PySimpleGUI as sg


class Table(Menu):
    """Inicialização da interface da tabela de registros dos clientes"""

    def layout(self,
               clients_register: list[tuple[any]]
               ) -> list[list[sg.Element]]:
        """Constroi layout único NÃO REUTILIZÁVEL da interface"""
        clients_register = [list(i) for i in clients_register.copy()]
        column_visibility = [False] + [True] * 5
        colors = ['white', 'lightblue']
        for c in clients_register:
            c.append('OK')
        table = [
            [sg.Table(
                clients_register,
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
                row_colors=[
                    (i, 'white' if i % 2 == 0 else 'lightgray')
                    for i in range(len(clients_register))
                ]
            )]
        ]

        button_size = 15
        interface = [
            [sg.Button(
                'Adicionar', key='-ADICIONAR_CLIENTE-', size=button_size
            )],
            [sg.Button(
                'Visualizar', key='-VISUALIZAR_CLIENTE-', size=button_size
            )],
            [sg.Button('Editar', key='-EDITAR_CLIENTE-', size=button_size)],
            [sg.Button('Excluir', key='-EXCLUIR_CLIENTE-', size=button_size)],
        ]

        return [
            [sg.Menu(self.menu_bar)],
            [sg.Column(table), sg.vtop(sg.Column(interface))]
        ]
