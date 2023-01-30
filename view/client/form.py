import PySimpleGUI as sg
from datetime import date

from view.widgets import Menu


class Form(Menu):
    """Inicialização da interface do formulário de registro de clientes"""
    def __init__(self):
        self.window_title = 'Novo cliente'
        self.abort_button_text = 'Limpar'
        self.abort_button_key = '-LIMPAR-'
        self.submit_button_text = 'Cadastrar'
        self.submit_button_key = '-CADASTRAR-'
        self.mode = ''

    def _set_buttons_attributes(self):
        options = {'editar': ('Editar registro do cliente',
                              'Cancelar',
                              'Salvar',
                              '-SALVAR_CLIENTE-'),
                   'visualizar': ('Visualizar dados do cliente',
                                  'Voltar',
                                  'Habilitar edição',
                                  '-HABILITAR_EDICAO-')}
        (self.window_title,
         self.abort_button_text,
         self.submit_button_text,
         self.submit_button_key) = options[self.mode]
        self.abort_button_key = 'Todos os clientes'

    def layout(self, mode='novo') -> list[list[sg.Element]]:
        """Constroi layout único NÃO REUTILIZÁVEL da interface"""
        self.mode = mode
        if self.mode != 'novo':
            self._set_buttons_attributes()
        disabled = True if self.mode == 'visualizar' else False
        title_color = 'green'
        left_column = [
            [sg.Text('Geral', text_color=title_color)],
            [sg.Text('Tipo de Cadastro'), sg.Column([
                [sg.Radio('Pessoa Jurídica',
                          'type',
                          True,
                          key='-1JURIDICA-',
                          disabled=disabled)],
                [sg.Radio('Pessoa Física',
                          'type',
                          key='-2FISICA-',
                          disabled=disabled)],
            ])],
            [sg.vbottom(sg.Column([
                [sg.Text('CNPJ')],
                [sg.Text('Razão Social')],
                [sg.Text('Nome Fantasia')]
            ])), sg.Column([
                [sg.Input(key='-INPUT_CNPJ-', disabled=disabled)],
                [sg.Input(key='-INPUT_RAZAO-', disabled=disabled)],
                [sg.Input(key='-INPUT_FANTASIA-', disabled=disabled)]
            ])],
            [sg.HorizontalSeparator()],
            [sg.Text('Detalhes', text_color=title_color)],
            [sg.vtop(sg.Text('Situação')), sg.Column([
                [sg.Radio('Ativo',
                          'situation',
                          True,
                          key='-1ATIVO-',
                          disabled=disabled)],
                [sg.Radio('Inativo',
                          'situation',
                          key='-2INATIVO-',
                          disabled=disabled)]
            ])],
            [sg.vtop(sg.Text('Categoria')), sg.Column([
                [sg.Radio('Pet  Shop',
                          'category',
                          True,
                          key='-1PET_SHOP-',
                          disabled=disabled)],
                [sg.Radio('Revendedor',
                          'category',
                          key='-2REVENDEDOR-',
                          disabled=disabled)]
            ])],
            [
                sg.Text('Data de Cadastro'),
                sg.Input(
                    str(date.today().__format__('%d/%m/%Y')),
                    key='-INPUT_CADASTRO-',
                    disabled=disabled
                ),
                sg.CalendarButton('Calendario', format='%d/%m/%Y')
            ],
        ]

        right_column = [
            [sg.Text('Endereco', text_color=title_color)],
            [sg.Text('Nome'), sg.Push(), sg.Input(key='-INPUT_NOME-',
                                                  disabled=disabled)],
            [sg.Text('Telefone'), sg.Push(), sg.Input(key='-INPUT_TELEFONE-',
                                                      disabled=disabled)],
            [sg.Text('Email'), sg.Push(), sg.Input(key='-INPUT_EMAIL-',
                                                   disabled=disabled)],
            [sg.Text('CEP'), sg.Push(), sg.Input(key='-INPUT_CEP-',
                                                 disabled=disabled)],
            [
                sg.Text('Logradouro'),
                sg.Push(),
                sg.Input(key='-INPUT_LOGRADOURO-', disabled=disabled)
            ],
            [sg.Text('Número'), sg.Push(), sg.Input(key='-INPUT_NUMERO-',
                                                    disabled=disabled)],
            [sg.Text('Bairro'), sg.Push(), sg.Input(key='-INPUT_BAIRRO-',
                                                    disabled=disabled)],
            [sg.Text('Cidade'), sg.Push(), sg.Input(key='-INPUT_CIDADE-',
                                                    disabled=disabled)],
            [sg.Text('Estado'), sg.Push(), sg.Input(key='-INPUT_UF-',
                                                    disabled=disabled)],
            [sg.Push()],
        ]

        return [
            [sg.Menu(self.menu_bar)],
            [sg.Text(self.window_title, key='-TITULO-')],
            [sg.HorizontalSeparator()],
            [
                sg.Column(left_column),
                sg.VerticalSeparator(),
                sg.vtop(sg.Column(right_column))
            ],
            [
                sg.Push(),
                sg.Button(self.abort_button_text, key='Todos os clientes'),
                sg.Button(self.submit_button_text, key=self.submit_button_key),
                sg.Button('Salvar', key='-SALVAR_CLIENTE-', visible=False)
            ]
        ]
