from time import strftime

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.utils import get_color_from_hex

#윈도우 설정
Window.size = (550,350)
Window.clearcolor = get_color_from_hex('#333300')

class ClockApp(App):
    sw_seconds = 0
    started = False

    def update_clock(self, nap):
        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')

    def on_start(self):
        Clock.schedule_interval(self.update_clock, 1)
        Clock.schedule_interval(self.update, 0.01)

    def start_stop(self):
        self.root.ids.start_stop.text = ('Start'
                                         if self.started else 'Stop')
        self.started = not self.started
        print(self.started)
        print(self.sw_seconds)

    def reset(self):
        if self.started:
            self.root.ids.start_stop.text = 'Start'
            self.started = False
        self.sw_seconds = 0

    def update(self, nap):
        if self.started:
            self.sw_seconds += nap
        minutes, seconds = divmod(self.sw_seconds, 60)
        self.root.ids.stopwatch.text = (
            'Timer : %02d: %02d.[size=40]%02d[/size]'%
            (int(minutes),int(seconds),
             int(seconds * 100 % 100))
        )

if __name__ == '__main__':
    ClockApp().run()

LabelBase.register(name = 'Roboto',
                   fn_regular='./font/Roboto-Thin.ttf',
                   fn_bold='./font/Roboto-Medium.ttf')