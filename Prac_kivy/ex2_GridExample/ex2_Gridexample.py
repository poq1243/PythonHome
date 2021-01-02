from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

fontName = 'NanumGothicCoding-Bold.ttf'
class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.padding = 10
        self.spacing = 10

        self.cols = 2
        self.add_widget(Label(text='사용자명: ', font_name=fontName,
                              font_size=40))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='비밀번호: ', font_name=fontName,
                              font_size=40))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__=='__main__':
    MyApp().run()