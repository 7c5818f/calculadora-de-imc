from kivy.lang import Builder
from kivy.uix.label import Label


Builder.load_string(
"""
<CLabel>:
    size_hint: (None, None)
    size: self.texture_size
    font_size: '14sp'
    color: rgba('#000000')


<CWLabel@Label>:
    size_hint_y: None
    text_size: self.width, None
    height: self.texture_size[1]
    font_size: '14sp'
    color: rgba('#000000')
"""
)


class CLabel(Label):
    pass


class CWLabel(Label):
    pass
