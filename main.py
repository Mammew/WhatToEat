import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from functions import funct  # Importa la funzione dal file functions.py

class childApp(BoxLayout):
    def __init__(self, **kwargs): # kwargs is used for adding unlimited args
        super(childApp, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        with self.canvas.before:
            Color(1, 1, 1, 0.8)  # bianco
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self._update_rect, pos=self._update_rect)

        #self.add_widget(Label(text="Dish Name", size_hint=(1, 0.2), bold=True, font_size=24))
        title_label = Label(text="Dish Name", size_hint=(1, 0.2), bold=True, font_size=24)
        with title_label.canvas.before:
            Color(0, 0, 1, 0.5)  # Colore blu
            self.title_rect = Rectangle(size=title_label.size, pos=title_label.pos)
        title_label.bind(size=self._update_title_rect, pos=self._update_title_rect)
        self.add_widget(title_label)

        self.result_label = Label(text="", size_hint=(1, 0.4), color=(0, 0, 0, 1), bold=True, font_size=18)
        self.add_widget(self.result_label)

        self.submit = Button(text="Extract Dish", size_hint=(1, 0.2), background_color=(0, 1, 0, 1))
        self.submit.bind(on_press=self.call_funct)
        self.add_widget(self.submit)
    
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def _update_title_rect(self, instance, value):
        self.title_rect.pos = instance.pos
        self.title_rect.size = instance.size
    
    def call_funct(self, instance):
        funct(instance, self.result_label)  # call the function from functions.py

class parentApp(App):
    def build(self):
        return childApp()
    
if __name__ == "__main__": # Check if the code is run from the main file
    parentApp().run()

# Run the code
