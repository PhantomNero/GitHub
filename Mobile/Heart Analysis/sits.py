# напиши модуль для подсчета количества приседаний
from kivy.uix.label import Label
class Sits(Label):
    
    def __init__(self, total, **kwargs):
        self.current = 0
        self.total = total
        my_text = "Приседаем ещё " + str(self.total) + " раз."
        super().__init__(text=my_text, **kwargs)

    def next(self, *args):
        self.current += 1
        remain = max(0, self.total - self.current)
        my_text = "Приседаем ещё " + str(remain) + " раз."
        self.text = my_text
