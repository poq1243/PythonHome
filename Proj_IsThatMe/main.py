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
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.storage.jsonstore import JsonStore
from kivy.uix.scrollview import ScrollView

db = JsonStore("tasks.json")

class Participants_num(Screen):
    def Value_save(self):
        self.manager.transition = NoTransition()
        db.put('game1', pnum=self.ids.part_num.text)

        for i in range(int(self.ids.part_num.text)):
            MkAnswerScreen()
            print(i)

class MkAnswerScreen(ScreenManager):
    def mkscreen(self):
        answerscreen = self.add_widget(AnswerScreen)
        return answerscreen

class Participants_input(Screen):
    def on_pre_enter(self):
        self.row = int(db.get('game1')['pnum'])
        box = BoxLayout(orientation = 'vertical')
        gly = GridLayout(cols = 3, padding = 10, spacing = 10, row_default_height = 30)
        btn = Button(text='Start')
        btn.bind(on_press=self.switch_start)

        label_order = Label(text='order')
        label_name = Label(text = 'Name')
        label_contact = Label(text = 'Contact')
        gly.add_widget(label_order)
        gly.add_widget(label_name)
        gly.add_widget(label_contact)

        for i in range(1, self.row+1):
            gly.add_widget(Label(text='{}'.format(i)))
            globals()['self.part_name_{}'.format(i)] = TextInput(multiline = False)
            globals()['self.part_contact_{}'.format(i)] = TextInput(multiline = False)
            gly.add_widget(globals()['self.part_name_{}'.format(i)])
            gly.add_widget(globals()['self.part_contact_{}'.format(i)])

        box.add_widget(gly)
        box.add_widget(btn)

        self.add_widget(box)

    def switch_start(self, *args):
        for i in range(1, self.row+1):
            temp_name = globals()['self.part_name_{}'.format(i)]
            temp_contact = globals()['self.part_contact_{}'.format(i)]
            db.put('player{}'.format(i), name = temp_name.text, contact = temp_contact.text)

        self.manager.transition = NoTransition()
        self.manager.current = self.manager.next()



class AnswerScreen(Screen):
    def __init__(self, **kwargs):
        super(AnswerScreen, self).__init__(**kwargs)
        box = BoxLayout(orientation='vertical')
        ans = TextInput()
        btn_next = Button(text='Next')
        btn_next.bind(on_press=self.switch_next)

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
        box.add_widget(btn_next)
        self.add_widget(box)



    def switch_next(self, *args):
        self.manager.transition = NoTransition()
        self.manager.current = self.manager.next()


class IsthatmeApp(App):
    def build(self):
        Window.clearcolor = (0.6, 0.6, 0.6, 1)

        root = ScreenManager()
        root.add_widget(Participants_num(name='Pnum'))
        root.add_widget(Participants_input(name='Pinput'))

        return root

if __name__ == '__main__':
    IsthatmeApp().run()

