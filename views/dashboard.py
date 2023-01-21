from .widgets.menu import Menu
import PySimpleGUI as sg

class Dashboard(Menu):
    def __init__(self):
        self.design = [
            [sg.Menu(self.menu_bar)],
            [sg.Image(filename='dashboard.png')]
        ]