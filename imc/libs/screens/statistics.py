from kivy.uix.screenmanager import Screen

import sqlite3


class StatisticsScreen(Screen):

    def on_pre_enter(self):
        self.ids.table_name.text = f'ESTATÍSTICAS DE {self.manager.screens[1].selected_table.strip().upper()}'
        table_name = self.manager.screens[1].selected_table.strip().replace(' ', '_')
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        ###
        query = f'''
        SELECT AVG(bmi) AS average_bmi
        FROM {table_name}
        WHERE sex = 'M'
        AND (julianday('now') - julianday(birth_date)) / 365.25 BETWEEN 6 AND 15;
        '''
        cursor.execute(query)
        result = str(cursor.fetchone()[0])
        if result == 'None':
            self.ids.bmi_boys.text = 'Indisponível'
        else:
            self.ids.bmi_boys.text = result
        ###
        query = f'''
        SELECT AVG(bmi) AS average_bmi
        FROM {table_name}
        WHERE sex = 'F'
        AND (julianday('now') - julianday(birth_date)) / 365.25 BETWEEN 6 AND 15;
        '''
        cursor.execute(query)
        result = str(cursor.fetchone()[0])
        if result == 'None':
            self.ids.bmi_girls.text = 'Indisponível'
        else:
            self.ids.bmi_girls.text = result
        ###
        query = f'''
        SELECT AVG(bmi) AS average_bmi
        FROM {table_name}
        WHERE sex = 'M'
        AND (julianday('now') - julianday(birth_date)) / 365.25 BETWEEN 16 AND 60;
        '''
        cursor.execute(query)
        result = str(cursor.fetchone()[0])
        if result == 'None':
            self.ids.bmi_xy_adults.text = 'Indisponível'
        else:
            self.ids.bmi_xy_adults.text = result
        ###
        query = f'''
        SELECT AVG(bmi) AS average_bmi
        FROM {table_name}
        WHERE sex = 'F'
        AND (julianday('now') - julianday(birth_date)) / 365.25 BETWEEN 16 AND 60;
        '''
        cursor.execute(query)
        result = str(cursor.fetchone()[0])
        if result == 'None':
            self.ids.bmi_xx_adults.text = 'Indisponível'
        else:
            self.ids.bmi_xx_adults.text = result
        ###
        query = f'''
        SELECT AVG(bmi) AS average_bmi
        FROM {table_name}
        WHERE (julianday('now') - julianday(birth_date)) / 365.25 BETWEEN 16 AND 60;
        '''
        cursor.execute(query)
        result = str(cursor.fetchone()[0])
        if result == 'None':
            self.ids.bmi_adults.text = 'Indisponível'
        else:
            self.ids.bmi_adults.text = result
        ###
        query = f'''
        SELECT AVG(bmi) AS average_bmi
        FROM {table_name}
        WHERE sex = 'M'
        AND (julianday('now') - julianday(birth_date)) / 365.25 > 60;
        '''
        cursor.execute(query)
        result = str(cursor.fetchone()[0])
        if result == 'None':
            self.ids.bmi_xy_elders.text = 'Indisponível'
        else:
            self.ids.bmi_xy_elders.text = result
        ###
        query = f'''
        SELECT AVG(bmi) AS average_bmi
        FROM {table_name}
        WHERE sex = 'F'
        AND (julianday('now') - julianday(birth_date)) / 365.25 > 60;
        '''
        cursor.execute(query)
        result = str(cursor.fetchone()[0])
        if result == 'None':
            self.ids.bmi_xx_elders.text = 'Indisponível'
        else:
            self.ids.bmi_xx_elders.text = result
        ###
        query = f'''
        SELECT AVG(bmi) AS average_bmi
        FROM {table_name}
        WHERE (julianday('now') - julianday(birth_date)) / 365.25 > 60;
        '''
        cursor.execute(query)
        result = str(cursor.fetchone()[0])
        if result == 'None':
            self.ids.bmi_elders.text = 'Indisponível'
        else:
            self.ids.bmi_elders.text = result
