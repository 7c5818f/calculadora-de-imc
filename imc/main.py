"""
Autor: Isaak Gomes
"""

from kivy.core.window import Window
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager

from libs.screens.components import button
from libs.screens.components import label
from libs.screens.components import textinput
from libs.screens.components import checkbox
from libs.screens.components import separator
from libs.screens.home import HomeScreen
from libs.screens.selection import SelectionScreen
from libs.screens.statistics import StatisticsScreen
from libs.screens.new_table import NewTableScreen
from libs.screens.calculator import CalculatorScreen
from libs.screens.entries import EntriesScreen


Window.softinput_mode = 'below_target'
Window.size = (340, 600)


class MainApp(App):

    def load_all_kv_files(self):
        Builder.load_file('libs/screens/home.kv')
        Builder.load_file('libs/screens/selection.kv')
        Builder.load_file('libs/screens/statistics.kv')
        Builder.load_file('libs/screens/new_table.kv')
        Builder.load_file('libs/screens/calculator.kv')
        Builder.load_file('libs/screens/entries.kv')

    def build(self):
        self.load_all_kv_files()
        Config.set(
            'kivy', 'default_font',
            ['LiberationSans',
            'assets/fonts/LiberationSans/LiberationSans-Regular.ttf',
            'assets/fonts/LiberationSans/LiberationSans-Italic.ttf',
            'assets/fonts/LiberationSans/LiberationSans-Bold.ttf',
            'assets/fonts/LiberationSans/LiberationSans-BoldItalic.ttf']
        )
        LabelBase.register(
            name='DejaVuSansMono',
            fn_regular='assets/fonts/DejaVuSansMono/DejaVuSansMono.ttf',
            fn_bold='assets/fonts/DejaVuSansMono/DejaVuSansMono-Bold.ttf',
            fn_italic='assets/fonts/DejaVuSansMono/DejaVuSansMono-Oblique.ttf',
            fn_bolditalic='assets/fonts/DejaVuSansMono/DejaVuSansMono-BoldOblique.ttf'
        )
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home_screen'))
        sm.add_widget(SelectionScreen(name='selection_screen'))
        sm.add_widget(StatisticsScreen(name='statistics_screen'))
        sm.add_widget(NewTableScreen(name='new_table_screen'))
        sm.add_widget(CalculatorScreen(name='calculator_screen'))
        sm.add_widget(EntriesScreen(name='entries_screen'))
        return sm


if __name__ == '__main__':
    MainApp().run()
