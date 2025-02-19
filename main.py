from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, RoundedRectangle
from functions import funct  # Importa la funzione dal file functions.py

class ChildApp(BoxLayout):
    def __init__(self, **kwargs):
        super(ChildApp, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 15

        with self.canvas.before:
            Color(0.95, 0.95, 0.95, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        self.title_label = Label(
            text="Dish Extractor",
            size_hint=(1, 0.2),
            bold=True,
            font_size='28sp',
            color=(0, 0, 0, 1)
        )
        self.add_widget(self.title_label)

        self.result_label = Label(
            text="Press the button to extract a dish!",
            size_hint=(1, 0.3),
            color=(0.2, 0.2, 0.2, 1),
            font_size='20sp'
        )
        self.add_widget(self.result_label)

        self.submit = Button(
            text="Extract Dish",
            size_hint=(0.8, 0.2),
            pos_hint={'center_x': 0.5},
            background_color=(0.2, 0.6, 1, 1),
            color=(1, 1, 1, 1),
            bold=True,
            font_size='20sp'
        )
        self.submit.bind(on_press=self.call_funct)
        self.add_widget(self.submit)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def call_funct(self, instance):
        funct(instance, self.result_label)

class ParentApp(App):
    def build(self):
        self.title = "Dish Extractor"
        return ChildApp()

if __name__ == "__main__":
    ParentApp().run()
