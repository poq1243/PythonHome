from os.path import dirname
from os.path import join
from kivy.app import App
from kivy.lang import Builder


class TestApp(App):
    def build(self):
        return Builder.load_file(join(dirname(__file__), 'noname.kv'))

def main():
    TestApp().run()

if __name__ == "__main__":
    main()