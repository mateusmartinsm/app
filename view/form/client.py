from view.widgets import Menu
from datetime import date
import PySimpleGUI as sg


class Client(Menu):
    """Inicialização da interface do formulário de registro de clientes"""
    def __init__(self):
        self.window_title = 'Novo cliente'
        self.abort_button_text = 'Limpar'
        self.abort_button_key = '-LIMPAR-'
        self.submit_button_text = 'Cadastrar'
        self.submit_button_key = '-CADASTRAR-'

    def layout(self) -> list[list[sg.Element]]:
        """Constroi layout único NÃO REUTILIZÁVEL da interface"""
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
            [sg.Text(self.window_title)],
            [sg.HorizontalSeparator()],
            [
                sg.Column(left_column),
                sg.VerticalSeparator(),
                sg.vtop(sg.Column(right_column))
            ],
            [
                sg.Push(),
                sg.Button(self.abort_button_text, key=self.abort_button_key),
                sg.Button(self.submit_button_text, key=self.submit_button_key)
            ]
        ]
