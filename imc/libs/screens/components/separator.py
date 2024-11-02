from kivy.lang import Builder
from kivy.uix.widget import Widget


Builder.load_string(
"""
<Separator>:
    size_hint: (1, None)
    height: '1dp'
    canvas.before:
        Color:
            rgba: rgba('#BFBFBF')
        Rectangle:
            pos: self.pos
            size: self.size
"""
)


class Separator(Widget):
    pass