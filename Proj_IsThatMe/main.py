import kivy

kivy.require('2.0.0')

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

class Participants_num(Screen):
    pass
    def Value_save(self):
        f = open('./Data.txt', 'w')
        f.write(self.ids.part_num.text)
        f.close()


class Participants_input(Screen):
    f = open('./Data.txt', 'r')
    part_num = f.readline()
    f.close()
    def test(self):
        print(self.part_num)

    pass

class Answer_input(Screen):
    def __init__(self, **kwargs):
        super(Answer_input, self).__init__(**kwargs)
        box = BoxLayout(orientation='vertical')
        ans = TextInput()

        dropdown = DropDown()
        for index in range(2):
            btn = Button(text='Value %d' % index, size_hint_y=None, height=30, width=self.width)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))

            dropdown.add_widget(btn)

        mainbutton = Button(text='Value 1', size_hint=(1,None), height=30, width=self.width)
        mainbutton.bind(on_release=dropdown.open)

        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton,'text',x))

        box.add_widget(mainbutton)
        box.add_widget(ans)
        self.add_widget(box)


class IsthatmeApp(App):
    def build(self):
        Window.clearcolor = (0.6, 0.6, 0.6, 1)
        root = ScreenManager()
        root.add_widget(Participants_num(name='Pnum'))
        root.add_widget(Participants_input(name='Pinput'))
        root.add_widget(Answer_input(name='answer'))
        return root


if __name__ == '__main__':
    IsthatmeApp().run()

