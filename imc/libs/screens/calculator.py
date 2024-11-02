from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.clock import Clock

from .components.popup import ResultPopup
from .components.popup import ErrorPopup

from datetime import datetime, date
import sqlite3


class DateError(Exception):
    pass


class CalculatorScreen(Screen):

    birth_date = StringProperty()
    bmi = NumericProperty()
    popup = ObjectProperty()
    event = ObjectProperty()

    def calculate_age(self):
        try:
            birth_day = int(self.ids.birth_day.text)
            birth_month = int(self.ids.birth_month.text)
            birth_year = int(self.ids.birth_year.text)
            self.birth_date = f'{birth_year}-{birth_month}-{birth_day}'
            birth_date = datetime(birth_year, birth_month, birth_day)
            today_date = datetime(date.today().year, date.today().month, date.today().day)
            age = today_date - birth_date
            age = int((age.days + age.seconds / 86400) / 365.2425)
            if age < 0:
                raise DateError('Valor inválido para dia, mês ou ano!')
            if age < 6:
                raise DateError('Não é possível calcular o IMC de uma pessoa menor de 6 anos!')
        except ValueError:
            raise DateError('Valor inválido para dia, mês ou ano!')
        else:
            return age

    def clear_fields(self):
        self.ids.first_name.text = ''
        self.ids.birth_year.text = ''
        self.ids.birth_month.text = ''
        self.ids.birth_day.text = ''
        self.ids.weight.text = ''
        self.ids.height.text = ''

    def save_result(self, dt):
        if self.popup.save_result is not None:
            if self.popup.save_result:
                conn = sqlite3.connect('data.db')
                cursor = conn.cursor()
                table_name = self.manager.screens[1].selected_table
                if self.ids.male.active:
                    sex = 'M'
                else:
                    sex = 'F'
                insert_into = f'''
                INSERT INTO {table_name} (first_name, birth_date, sex, height, weight, bmi)
                values (?, ?, ?, ?, ?, ?);'''
                cursor.execute(
                    insert_into, (self.ids.first_name.text.split(' ')[0], self.birth_date, sex,
                    float(self.ids.height.text), float(self.ids.weight.text), self.bmi)
                )
                conn.commit()
                cursor.close()
                conn.close()
            self.clear_fields()
            Clock.unschedule(self.event)

    def calculate(self):
        popup = ErrorPopup()
        try:
            age = self.calculate_age()
            self.bmi = float(self.ids.weight.text) / ((float(self.ids.height.text)/100) * (float(self.ids.height.text)/100))
        except (ZeroDivisionError, ValueError):
            popup.msg = 'Valor inválido para peso ou altura!'
            popup.open()
        except DateError as err:
            popup.msg = str(err)
            popup.open()
        else:
            if age <= 15:
                if self.ids.male == True:
                    bmi_table = {
                        6: (14.5, 16.6, 18), 7: (15, 17.3, 19.1), 8: (15.6, 16.7, 20.3),
                        9: (16.1, 18.8, 21.4), 10: (16.7, 19.6, 22.5), 11: (17.2, 20.3, 23.7),
                        12: (17.8, 21.1, 24.8), 13: (18.5, 21.9, 25.9), 14: (19.2, 22.7, 26.9),
                        15: (19.9, 23.6, 27.7)
                    }
                else:
                    bmi_table = {
                        6: (14.3, 16.1, 17.4), 7: (14.9, 17.1, 18.9), 8: (15.6, 18.1, 20.3),
                        9: (16.3, 19.1, 21.7), 10: (17, 20.1, 23.2), 11: (17.6, 21.1, 24.5),
                        12: (18.3, 22.1, 25.9), 13: (18.9, 23, 27.7), 14: (19.3, 23.8, 27.9),
                        15: (19.6, 24.2, 28.8)
                    }
                if self.bmi < bmi_table[age][0]:
                    category = 'abaixo do peso'
                elif self.bmi >= bmi_table[age][0] and self.bmi < bmi_table[age][1]:
                    category = 'peso normal'
                elif self.bmi >= bmi_table[age][1] and self.bmi < bmi_table[age][2]:
                    category = 'sobrepeso'
                else:
                    category = 'obesidade'
            elif age <= 60:
                if self.bmi < 18.5:
                    category = 'abaixo do peso'
                elif self.bmi >= 18.5 and self.bmi < 25:
                    category = 'peso normal'
                elif self.bmi >= 25 and self.bmi < 30:
                    category = 'sobrepeso'
                elif self.bmi >= 30 and self.bmi < 35:
                    category = 'obesidade grau 1'
                elif self.bmi >= 35 and self.bmi < 40:
                    category = 'obesidade grau 2 (severa)'
                else:
                    category = 'obesidade grau 3 (mórbita)'
            else:
                if self.bmi < 22:
                    category = 'abaixo do peso'
                elif self.bmi >= 22 and self.bmi < 27:
                    category = 'peso normal'
                elif self.bmi >= 27 and self.bmi < 30:
                    category = 'sobrepeso'
                elif self.bmi >= 30 and self.bmi < 35:
                    category = 'obesidade grau 1'
                elif self.bmi >= 35 and self.bmi < 40:
                    category = 'obesidade grau 2 (severa)'
                else:
                    category = 'Obesidade grau 3 (mórbita)'
            self.popup = ResultPopup()
            self.popup.bmi = f'IMC.........: {self.bmi}'
            self.popup.category = f'categoria...: {category}'
            self.popup.open()
            self.event = Clock.schedule_interval(self.save_result, 0)
