#! venv/bin/python

import PySimpleGUI as sg

import models
from views import Charge, Client, Dashboard


def limpar_campos():
    for key in window.key_dict.keys():
        if type(key) == str:
            if 'INPUT' in key:
                window[key].update('')
            elif key[1] == '1':
                window[key].update(True)


client = models.Client()
ticket = models.Ticket()

sg.theme('DefaultNoMoreNagging')

window = sg.Window(
    'Gestor de Cobranças', layout=Client().form, element_padding=7
)

while True:
    event, values = window.read()
    # breakpoint()

    if event == sg.WIN_CLOSED:
        break
    if event in [
        'Dashboard',
        'Novo cliente',
        'Novo boleto',
        'Todos os clientes',
        'Relatório cobranças'
    ]:
        match event:
            case 'Dashboard':
                layout = Dashboard().design
            case 'Novo cliente':
                layout = Client().form
            case 'Novo boleto':
                layout = Charge().form
            case 'Todos os clientes':
                layout = Client().report(client.read_all())
            case 'Relatório cobranças':
                layout = Charge().report(ticket.read_all())
            case _:
                raise NameError('layout não definido')
        window.close()
        window = sg.Window(
            'Gestor de Cobranças',
            layout,
            element_padding=7
        )
    elif event == '-LIMPAR-':
        limpar_campos()
    elif event == '-CADASTRAR-':
        client.create(
            'Pessoa Jurídica' if values['-1JURIDICA-'] else 'Pessoa Física',
            values['-INPUT_FANTASIA-'],
            values['-INPUT_NOME-'],
            values['-INPUT_BAIRRO-'],
            values['-INPUT_TELEFONE-']
        )
        sg.PopupOK(f'Cliente {values["-INPUT_NOME-"]} cadastrado com sucesso.')
        limpar_campos()
