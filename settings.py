from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Settings(BoxLayout):
    def __init__(self, **kwargs):
        super(Settings, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.add_widget(Label(text="Settings", size_hint_y=0.1))

        self.add_widget(Label(text="Setting 1"))
        self.setting1 = TextInput(multiline=False)
        self.add_widget(self.setting1)

        self.add_widget(Label(text="Setting 2"))
        self.setting2 = TextInput(multiline=False)
        self.add_widget(self.setting2)

        self.add_widget(Label(text="Setting 3"))
        self.setting3 = TextInput(multiline=False)
        self.add_widget(self.setting3)

        save_btn = Button(text="Save Settings")
        save_btn.bind(on_press=self.save_settings)
        self.add_widget(save_btn)

    def save_settings(self, instance):
        settings = {
            'setting1': self.setting1.text,
            'setting2': self.setting2.text,
            'setting3': self.setting3.text
        }
        with open('settings.txt', 'w') as file:
            file.write(str(settings))
        print("Settings saved")