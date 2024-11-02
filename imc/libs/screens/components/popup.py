from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty

from kivy.clock import Clock


Builder.load_string(
"""
<ResultPopup>:
    size_hint: (0.85, None)
    height: '300dp'
    title: ''
    separator_height: 0
    background: 'assets/images/popup_background.png'
    auto_dismiss: False
    FloatLayout:
        padding: 0
        size_hint: (1, 1)
        BoxLayout:
            orientation: 'vertical'
            size_hint: (None, None)
            size: self.minimum_size
            pos_hint: {'center_x': 0.5, 'top': 1}
            padding: '20dp'
            spacing: '5dp'
            canvas.before:
                Color:
                    rgba: rgba('#000000')
                Rectangle:
                    pos: self.pos
                    size: self.size
            canvas.after:
                Color:
                    rgba: rgba('#BFBFBF')
                Line:
                    width: 2
                    rectangle: self.x, self.y, self.width, self.height
            CLabel:
                id: bmi_label
                font_name: 'DejaVuSansMono'
                font_size: '11sp'
                color: rgba('#ffffff')
                text: 'IMC.........: '
            CLabel:
                id: category_label
                font_name: 'DejaVuSansMono'
                font_size: '11sp'
                color: rgba('#ffffff')
                text: 'Categoria...: '
        BoxLayout:
            orientation: 'vertical'
            size_hint: (1, None)
            height: self.minimum_size[1]
            pos_hint: {'x': 0, 'y': -0.04}
            spacing: '15dp'
            CLabel:
                text: 'Deseja registrar este resultado?'
                pos_hint: {'center_x': 0.5}
            BoxLayout:
                orientation: 'horizontal'
                size_hint: (1, None)
                height: self.minimum_size[1]
                spacing: '2dp'
                CButton:
                    size_hint: (0.5, None)
                    height: '40dp'
                    text: 'Sim'
                    on_release: root.save_data()
                CButton:
                    size_hint: (0.5, None)
                    height: '40dp'
                    background_normal: 'assets/images/red_btn_normal.png'
                    background_down: 'assets/images/red_btn_down.png'
                    text: 'Não'
                    on_release: root.dont_save_data()


<ErrorPopup>:
    size_hint: (0.85, None)
    height: '300dp'
    background: 'assets/images/popup_background.png'
    separator_height: '1dp'
    separator_color: rgba('#BFBFBF')
    auto_dismiss: False
    title: 'ERRO'
    title_color: rgba('#000000')
    title_align: 'center'
    FloatLayout:
        size_hint: (1, 1)
        CLabel:
            text: root.msg
            color: rgba('#000000')
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        CButton:
            size_hint: (0.33, None)
            height: '40dp'
            pos_hint: {'center_x': 0.5, 'y': 0}
            text: 'OK'
            on_release: root.dismiss()


<OptionsPopup>:
    size_hint: (0.85, None)
    height: '300dp'
    background: 'assets/images/popup_background.png'
    separator_height: '1dp'
    separator_color: rgba('#BFBFBF')
    auto_dismiss: False
    title: 'Que ação deseja realizar?'
    title_color: rgba('#000000')
    title_align: 'left'
    BoxLayout:
        orientation: 'vertical'
        size_hint: (1, 1)
        spacing: '20dp'
        Widget:
            size_hint: (1, None)
            height: '0dp'
        CButton:
            text: 'Visualizar estatísticas'
            size_hint: (1, 1)
            height: '40dp'
            on_release:
                root.chosen_option = 'view_statistics'
                root.dismiss()
        CButton:
            text: 'Visualizar entradas'
            size_hint: (1, 1)
            height: '40dp'
            on_release:
                root.chosen_option = 'view_entries'
                root.dismiss()
        CButton:
            text: 'Deletar base de dados'
            size_hint: (1, 1)
            height: '40dp'
            background_normal: 'assets/images/red_btn_normal.png'
            background_down: 'assets/images/red_btn_down.png'
            on_release:
                root.chosen_option = 'delete_table'
                root.dismiss()


<DeletionPopup@Popup>:
    size_hint: (0.85, None)
    title: ''
    separator_height: 0
    background: 'assets/images/popup_background.png'
    auto_dismiss: False
    BoxLayout:
        orientation: 'vertical'
        size_hint: (1, None)
        height: self.minimum_size[1]
        pos_hint: {'x': 0, 'y': -0.04}
        spacing: '15dp'
        CLabel:
            text: 'Deseja deletar este registro?'
            pos_hint: {'center_x': 0.5}
        BoxLayout:
            orientation: 'horizontal'
            size_hint: (1, None)
            height: self.minimum_size[1]
            spacing: '2dp'
            CButton:
                size_hint: (0.5, None)
                height: '40dp'
                text: 'Sim'
                on_release: root.del_entry()
            CButton:
                size_hint: (0.5, None)
                height: '40dp'
                background_normal: 'assets/images/red_btn_normal.png'
                background_down: 'assets/images/red_btn_down.png'
                text: 'Não'
                on_release: root.dont_del_entry()
"""
)


class ResultPopup(Popup):
    bmi = StringProperty()
    category = StringProperty()
    save_result = ObjectProperty(None)

    def on_open(self):
        self.ids.bmi_label.text = self.bmi
        self.ids.category_label.text = self.category
    
    def save_data(self):
        self.save_result = True
        self.dismiss()
    
    def dont_save_data(self):
        self.save_result = False
        self.dismiss()


class ErrorPopup(Popup):
    msg = StringProperty('')


class OptionsPopup(Popup):
    chosen_option = StringProperty()


class DeletionPopup(Popup):
    delete_entry = ObjectProperty(None)

    def del_entry(self):
        self.delete_entry = True
        self.dismiss()
    
    def dont_del_entry(self):
        self.delete_entry = False
        self.dismiss()