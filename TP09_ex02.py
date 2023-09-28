import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class Prog(App):
    def build(self):

        #Criação dos Box
        box1 = BoxLayout(orientation = "vertical")
        box2 = BoxLayout(orientation = "horizontal")
        box3 = BoxLayout(orientation = "vertical") 
        box4 = BoxLayout(orientation = "horizontal") 

        #Labels:
        
        self.lbl1 = Label(text="0", font_size= "50")
        self.lbl2 = Label(text="1", font_size= "50")

        #Buttons

        self.btn1 = Button(text="Incrementar", font_size = "25", color = [1,1,1,1], background_color = [0.5,1,0.5,1])
        self.btn2 = Button(text="Descrementar", font_size = "25", color = [1,1,1,1], background_color = [0.5,1,0.5,1])
        self.btn3 = Button(text="Zerar", font_size = "40", color = [1,1,1,1], background_color = [0.5,1,0.5,1])
        self.btn4 = Button(text="+", font_size = "40", color = [1,1,1,1], background_color = [0.5,1,0.5,1])
        self.btn5 = Button(text="-", font_size = "40", color = [1,1,1,1], background_color = [0.5,1,0.5,1])

        #On_Press
        self.btn1.on_press = self.Mais
        self.btn2.on_press = self.Menos
        self.btn3.on_press = self.Zerar
        self.btn4.on_press = self.Max
        self.btn5.on_press = self.Min
        


        #Ordem dos Boxs

        box1.add_widget(self.lbl1)
        box1.add_widget(box2)

        box2.add_widget(self.btn1)
        box2.add_widget(self.btn2)
        box2.add_widget(self.btn3)
        box2.add_widget(box3)

        box3.add_widget(box4)
        box3.add_widget(self.lbl2)

        box4.add_widget(self.btn4)
        box4.add_widget(self.btn5)

        return box1

    def Mais(self):
        X = int(self.lbl2.text)
        Y = int(self.lbl1.text)
        self.lbl1.text = str(Y+X)

    def Menos(self):
        X = int(self.lbl2.text)
        Y = int(self.lbl1.text)
        if self.lbl1.text != '0':
            self.lbl1.text = str(Y-X)
            
    def Zerar(self):
        self.lbl1.text = "0"

    def Max(self):
        X = int(self.lbl2.text)
        Y = X + 1
        self.lbl2.text = str(Y)

    def Min(self):
        X = int(self.lbl2.text)
        if self.lbl2.text != '1':
            Y = X - 1
            self.lbl2.text = str(Y)
            

Prog().run()
