from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition


class Participants_num(Screen):
    def switch_prev(self, *args):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = self.manager.previous()

class Participants_input(GridLayout):
    def __init__(self, **kwargs):
        super(Participants_input, self).__init__(**kwargs)
        self.padding = 10
        self.spacing = 10

        self.cols = 2
        self.rows = self.root.ids.part_num + 1
        self.add_widget(Label(text='Name', font_size=40))
        self.add_widget(Label(text='Number', font_size=40))



class IsthatmeApp(App):
    def build(self):
        root = ScreenManager()
        root.add_widget(Participants_num())
        root.add_widget(Participants_input())

        return root


if __name__ == '__main__':
    IsthatmeApp().run()

LabelBase.register(name = 'Roboto',
                   fn_regular='./font/Roboto-Thin.ttf',
                   fn_bold='./font/Roboto-Medium.ttf')