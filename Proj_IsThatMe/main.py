from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition


class Participants_num(Screen):
    part_num = ObjectProperty(None)
    def put_pnum(self):
        global pnum
        pnum=int(self.part_num.text)


class Participants_input(Screen):
    def check_status(self):
        print('text input text is: %d' % pnum)



class IsthatmeApp(App):
    def build(self):
        root = ScreenManager()
        root.add_widget(Participants_num(name='Pnum'))
        root.add_widget(Participants_input(name='Pinput'))

        return root


if __name__ == '__main__':
    IsthatmeApp().run()

LabelBase.register(name = 'Roboto',
                   fn_regular='./font/Roboto-Thin.ttf',
                   fn_bold='./font/Roboto-Medium.ttf')