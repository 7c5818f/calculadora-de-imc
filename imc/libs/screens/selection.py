from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from .components.button import SCButton
from .components.separator import Separator
from .components.label import CLabel
from .components.popup import OptionsPopup

import sqlite3


class SelectionScreen(Screen):

    selected_table = StringProperty()
    popup = ObjectProperty()
    clock_event = ObjectProperty

    def on_pre_enter(self):
        self.ids.options.clear_widgets()
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        if len(tables) > 1:
            for table in tables:
                if table[0] != 'sqlite_sequence':
                    self.ids.options.add_widget(
                        SCButton(
                            size_hint=(1, None),
                            height='60dp',
                            color=(0, 0, 0, 1),
                            text=f"    {table[0].replace('_', ' ')}",
                            on_release=self.option_pressed
                        )
                    )
                    self.ids.options.add_widget(Separator())
        else:
            self.ids.options.padding = '20dp'
            self.ids.options.add_widget(
                CLabel(pos_hint={'center_x': 0.5},
                text='Nenhuma base de dados disponível')
            )
        cursor.close()
        conn.close()
    
    def check_user_choice(self, dt):
        if self.popup.chosen_option != '':
            if self.popup.chosen_option == 'view_statistics':
                self.manager.transition.direction = 'left'
                self.manager.current = 'statistics_screen'
            elif self.popup.chosen_option == 'view_entries':
                self.manager.transition.direction = 'left'
                self.manager.current = 'entries_screen'
            else:
                conn = sqlite3.connect('data.db')
                cursor = conn.cursor()
                cursor.execute(f"DROP TABLE IF EXISTS {self.selected_table.strip().replace(' ', '_')}")
                cursor.close()
                conn.close()
                self.on_pre_enter()
            self.popup.chosen_option = ''
            Clock.unschedule(self.clock_event)

    def option_pressed(self, instance):
        self.selected_table = instance.text
        if self.manager.screens[0].context == 'selection_for_calc':
            self.manager.transition.direction = 'left'
            self.manager.current = 'calculator_screen'
        else:
            self.popup = OptionsPopup()
            self.popup.open()
            self.clock_event = Clock.schedule_interval(self.check_user_choice, 0)
