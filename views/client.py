from .widgets.menu import Menu
from datetime import date
import PySimpleGUI as sg


class Client(Menu):
    '''Layouts de todas as janelas relacionadas ao cliente'''
    def form(self):
        title_color = 'green'
        left_column = [
            [sg.Text('Geral', text_color=title_color)],
            [sg.Text('Tipo de Cadastro'), sg.Column([
                [sg.Radio('Pessoa Jurídica', 'type', True, key='-1JURIDICA-')],
                [sg.Radio('Pessoa Física', 'type', key='-2FISICA-')],
            ])],
            [sg.vbottom(sg.Column([
                [sg.Text('CNPJ')],
                [sg.Text('Razão Social')],
                [sg.Text('Nome Fantasia')]
            ])), sg.Column([
                [sg.Input(key='-INPUT_CNPJ-')],
                [sg.Input(key='-INPUT_RAZAO-')],
                [sg.Input(key='-INPUT_FANTASIA-')]
            ])],
            [sg.HorizontalSeparator()],
            [sg.Text('Detalhes', text_color=title_color)],
            [sg.vtop(sg.Text('Situação')), sg.Column([
                [sg.Radio('Ativo', 'situation', True, key='-1ATIVO-')],
                [sg.Radio('Inativo', 'situation', key='-2INATIVO-')]
            ])],
            [sg.vtop(sg.Text('Categoria')), sg.Column([
                [sg.Radio('Pet  Shop', 'category', True, key='-1PET_SHOP-')],
                [sg.Radio('Revendedor', 'category', key='-2REVENDEDOR-')]
            ])],
            [
                sg.Text('Data de Cadastro'),
                sg.Input(
                    str(date.today().__format__('%d/%m/%Y')),
                    key='-INPUT_CADASTRO-'
                ),
                sg.CalendarButton('Calendario', format='%d/%m/%Y')
            ],
        ]

        right_column = [
            [sg.Text('Endereco', text_color=title_color)],
            [sg.Text('Nome'), sg.Push(), sg.Input(key='-INPUT_NOME-')],
            [sg.Text('Telefone'), sg.Push(), sg.Input(key='-INPUT_TELEFONE-')],
            [sg.Text('Email'), sg.Push(), sg.Input(key='-INPUT_EMAIL-')],
            [sg.Text('CEP'), sg.Push(), sg.Input(key='-INPUT_CEP-')],
            [
                sg.Text('Logradouro'),
                sg.Push(),
                sg.Input(key='-INPUT_LOGRADOURO-')
            ],
            [sg.Text('Número'), sg.Push(), sg.Input(key='-INPUT_NUMERO-')],
            [sg.Text('Bairro'), sg.Push(), sg.Input(key='-INPUT_BAIRRO-')],
            [sg.Text('Cidade'), sg.Push(), sg.Input(key='-INPUT_CIDADE-')],
            [sg.Text('Estado'), sg.Push(), sg.Input(key='-INPUT_UF-')],
            [sg.Push()],
        ]

        return [
            [sg.Menu(self.menu_bar)],
            [sg.Text('Novo Cliente')],
            [sg.HorizontalSeparator()],
            [
                sg.Column(left_column),
                sg.VerticalSeparator(),
                sg.vtop(sg.Column(right_column))
            ],
            [
                sg.Push(),
                sg.Button('Limpar', key='-LIMPAR-'),
                sg.Button('Cadastrar', key='-CADASTRAR-')
            ]
        ]

    def report(self):
        column_visibility = [False] + [True] * 5
        self.clients = [list(i) for i in self.clients.copy()]
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
