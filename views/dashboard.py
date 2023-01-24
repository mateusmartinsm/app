from .widgets.menu import Menu
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg


class Dashboard(Menu):
    def create_plot(self):
        plt.plot([10, 20, 30], ['vencidos', 'abertos', 'faturados'])
        return plt.gcf()

    def draw_figure(self, canvas, figure):
        fg = FigureCanvasTkAgg(figure, canvas)
        fg.draw()
        fg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return fg

    def layout(self) -> list:
        return [
            [sg.Menu(self.menu_bar)],
            [
                sg.Push(),
                sg.Column([
                    [sg.Text('4', font=(None, 30), text_color='red')],
                    [sg.Text('Boletos vencidos')]
                ], element_justification='center'),
                sg.Push(),
                sg.Column([
                    [sg.Text('15', font=(None, 30), text_color='darkorange')],
                    [sg.Text('Boletos abertos')]
                ], element_justification='center'),
                sg.Push(),
                sg.Column([
                    [sg.Text('30', font=(None, 30), text_color='green')],
                    [sg.Text('Boletos pagos')]
                ], element_justification='center'),
                sg.Push()
            ],
            [sg.Canvas(size=(500, 300), key='-CANVAS-')]
        ]
