# напиши модуль для работы с анимацией
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.uix.button import Button
class Runner(BoxLayout):
    finished = BooleanProperty(False)
    value = NumericProperty(0)
    def __init__(self, total=10, steptime=1, autorepeat=True, bcolor=(0.78, 0.17, 0,96, 1), btext_inprogress="Приседание", **kwargs):
        super().__init__(**kwargs)
        self.autorepeat = autorepeat
        self.btext_inprogress = btext_inprogress
        self.total = total
        self.animation = (Animation(pos_hint={"top: 0.1"}, duration=steptime/2)) + (Animation(pos_hint={"top":1.0}, duration=steptime/2))
        self.animation.on_progress = self.next
        self.btn = Button(size_hint=(1, 0.1), pos_hint={"top": 1.0})
        self.add_widget(self.btn)

    def start(self):
        self.value = 0
        self.finished = False
        self.btn.text = self.btext_inprogress
        if self.autorepeat:
            self.animation.repeat = True
        self.animation.start(self.btn)
    def next(self, widget, step):
        if step == 1.0:
            self.value += 1
            if self.value >= self.total:
                self.animation.repeat = False
                self.finished = True