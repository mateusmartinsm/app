import PySimpleGUI as sg


class ClientTable:
    def __init__(self):
        self.clients_register = []
        self.column_visibility = []

    def table(self):
        self.clients_register = [list(i) for i in self.clients_register.copy()]
        self.column_visibility = [False] + [True] * 5
        for c in self.clients_register:
            c.append('OK')
        return [
            [sg.Table(
                self.clients_register,
                [
                    'id',
                    'Nome Fantasia',
                    'Nome',
                    'Bairro',
                    'Telefone',
                    'Pagamentos'
                ],
                self.column_visibility,
                key='-CLIENT TABLE-',
                auto_size_columns=False,
                def_col_width=20,
                justification='center',
                row_height=25,
                header_background_color='lightblue',
                row_colors=[
                    (i, 'white' if i % 2 == 0 else 'lightgray')
                    for i in range(len(self.clients_register))
                ]
            )]
        ]
