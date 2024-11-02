from kivy.lang import Builder
from kivy.uix.textinput import TextInput


Builder.load_string(
"""
<CTextInput>:
    background_normal: 'assets/images/txtinput_normal.png'
    background_active: 'assets/images/txtinput_active.png'
    cursor_color: rgba('#000000')
    padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
    multiline: False

<CCTextInput>:
    size_hint: (None, None)
    size: ('65dp', '30dp')
    input_type: 'number'
"""
)


class CTextInput(TextInput):
    pass


class CCTextInput(CTextInput):
    pass
