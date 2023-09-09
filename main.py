from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from random import randint 

def check_int(num):
    try:
        return int(num)
    except:
        return False
    
def randomed(first, second):
    try:
        return randint(first, second)
    except:
        return 'Неверное число'
    
first_num = None
second_num = None
res = None

Config.set('kivy', 'window_icon', 'logo.png')
Config.set('kivy', 'window_title', 'Генератор рандомных чисел')

class First(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vertical = BoxLayout(orientation='vertical', padding=5, spacing=5, pos_hint = { 'center_x': 0.5, 'center_y': 0.5 }, size_hint_y = 0.6)
        line1 = BoxLayout(size_hint=(0.7, None), height='30sp', pos_hint = { 'center_x': 0.5, 'center_y': 0.5 })
        line2 = BoxLayout(size_hint=(0.7, None), height='30sp', pos_hint = { 'center_x': 0.5, 'center_y': 0.5 })
        line3 = BoxLayout(size_hint=(0.7, None), height='200sp', pos_hint = { 'center_x': 0.5, 'center_y': 0.5 })
        img = Image(source='bg.jpg', allow_stretch=True, keep_ratio=False)
        img.size = Window.size
        generator = Label(text='Генератор рандомных чисел', color=(0, 0, 0, 1), font_size=20, font_name='font.ttf')
        first_num = Label(text='От', color=(0, 0, 0, 1), font_name='font.ttf')
        self.first_num_field = TextInput(multiline=False)
        second_num = Label(text='До', color=(0, 0, 0, 1), font_name='font.ttf')
        self.second_num_field = TextInput(multiline=False)
        submit_btn = Button(text='Сгенерировать', background_color=(100, 100, 100, 1), color=(0, 0, 0, 1), font_name='font.ttf')
        submit_btn.size_hint = (0.33, 0.33)
        submit_btn.pos_hint = {'x': 0.33, 'y': 0.33}
        submit_btn.on_press = self.next
        Window.add_widget(img)
        line1.add_widget(first_num)
        line1.add_widget(self.first_num_field)
        line2.add_widget(second_num)
        line2.add_widget(self.second_num_field)
        line3.add_widget(submit_btn)
        vertical.add_widget(generator)
        vertical.add_widget(line1)
        vertical.add_widget(line2)
        vertical.add_widget(line3)
        self.add_widget(vertical)

    def next(self):
        global first_num, second_num, res
        first_num = check_int(self.first_num_field.text)
        second_num = check_int(self.second_num_field.text)
        res = randomed(first_num, second_num)
        self.manager.transition.direction = 'up'
        self.manager.current = 'second'

class Second(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vertical = BoxLayout(orientation='vertical', padding=5, spacing=5, pos_hint = { 'center_x': 0.5, 'center_y': 0.5 }, size_hint_y = 0.6)
        line1 = BoxLayout(size_hint=(0.7, None), height='30sp', pos_hint = { 'center_x': 0.5, 'center_y': 0.5 })
        line2 = BoxLayout(size_hint=(0.7, None), height='30sp', pos_hint = { 'center_x': 0.5, 'center_y': 0.5 })
        line3 = BoxLayout(size_hint=(0.7, None), height='200sp', pos_hint = { 'center_x': 0.5, 'center_y': 0.5 })
        img = Image(source='bg.jpg', allow_stretch=True, keep_ratio=False)
        img.size = Window.size
        self.text = Label(text='Сгенерированное число:', color=(0, 0, 0, 1), font_size=20, font_name='font.ttf')
        self.result = Label(text='', color=(0, 0, 0, 1), font_size=20, font_name='font.ttf')
        self.on_enter = self.txt
        back_btn = Button(text='Сгенерировать заново', background_color=(100, 100, 100, 1), color=(0, 0, 0, 1), font_name='font.ttf')
        back_btn.size_hint = (0.33, 0.33)
        back_btn.pos_hint = {'x': 0.33, 'y': 0.33}
        back_btn.on_press = self.back
        Window.add_widget(img)
        line1.add_widget(self.text)
        line2.add_widget(self.result)
        line3.add_widget(back_btn)
        vertical.add_widget(line1)
        vertical.add_widget(line2)
        vertical.add_widget(line3)
        self.add_widget(vertical)

    def txt(self):
        global res
        self.result.text = str(res)
    
    def back(self):
        global first_num, second_num, res
        first_num = None
        second_num = None
        res = None
        self.manager.transition.direction = 'down'
        self.manager.current = 'first'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(First(name='first'))
        sm.add_widget(Second(name='second'))

        return sm

MyApp().run() 