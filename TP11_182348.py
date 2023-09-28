import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Tela(BoxLayout):
    pass

class Calc02(App):
    def build(self):
        return Tela()
            
    def analisar01(self,TBCM1,TBM1,TBKM1):
        if(TBCM1.state == "down"):
            self.CMcheck = True
            self.Mcheck = False
            self.KMcheck = False
        
        elif(TBM1.state == "down"):
            self.CMcheck = False
            self.Mcheck = True
            self.KMcheck = False

        elif(TBKM1.state == "down"):
            self.CMcheck = False
            self.Mcheck = False
            self.KMcheck = True
    
            
    def analisar02(self,TBCM2,TBM2,TBKM2):
       if(TBCM2.state == "down"):
           self.CMcheck2 = True
           self.Mcheck2 = False
           self.KMcheck2 = False
        
       elif(TBM2.state == "down"):
           self.CMcheck2 = False
           self.Mcheck2 = True
           self.KMcheck2 = False

       elif(TBKM2.state == "down"):
           self.CMcheck2 = False
           self.Mcheck2 = False
           self.KMcheck2 = True

    def Calculo(self,texto,LBres):
        Valor = int(texto.text)
        
        if(self.CMcheck and self.CMcheck2):
            LBres.text = str(Valor)
            
        elif(self.Mcheck and self.Mcheck2):
            LBres.text = str(Valor)

        elif(self.KMcheck and self.KMcheck2):
            LBres.text = str(Valor)
            

        elif(self.CMcheck and self.Mcheck2):
            Res = Valor / 100
            LBres.text = str(Res)

        elif(self.CMcheck and self.KMcheck2):
            Res = Valor / 100000
            LBres.text = str(Res)

            

        elif(self.Mcheck and self.KMcheck2):
            Res = Valor / 1000
            LBres.text = str(Res)

        elif(self.Mcheck and self.CMcheck2):
            Res = Valor * 100
            LBres.text = str(Res)



        elif(self.KMcheck and self.CMcheck2):
            Res = Valor * 100000
            LBres.text = str(Res)

        elif(self.KMcheck and self.Mcheck2):
            Res = Valor * 1000
            LBres.text = str(Res)
       

        
Calc02().run()
