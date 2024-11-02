from kivy.lang import Builder
from kivy.uix.button import Button


Builder.load_string(
"""
<CButton>:
    background_normal: 'assets/images/btn_normal.png'
    background_down: 'assets/images/btn_down.png'
    color: rgba('#ffffff')
    bold: True
    font_size: '14sp'
<SCButton>:
    background_normal: 'assets/images/selection_btn_normal.png'
    background_down: 'assets/images/selection_btn_down.png'
    text_size: self.size
    halign: 'left'
    valign: 'center'
    bold: True
    font_size: '14sp'
"""
)


class CButton(Button):
    pass


class SCButton(Button):
    pass

