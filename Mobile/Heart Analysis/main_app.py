# напиши здесь свое приложение
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

from instructions import txt_instruction, txt_test1, txt_sits, txt_test3
from ruffier import test
from seconds import Seconds

age = 7
name = ""
p1, p2, p3 = 0, 0, 0

Window.clearcolor = (0.5, 0.55, 0.84, 0.4)
btn_color = (0.18, 0.21, 0.8, 1)
def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False


class InScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_instruction)
        lbl1 = Label(text="Введите имя:", halign="right")
        self.in_name = TextInput(multiline=False)
        lbl2 = Label(text="Введите возраст:", halign="right")
        self.in_age = TextInput(text="7", multiline=False)
        self.btn = Button(text="Начать", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        self.btn.background_color = btn_color
        self.btn.on_press = self.next
        line1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        line2 = BoxLayout(size_hint=(0.8, None), height="30sp")
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)
        outer = BoxLayout(orientation="vertical", spacing=8, padding=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def next(self):
        global name
        name = self.in_name.text
        age = check_int(self.in_age.text)
        if not age or age < 7:
            age = 7
            self.in_age.text = str(age)
        else:
            self.manager.current = "pulse1"


class PulseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        instr = Label(text=txt_test1)
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)
        line1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        lbl_result = Label(text="Введите результат:", halign="right")
        self.in_result = TextInput(text="0", multiline=False)
        self.in_result.set_disabled(True)

        line1.add_widget(lbl_result)
        line1.add_widget(self.in_result)
        self.btn = Button(text="Продолжить", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        self.btn.on_press = self.next
        self.btn.background_color = btn_color
        outer = BoxLayout(orientation="vertical", padding=8,spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.lbl_sec)
        outer.add_widget(line1)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def sec_finished(self, *args):

        self.next_screen = True
        self.in_result.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = "Продолжить"

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p1
            p1 = check_int(self.in_result.text)
            if not p1 or p1 <= 0:
                p1 = 0
                self.in_result.text = str(p1)
            else:
                self.manager.current = "sits"


class CheakSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_sits)
        self.btn = Button(text="Продолжить", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        self.btn.on_press = self.next
        outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.btn)
        self.add_widget(outer)
        self.btn.background_color = btn_color
    def next(self):
        self.manager.current = "pulse2"


class PulseScr2(Screen):
    def __init__(self, **kwargs):
        self.next_screen = False
        self.stage = 0
        super().__init__(**kwargs)

        instr = Label(text=txt_test3)
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)
        self.lbl1 = Label(text="Считаем пульс")


        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl_result1 = Label(text='Результат:', halign='right')
        self.in_result1 = TextInput(text='0', multiline=False)
        line1.add_widget(lbl_result1)
        line1.add_widget(self.in_result1)

        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl_result2 = Label(text='Результат после отдыха:', halign='right')
        self.in_result2 = TextInput(text='0', multiline=False)

        self.in_result1.set_disabled(True)
        self.in_result2 .set_disabled(True)
        line2.add_widget(lbl_result2)
        line2.add_widget(self.in_result2)

        self.btn = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        self.btn.background_color = btn_color
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.lbl1)
        outer.add_widget(self.lbl_sec)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def sec_finished(self, *args):
        if self.lbl_sec.done:
            if self.stage == 0:
                self.stage = 1
                self.lbl1.text = "Отдыхайте"
                self.lbl_sec.restart(30)
                self.in_result1.set_disabled(False)
            elif self.stage == 1:
                self.stage = 2
                self.lbl1.text = "Считайте пульс"
                self.lbl_sec.restart(15)
            elif self.stage == 2:
                self.in_result2.set_disabled(False)
                self.btn.set_disabled(False)
                self.btn.text = "Завершить"
                self.next_screen = True


    def next(self):
        if not self.next_screen:
            self.btn.dec_disabled(True)
            self.lbl_sec.start()
        else:
            global p2, p3
            p2 = int(self.in_result1.text)
            p3 = int(self.in_result2.text)
            if not p2:
                p2 = 0
                self.in_result1.text = str(p2)
            elif not p3:
                p3 = 0
                self.in_result1.text = str(p3)
            else:
                self.manager.current = "result"
class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.instr = Label(text="")
        self.outer.add_widget(self.instr)
        self.add_widget(self.outer)
        self.on_enter = self.before

    def before(self):
        global name
        self.instr.text = name + "\n" + test(p1, p2, p3, age)


class HeartCheak(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InScr(name="instr"))
        sm.add_widget(PulseScreen(name="pulse1"))
        sm.add_widget(PulseScr2(name="pulse2"))
        sm.add_widget(CheakSits(name="sits"))
        sm.add_widget(Result(name="result"))
        return sm


app = HeartCheak()
app.run()
