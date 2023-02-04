import PySimpleGUI as sg


class Table:
    @staticmethod
    def shape(clients_register, headings, key):
        column_visibility = [False] + [True] * 5
        return sg.Table(clients_register,
                        headings,
                        key=key,
                        visible_column_map=column_visibility,
                        auto_size_columns=False,
                        def_col_width=20,
                        justification='center',
                        row_height=25,
                        header_background_color='lightblue',
                        row_colors=[
                            (i, 'white' if i % 2 == 0 else 'lightgray')
                            for i in range(len(clients_register))
                        ])
