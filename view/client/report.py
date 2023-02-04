from view.widgets import ClientTable, Menu
import PySimpleGUI as sg


class Report(ClientTable, Menu):
    """Inicialização da interface da tabela de registros dos clientes"""
    def layout(self) -> list[list[sg.Element]]:
        """Constroi layout único NÃO REUTILIZÁVEL da interface"""
        button_size = 15
        interface = [
            [sg.Button(
                'Adicionar', key='Novo cliente', size=button_size
            )],
            [sg.Button(
                'Visualizar', key='-VISUALIZAR_CLIENTE-', size=button_size
            )],
            [sg.Button('Editar', key='-EDITAR_CLIENTE-', size=button_size)],
            [sg.Button('Excluir', key='-EXCLUIR_CLIENTE-', size=button_size)],
        ]

        return [
            [sg.Menu(self.menu_bar)],
            [sg.Column([[self.table()]]), sg.vtop(sg.Column(interface))]
        ]
