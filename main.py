from typing import Text
from kivy.config import Config
Config.set("graphics", "width", "570")
Config.set("graphics", "height", "430")

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from random import random
from kivy.uix.button import Button

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            color = random(), random(), random()
            d = 30
            Color(*color, mode="hsv")
            Ellipse(pos= (touch.x - d/2, touch.y - d/2), size=(d,d))
            touch.ud["line"] = Line(points = (touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud["line"].points += [touch.x, touch.y]

class MyPaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()
        btn = Button(text="Clear", size=(100, 50))
        btn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(btn)

        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()

if __name__ == "__main__":
    MyPaintApp().run()