from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(
            text="Hello from Aviral!",
            font_size=30
        )

MyApp().run()