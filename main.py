import PySimpleGUI as sg

import models
import view

sg.theme('DefaultNoMoreNagging')


def init_window(self):
    return sg.Window(
        'Gestor de Cobranças',
        self.layout,
        element_padding=7,
        finalize=True
    )


def clean_form(self):
    for k in self.window.key_dict.keys():
        if type(k) == str:
            if 'INPUT' in k:
                self.window[k].update('')
            elif k[1] == '1':
                self.window[k].update(True)


def show_popup(keyword):
    msg = 'ERRO: Nenhum registro selecionado.\n' \
          f'Por favor, selecione o registro que deseja {keyword}\n'
    sg.Popup(
        msg,
        title='Mensagem de erro',
        text_color='red',
        line_width=len(msg),
        keep_on_top=True,
        any_key_closes=True
    )


class MainFrame:
    def __init__(self):
        self.client_model = models.Client()
        self.client_form = view.form.Client()
        self.client_report = view.report.Client()
        self.client_report.clients = self.client_model.read_all()

        self.charge_model = models.Ticket()
        self.charge_form = view.form.Charge()
        self.charge_report = view.report.Charge()
        self.charge_report.tickets = self.charge_model.read_all()

        self.dashboard = view.Dashboard()
        self.layout = self.dashboard.layout()

        self.window = sg.Window(
            'Gestor de Cobranças',
            element_padding=7,
            layout=self.layout,
            finalize=True
        )

        self.event = None
        self.values = None

        self.dashboard.draw_figure(
            self.window['-CANVAS-'].TKCanvas,
            self.dashboard.create_plot()
        )

    # def open_page(self):
    #

    def loop(self):
        while True:
            self.event, self.values = self.window.read()
            if self.event == sg.WIN_CLOSED:
                break
            if self.event in [
                'Dashboard',
                'Novo cliente',
                'Nova cobrança',
                'Todos os clientes',
                'Relatório cobranças',
                '-ADICIONAR_CLIENTE-',
                '-CANCELAR-'
            ]:
                match self.event:
                    case 'Dashboard':
                        self.layout = self.dashboard.layout()
                    case 'Novo cliente' | '-ADICIONAR_CLIENTE-':
                        self.layout = self.client_form.layout()
                    case 'Nova cobrança':
                        self.layout = self.charge_form.layout()
                    case 'Todos os clientes' | '-CANCELAR-':
                        self.client_report.clients = \
                            self.client_model.read_all()
                        self.layout = self.client_report.layout()
                    case 'Relatório cobranças':
                        self.charge_report.tickets = self.charge_model.read_all()
                        self.layout = self.charge_report.layout()
                    case _:
                        raise NameError('layout não definido')
                self.window.close()
                self.window = init_window(self)
                if self.event == 'Dashboard':
                    self.dashboard.draw_figure(
                        self.window['-CANVAS-'].TKCanvas,
                        self.dashboard.create_plot()
                    )
            elif self.event == '-LIMPAR-':
                clean_form(self)
            elif self.event == '-CADASTRAR-':
                if self.values['-1JURIDICA-']:
                    tipo_de_cliente = 'Pessoa Jurídica'
                else:
                    tipo_de_cliente = 'Pessoa Física'
                self.client_model.create(
                    tipo_de_cliente,
                    self.values['-INPUT_FANTASIA-'],
                    self.values['-INPUT_NOME-'],
                    self.values['-INPUT_BAIRRO-'],
                    self.values['-INPUT_TELEFONE-']
                )
                self.client_report.clients = self.client_model.read_all()
                sg.PopupOK(
                    f'Cliente {self.values["-INPUT_NOME-"]} '
                    'cadastrado com sucesso.'
                )
                clean_form(self)
            elif self.event == '-EDITAR_CLIENTE-':
                try:
                    key = '-TABELA_CLIENTES-'
                    client_id = int(self.window[key].get()[self.values[key][0]][0])
                    self.client_form.window_title = 'Editar registro do '\
                                                    'cliente'
                    self.client_form.abort_button_text = 'Cancelar'
                    self.client_form.abort_button_key = '-CANCELAR-'
                    self.client_form.submit_button_text = 'Salvar'
                    self.client_form.submit_button_key = '-SALVAR-'
                    self.layout = self.client_form.layout()
                    self.window.close()
                    self.window = init_window(self)
                    input_keys = ['FANTASIA', 'NOME', 'TELEFONE', 'BAIRRO']
                    input_fields = [
                        'nome_fantasia',
                        'nome',
                        'email',
                        'cidade'
                    ]
                    for i, field in enumerate(input_fields):
                        self.window[f'-INPUT_{input_keys[i]}-'].update(
                            self.client_model.read(client_id)[field]
                        )
                except IndexError:
                    show_popup('editar')
            elif self.event == '-EXCLUIR_CLIENTE-':
                try:
                    key = '-TABELA_CLIENTES-'
                    client_id = int(
                        self.window[key].get()[self.values[key][0]][0]
                    )
                    self.client_model.delete(client_id)
                    clients_register = self.client_model.read_all()
                    clients_register = [
                        list(i) for i in clients_register.copy()
                    ]
                    for register in clients_register:
                        register.append('OK')
                    self.window[key].update(values=clients_register)
                except IndexError:
                    show_popup('deletar')


root = MainFrame()
root.loop()
