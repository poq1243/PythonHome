from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

class Npc(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.img = Image(source = "config.png", size=(400,300))
        self.add_widget(self.img)

class MyApp(App):
    def build(self):
        return Npc()

MyApp().run()