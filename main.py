import PySimpleGUI as sg

import models
import view

sg.theme('DefaultNoMoreNagging')


def show_popup(keyword: str = None, msg: str = None) -> None:
    if msg is None:
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
        self.client_id = None
        self.client_model = models.Client()
        self.client_table = view.widgets.ClientTable()
        self.client_form = view.client.Form()
        self.client_report = view.client.Report()
        self.client_search = view.client.Search()

        self.charge_model = models.Ticket()
        self.charge_form = view.charge.Form()
        self.charge_report = view.charge.Report()

        self.dashboard = view.Dashboard()
        expired_tickets, pending_tickets, paid_tickets = \
            tuple([self.charge_model.count(i) for i in ['vencido',
                                                        'pendente',
                                                        'pago']])

        self.window = sg.Window('Gestor de Cobranças',
                                element_padding=7,
                                finalize=True,
                                layout=self.dashboard.layout(expired_tickets,
                                                             pending_tickets,
                                                             paid_tickets))

        self.dashboard.draw_figure(
            self.window['-CANVAS-'].TKCanvas,
            self.dashboard.create_plot()
        )

        self.values = {}

    @staticmethod
    def _init_window(layout: list[list[sg.Element]]) -> sg.Window:
        return sg.Window('Gestor de Cobranças',
                         layout,
                         element_padding=7,
                         finalize=True)

    def _alter_form_state(self, state) -> None:
        if state == 'enable':
            self.window['-TITULO-'].update('Editar rergistro do cliente')
            self.window['Todos os clientes'].update(text='Cancelar')
            self.window['-HABILITAR_EDICAO-'].update(visible=False)
            self.window['-SALVAR_CLIENTE-'].update(visible=True)
        for k in self.window.key_dict.keys():
            if type(k) == str:
                if 'INPUT' in k:
                    match state:
                        case 'clean': self.window[k].update('')
                        case 'enable': self.window[k].update(disabled=False)
                elif state == 'clean' and k[1] == '1':
                    self.window[k].update(True)
                elif state == 'enable' and k[1].isnumeric():
                    self.window[k].update(disabled=False)

    def _open_client_data_form(self, mode: str) -> None:
        try:
            key = '-CLIENT TABLE-'
            self.client_id = int(
                self.window[key].get()[self.values[key][0]][0]
            )
            self.window.close()
            self.window = self._init_window(self.client_form.layout(mode))
            input_keys = ['FANTASIA', 'NOME', 'TELEFONE', 'BAIRRO']
            input_fields = [
                'nome_fantasia',
                'nome',
                'email',
                'cidade'
            ]
            for i, field in enumerate(input_fields):
                self.window[f'-INPUT_{input_keys[i]}-'].update(
                    self.client_model.read(self.client_id)[field]
                )
        except IndexError:
            show_popup(mode)

    def loop(self):
        while True:
            event, self.values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            if event in [
                'Dashboard',
                'Novo cliente',
                'Nova cobrança',
                'Todos os clientes',
                'Relatório cobranças',
                '-COBRANÇAS VENCIDAS-',
                '-COBRANÇAS PAGAS-',
                '-CLIENT SEARCH PAGE-'
            ]:
                match event:
                    case 'Dashboard':
                        expired_tickets, pending_tickets, paid_tickets = \
                            tuple([self.charge_model.count(i) for i in [
                                'vencido',
                                'pendente',
                                'pago'
                            ]])
                        layout = self.dashboard.layout(expired_tickets,
                                                       pending_tickets,
                                                       paid_tickets)
                    case 'Novo cliente':
                        layout = self.client_form.layout()
                    case 'Nova cobrança':
                        try:
                            layout = self.charge_form.layout()
                        except TypeError:
                            show_popup(msg='ERRO: Nenhum cliente cadastrado\n'
                                           'Cadastre o cliente antes de '
                                           'registrar o boleto.\n')
                            continue
                    case 'Todos os clientes':
                        self.client_report.clients_register = \
                            self.client_model.read_all()
                        layout = self.client_report.layout()
                    case 'Relatório cobranças':
                        layout = self.charge_report.layout(
                            self.charge_model.read_all('pendente')
                        )
                    case '-COBRANÇAS VENCIDAS-':
                        layout = self.charge_report.layout(
                            self.charge_model.read_all('vencido'),
                            'vencido'
                        )
                    case '-COBRANÇAS PAGAS-':
                        layout = self.charge_report.layout(
                            self.charge_model.read_all('pago'),
                            'pago'
                        )
                    case '-CLIENT SEARCH PAGE-':
                        self.client_search.clients_register = \
                            self.client_model.read_all()
                        layout = self.client_search.layout()
                    case _:
                        raise NameError('layout não definido')
                self.window.close()
                self.window = self._init_window(layout)
                if event == 'Dashboard':
                    self.dashboard.draw_figure(
                        self.window['-CANVAS-'].TKCanvas,
                        self.dashboard.create_plot()
                    )
            elif event in ['-VISUALIZAR_CLIENTE-', '-EDITAR_CLIENTE-']:
                mode = {
                    '-VISUALIZAR_CLIENTE-': 'visualizar',
                    '-EDITAR_CLIENTE-': 'editar'
                }
                self._open_client_data_form(mode[event])
            elif event == '-LIMPAR-':
                self._alter_form_state('clean')
            elif event == '-CADASTRAR-':
                if self.values['-1JURIDICA-']:
                    tipo_de_cliente = 'Pessoa Jurídica'
                else:
                    tipo_de_cliente = 'Pessoa Física'
                self.client_model.create(tipo_de_cliente,
                                         self.values['-INPUT_FANTASIA-'],
                                         self.values['-INPUT_NOME-'],
                                         self.values['-INPUT_BAIRRO-'],
                                         self.values['-INPUT_TELEFONE-'])
                self.client_report.clients = self.client_model.read_all()
                sg.PopupOK(f'Cliente {self.values["-INPUT_NOME-"]} '
                           'cadastrado com sucesso.')

                layout = self.client_report.layout()
                self.window.close()
                self.window = self._init_window(layout)
            elif event == '-SELECT CLIENT-':
                key = '-CLIENT TABLE-'
                client_id = int(
                    self.window[key].get()[self.values[key][0]][0]
                )
                ticket_list = self.charge_model.read(client_id, list)
                layout = self.charge_form.layout(ticket_list)
                self.window.close()
                self.window = self._init_window(layout)
            elif event == '-HABILITAR_EDICAO-':
                self._alter_form_state('enable')
            elif event == '-SALVAR_CLIENTE-':
                self.client_model.update(self.client_id, **{
                    'nome_fantasia': self.values['-INPUT_FANTASIA-'],
                    'nome': self.values['-INPUT_NOME-'],
                    'telefone': self.values['-INPUT_TELEFONE-'],
                    'bairro': self.values['-INPUT_BAIRRO-']
                })
                sg.Popup('Registro atualizado com sucesso.\n\n')
                self.window.close()
                self.window = self._init_window(self.client_report.layout())
            elif event == '-EXCLUIR_CLIENTE-':
                try:
                    key = '-TABELA_CLIENTES-'
                    self.client_id = \
                        int(self.window[key].get()[self.values[key][0]][0])
                    self.client_model.delete(self.client_id)
                    clients_register = self.client_model.read_all()
                    clients_register = \
                        [list(i) for i in clients_register.copy()]
                    for register in clients_register:
                        register.append('OK')
                    self.window[key].update(values=clients_register)
                except IndexError:
                    show_popup('deletar')
            elif event == '-COMBO SITUATION-':
                situation = self.values['-COMBO SITUATION-']
                try:
                    new_table_values = self.charge_model.read_all(situation)
                    self.window['-TICKET_TABLE-'].update(
                        new_table_values,
                        row_colors=[  # row_colors é resetado no update
                            (i, 'white' if i % 2 == 0 else 'lightgray')
                            for i in range(len(new_table_values))
                        ]
                    )
                except IndexError:
                    show_popup(msg=f'Sem boletos {situation}s')
            else:
                sg.Popup(NameError(f'evento {event} não encontrado\n\n'))


root = MainFrame()
root.loop()
