from .widgets.menu import Menu
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg


class Dashboard(Menu):
    @staticmethod
    def create_plot():
        plt.plot([10, 20, 30], ['vencidos', 'abertos', 'faturados'])
        return plt.gcf()

    @staticmethod
    def draw_figure(canvas, figure):
        fg = FigureCanvasTkAgg(figure, canvas)
        fg.draw()
        fg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return fg

    @staticmethod
    def button_shape(quantity: str, key: str, color: str) -> sg.Button:
        return sg.Button(quantity,
                         key=key,
                         font=(None, 30),
                         border_width=0,
                         button_color=(color, 'lightgrey'),
                         size=3)

    def layout(self,
               expired_tickets: int,
               pending_tickets: int,
               paid_tickets: int) -> list[list[sg.Element]]:
        return [
            [sg.Menu(self.menu_bar)],
            [
                sg.Push(),
                sg.Column([
                    [self.button_shape(str(expired_tickets),
                                       '-COBRANÇAS VENCIDAS-',
                                       'red')],
                    [sg.Text('Boletos vencidos')]
                ], element_justification='center'),
                sg.Push(),
                sg.Column([
                    [self.button_shape(str(pending_tickets),
                                       'Relatório cobranças',
                                       'darkorange')],
                    [sg.Text('Boletos abertos')]
                ], element_justification='center'),
                sg.Push(),
                sg.Column([
                    [self.button_shape(str(paid_tickets),
                                       '-COBRANÇAS PAGAS-',
                                       'green')],
                    [sg.Text('Boletos pagos')]
                ], element_justification='center'),
                sg.Push()
            ],
            [sg.Canvas(size=(500, 300), key='-CANVAS-')]
        ]
