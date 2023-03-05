# напиши модуль для работы с анимацией
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
class Runner(BoxLayout):
    finished = BooleanProperty(False)
    value = NumericProperty(0)
    def __init__(self):
        pass

    def start(self):
        pass

    def next(self, widget, step):
        pass