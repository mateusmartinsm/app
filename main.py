#! venv/bin/python

import PySimpleGUI as sg

import models
import views

sg.theme('DefaultNoMoreNagging')

def limpar_campos():
    for k in window.key_dict.keys():
        if type(k) == str:
            if 'INPUT' in k:
                window[k].update('')
            elif k[1] == '1':
                window[k].update(True)


charge_model = models.Ticket()
charge_view = views.Charge(charge_model.read_all())
client_model = models.Client()
client_view = views.Client(client_model.read_all())
dashboard_view = views.Dashboard()


window = sg.Window(
    'Gestor de Cobranças',
    layout=dashboard_view.get_design,
    element_padding=7,
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
                layout = dashboard_view.get_design
            case 'Novo cliente' | '-ADICIONAR_CLIENTE-':
                layout = client_view.get_form()
            case 'Nova cobrança':
                layout = charge_view.get_form()
            case 'Todos os clientes':
                client_view.clients = client_model.read_all()
                layout = client_view.get_report()
            case 'Relatório cobranças':
                charge_view.tickets = charge_model.read_all()
                layout = charge_view.get_report()
            case _:
                raise NameError('layout não definido')
        window.close()
        del window
        window = sg.Window(
            'Gestor de Cobranças',
            layout,
            element_padding=7,
        )
    elif event == '-LIMPAR-':
        limpar_campos()
    elif event == '-CADASTRAR-':
        client_model.create(
            'Pessoa Jurídica' if values['-1JURIDICA-'] else 'Pessoa Física',
            values['-INPUT_FANTASIA-'],
            values['-INPUT_NOME-'],
            values['-INPUT_BAIRRO-'],
            values['-INPUT_TELEFONE-']
        )
        sg.PopupOK(f'Cliente {values["-INPUT_NOME-"]} cadastrado com sucesso.')
        limpar_campos()
    elif event == '-EXCLUIR_CLIENTE-':
        key = '-TABELA_CLIENTES-'
        client_id = window[key].get()[values[key][0]][0]
        client_model.delete(client_id)
        clients_register = client_model.read_all()
        clients_register = [list(i) for i in clients_register.copy()]
        for register in clients_register:
            register.append('OK')
        window[key].update(values=clients_register)
