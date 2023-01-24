import PySimpleGUI as sg

import models
import views

sg.theme('DefaultNoMoreNagging')


def clean_form():
    for k in window.key_dict.keys():
        if type(k) == str:
            if 'INPUT' in k:
                window[k].update('')
            elif k[1] == '1':
                window[k].update(True)


client_model = models.Client()
client_view = views.Client()
client_view.clients = client_model.read_all()
charge_model = models.Ticket()
charge_view = views.Charge()
charge_view.tickets = charge_model.read_all()
dashboard_view = views.Dashboard()

window = sg.Window(
    'Gestor de Cobranças',
    element_padding=7,
    layout=dashboard_view.layout(),
    finalize=True
)

dashboard_view.draw_figure(
    window['-CANVAS-'].TKCanvas,
    dashboard_view.create_plot()
)

while True:
    event, values = window.read()
    # breakpoint()

    if event == sg.WIN_CLOSED:
        break
    if event in [
        'Dashboard',
        'Novo cliente',
        'Nova cobrança',
        'Todos os clientes',
        'Relatório cobranças',
        '-ADICIONAR_CLIENTE-'
    ]:
        match event:
            case 'Dashboard':
                layout = dashboard_view.layout()
            case 'Novo cliente' | '-ADICIONAR_CLIENTE-':
                layout = client_view.form()
            case 'Nova cobrança':
                layout = charge_view.form()
            case 'Todos os clientes':
                layout = client_view.report()
            case 'Relatório cobranças':
                charge_view.tickets = charge_model.read_all()
                layout = charge_view.report()
            case _:
                raise NameError('layout não definido')
        window.close()
        del window
        window = sg.Window(
            'Gestor de Cobranças',
            layout,
            element_padding=7,
            finalize=True
        )
        if event == 'Dashboard':
            dashboard_view.draw_figure(
                window['-CANVAS-'].TKCanvas,
                dashboard_view.create_plot()
            )
    elif event == '-LIMPAR-':
        clean_form()
    elif event == '-CADASTRAR-':
        client_model.create(
            'Pessoa Jurídica' if values['-1JURIDICA-'] else 'Pessoa Física',
            values['-INPUT_FANTASIA-'],
            values['-INPUT_NOME-'],
            values['-INPUT_BAIRRO-'],
            values['-INPUT_TELEFONE-']
        )
        client_view.clients = client_model.read_all()
        sg.PopupOK(f'Cliente {values["-INPUT_NOME-"]} cadastrado com sucesso.')
        clean_form()
    elif event == '-EDITAR_CLIENTE-':
        key = '-TABELA_CLIENTES-'
        client_id = window[key].get()[values[key][0]][0]
    elif event == '-EXCLUIR_CLIENTE-':
        try:
            key = '-TABELA_CLIENTES-'
            client_id = int(window[key].get()[values[key][0]][0])
            client_model.delete(client_id)
            clients_register = client_model.read_all()
            clients_register = [list(i) for i in clients_register.copy()]
            for register in clients_register:
                register.append('OK')
            window[key].update(values=clients_register)
        except IndexError:
            msg = 'ERRO: Nenhum registro selecionado.\n' \
                  'Por favor, selecione o registro de um cliente ' \
                  'antes de deletá-lo'
            sg.Popup(
                msg,
                title='Mensagem de erro',
                text_color='red',
                line_width=len(msg),
                keep_on_top=True,
                any_key_closes=True
            )
