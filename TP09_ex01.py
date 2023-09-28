import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Prog(App):
    def build(self):
        box = BoxLayout(orientation = "vertical")
        self.lbl1 = Label(text="Ola", font_size= "50")
        self.lbl2 = Label(text="Mundo", font_size= "50")

        self.btn = Button(text="Trocar", font_size = "40", color = [1,1,1,1],
                          background_color = [0.5,1,0.5,1])
        self.btn.on_press = self.apertou

        box.add_widget(self.lbl1)
        box.add_widget(self.lbl2)
        box.add_widget(self.btn)

        return box

    def apertou(self):
        lbltest = self.lbl1.text
        self.lbl1.text = self.lbl2.text
        self.lbl2.text = lbltest

Prog().run()
