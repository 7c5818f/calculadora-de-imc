from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from .components.button import SCButton
from .components.separator import Separator
from .components.popup import DeletionPopup

import sqlite3


class EntriesScreen(Screen):

    popup = ObjectProperty()
    entry_id = NumericProperty()
    event = ObjectProperty()

    def delete_entry(self, dt):
        if self.popup.delete_entry is not None:
            if self.popup.delete_entry:
                conn = sqlite3.connect('data.db')
                cursor = conn.cursor()
                table_name = self.manager.screens[1].selected_table
                cursor.execute(f'DELETE FROM {table_name} WHERE id = {self.entry_id};')
                conn.commit()
                cursor.close()
                conn.close()
                self.on_pre_enter()
            Clock.unschedule(self.event)

    def option_pressed(self, instance):
        self.popup = DeletionPopup()
        self.popup.open()
        self.entry_id = int(instance.text.split(' / ')[0])
        self.event = Clock.schedule_interval(self.delete_entry, 0)

    def on_pre_enter(self):
        self.ids.table_name.text = f'ENTRADAS DE {self.manager.screens[1].selected_table.strip().upper()}'
        table_name = self.manager.screens[1].selected_table.strip().replace(' ', '_')
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {table_name}')
        results = cursor.fetchall()
        self.ids.options.clear_widgets()
        for res in results:
            self.ids.options.add_widget(
                SCButton(
                    size_hint=(1, None), padding=['5dp', '10dp'],
                    halign='center', color=(0, 0, 0, 1),
                    text=f"{res[0]} / {res[1]} / {res[2]} / {res[3]} / {res[4]} / {res[5]} / {res[6]:.3f}",
                    on_release=self.option_pressed
                )
            )
            self.ids.options.add_widget(Separator())
