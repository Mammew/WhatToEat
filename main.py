from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.relativelayout import RelativeLayout
import subprocess
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

'''class IconButton(Button):
    def __init__(self, icon_source, **kwargs):
        super(IconButton, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (50, 50)
        self.background_normal = ''
        self.background_color = (0, 0, 0, 0) 
        self.icon = Image(source=icon_source)
        self.add_widget(self.icon)
'''

class NavBar(BoxLayout):
    """Navbar in basso per la navigazione"""
    def __init__(self, screen_manager, **kwargs):
        super(NavBar, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = 0.1
        self.spacing = 10
        self.padding = 10

        self.screen_manager = screen_manager

        home_btn = Button(text="Home", background_color=(0.2, 0.6, 1, 1))
        #home_layout = RelativeLayout()
        #icon_size = (home_btn.width * 0.2, home_btn.height * 0.8)  # Adatta le dimensioni dell'icona
        #home_icon = Image(source='image/home_icon.png', size_hint=(None, None), size=icon_size, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        #home_layout.add_widget(home_icon)
        #home_btn.add_widget(home_icon)
        home_btn.bind(on_press=lambda x: self.switch_screen("home"))
        self.add_widget(home_btn)

        history_btn = Button(text="History", background_color=(0.2, 0.6, 1, 1))
        history_btn.bind(on_press=lambda x: self.execute_and_switch("history", "history.py"))
        self.add_widget(history_btn)

        settings_btn = Button(text="Settings", background_color=(0.2, 0.6, 1, 1))
        settings_btn.bind(on_press=lambda x: self.execute_and_switch("settings", "settings.py"))
        self.add_widget(settings_btn)

    def switch_screen(self, screen_name):
        self.screen_manager.current = screen_name
    
    def execute_file(self, file_path):
        subprocess.run(["python3", file_path])

    def execute_and_switch(self, screen_name, file_path):
        self.switch_screen(screen_name)
        self.execute_file(file_path)
        

class ParentApp(App):
    def build(self):
        self.title = "Dish Extractor"
        self.screen_manager = ScreenManager()

        # Crea le schermate
        home_screen = Screen(name="home")
        home_screen.add_widget(ChildApp())
        self.screen_manager.add_widget(home_screen)

        history_screen = Screen(name="history")
        history_screen.add_widget(Label(text="History Screen"))
        self.screen_manager.add_widget(history_screen)

        settings_screen = Screen(name="settings")
        settings_screen.add_widget(Label(text="Settings Screen"))
        self.screen_manager.add_widget(settings_screen)

        # Crea il layout principale
        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(self.screen_manager)
        main_layout.add_widget(NavBar(self.screen_manager))

        return main_layout

if __name__ == "__main__":
    ParentApp().run()
