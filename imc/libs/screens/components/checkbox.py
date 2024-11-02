from kivy.lang import Builder
from kivy.uix.checkbox import CheckBox
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.metrics import sp


Builder.load_string(
"""
<CCheckBox>:
    allow_no_selection: False
    canvas:
        Clear:
        Color:
            rgba: rgba(root.background_color)
        Rectangle:
            size: root.icon_size
            pos: (int(self.center_x - root.icon_size[0]/2), int(self.center_y - root.icon_size[1]/2))
        Color:
            rgba: rgba(root.background_color)
        Rectangle:
            source: 'assets/images/%s_%s.png' % (('radio' if self.group else 'checkbox'), ('on' if self.active else 'off'))
            size: root.icon_size
            pos: (int(self.center_x - root.icon_size[0]/2), int(self.center_y - root.icon_size[1]/2))
    size_hint: (None, None)
    size: root.icon_size
"""
)


class CCheckBox(CheckBox):
    background_color = StringProperty('#f6f8fa')
    icon_size = ListProperty((sp(24), sp(24)))
