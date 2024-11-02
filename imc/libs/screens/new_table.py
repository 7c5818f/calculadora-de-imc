from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

from .components.popup import ErrorPopup

import sqlite3

class NewTableScreen(Screen):

    def on_pre_enter(self):
        self.ids.table_name.text = ''
        Clock.schedule_interval(self.update_total_characters, 0)

    def update_total_characters(self, dt):
        lenght = len(self.ids.table_name.text)
        self.ids.total_characters.text = f'{lenght}/32'
        if lenght >= 4 and lenght <= 32:
            self.ids.total_characters.color = (0, 1, 0, 1)
        else:
            self.ids.total_characters.color = (1, 0, 0, 1)

    def create_table(self):
        lenght = len(self.ids.table_name.text)
        popup = ErrorPopup()
        popup.msg = 'Nome inválido!'
        if lenght < 4 or lenght > 32:
            popup.open()
        else:
            try:
                conn = sqlite3.connect('data.db')
                cursor = conn.cursor()
                cursor.execute(
                f'''
                CREATE TABLE {self.ids.table_name.text.strip().replace(' ', '_')} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    birth_date DATE NOT NULL,
                    sex TEXT CHECK(sex in ('M', 'F')) NOT NULL,
                    height REAL NOT NULL,
                    weight REAL NOT NULL,
                    bmi REAL NOT NULL
                );
                '''
                )
                cursor.close()
                conn.close()
            except:
                popup.open()
            else:
                self.manager.transition.direction = 'right'
                self.manager.current = 'selection_screen'