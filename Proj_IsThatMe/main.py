import kivy

kivy.require('2.0.0')

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition


class Participants_num(Screen):
    def __init__(self, **kwargs):
        super(Participants_num, self).__init__(**kwargs)
        box = BoxLayout(orientation='vertical')

        lbl1 = Label(text='How many people?')
        self.txtin = TextInput(multiline=False)
        btn = Button(text='Start')

        btn.bind(on_release=self.switch_btn)

        box.add_widget(lbl1)
        box.add_widget(self.txtin)
        box.add_widget(btn)

        self.add_widget(box)

    def switch_btn(self, *args):
        global pnum
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'Pinput'
        pnum=int(self.txtin.text)



class Participants_input(Screen):
    def __init__(self, **kwargs):
        super(Participants_input, self).__init__(**kwargs)
        box = BoxLayout(orientation='vertical')
        glayout = GridLayout(rows=3, cols=2)

        lbl1 = Label(text='Name')
        lbl2 = Label(text='Number')
        name1 = TextInput(multiline=False)
        name2 = TextInput(multiline=False)
        num1 = TextInput(multiline=False)
        num2 = TextInput(multiline=False)
        btn = Button(text='Next')

        btn.bind(on_release=self.switch_btn)

        glayout.add_widget(lbl1)
        glayout.add_widget(lbl2)
        glayout.add_widget(name1)
        glayout.add_widget(name2)
        glayout.add_widget(num1)
        glayout.add_widget(num2)

        box.add_widget(glayout)
        box.add_widget(btn)

        self.add_widget(box)

    def switch_btn(self, *args):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'answer'


class Answer_input(Screen):
    def __init__(self, **kwargs):
        super(Answer_input, self).__init__(**kwargs)
        box=BoxLayout(orientation='vertical')
        ans=TextInput()

        dropdown = DropDown()
        for index in range(2):
            btn = Button(text='Value %d' % index, size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))

            dropdown.add_widget(btn)

        mainbutton = Button(text='Value 1', size_hint=(None,None), height=30)
        mainbutton.bind(on_release=dropdown.open)

        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton,'text',x))

        box.add_widget(mainbutton)
        box.add_widget(ans)
        self.add_widget(box)







class IsthatmeApp(App):
    def build(self):
        root = ScreenManager()
        #root.add_widget(Participants_num(name='Pnum'))
        root.add_widget(Participants_input(name='Pinput'))
        root.add_widget(Answer_input(name='answer'))

        return root


if __name__ == '__main__':
    IsthatmeApp().run()

LabelBase.register(name = 'Roboto',
                   fn_regular='./font/Roboto-Thin.ttf',
                   fn_bold='./font/Roboto-Medium.ttf')