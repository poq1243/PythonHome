from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition

class CustomScreen(Screen):
    def __init__(self, **kwargs):
        super(CustomScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text=self.name, font_size=50))

        # Add another layout to handle the navigation
        # and set the height of navigation to 20%
        # of the CustomScreen
        navig = BoxLayout(size_hint_y=0.1)

        # Create buttons with a custom text
        prev = Button(text='Previous')
        next = Button(text='Next')

        # Bind to 'on_relase' events of buttons
        prev.bind(on_release=self.switch_prev)
        next.bind(on_release=self.switch_next)

        # Add buttons to navigation
        # and the navigation to layout
        navig.add_widget(prev)
        navig.add_widget(next)
        layout.add_widget(navig)

        # And add the layout to the screen
        self.add_widget(layout)

    def switch_prev(self, *args):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = self.manager.previous()

    def switch_next(self, *args):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = self.manager.next()

class ScreenManagerApp(App):
    def build(self):
        root = ScreenManager()

        for x in range(4):
            root.add_widget(CustomScreen(name='Screen %d' % x))

        return root

if __name__ == '__main__':
    ScreenManagerApp().run()
