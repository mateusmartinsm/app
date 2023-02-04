from view import widgets
import PySimpleGUI as sg


class Report(widgets.Menu):
    """Inicialização da interface da tabela de registros de cobranças"""
    def __init__(self):
        self.table = widgets.Table()
        self.tickets = []

    def layout(self,
               tickets,
               default_combo_value: str = 'pendente'
               ) -> list[list[sg.Element]]:
        """Constroi layout único NÃO REUTILIZÁVEL da interface"""
        table = self.table.shape(
            tickets,
            [
                'id'
                'Nome Fantasia',
                'Nome',
                'CNPJ',
                'Data de Vencimento',
                'valor',
                'N. Boleto'
            ],
            key='-TICKET_TABLE-'
        )

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
            [sg.Column([
                [sg.Push(), sg.Combo(['pendente', 'pago', 'vencido'],
                                     default_value=default_combo_value,
                                     enable_events=True,
                                     key='-COMBO SITUATION-')],
                [table]
            ]), sg.vtop(sg.Column(interface, pad=((0, 0), (38, 0))))]
        ]
