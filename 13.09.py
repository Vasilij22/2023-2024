import PySimpleGUI as psg

class Sastavdala():
    #Konstruktora izveide
    def __init__(self,veids,modelis,cena):
        self.veids = veids
        self.modelis = modelis
        self.cena= cena
    #Datu izveda
    def apskate(self):
        print(self.veids)
        print(self.modelis)
        print(self.cena)
    #Datu labosana    
    def labosana(self,veids,modelis,cena):
        self.veids = veids
        self.modelis = modelis
        self.cena= cena
    #Datu saglabašana
    def saglabat(self):
        with open('sastavdalas.txt','w',encoding="utf-8") as fails:
            fails.write(self.modelis)
            fails.write("Veids",)

jauns = Sastavdala("RAM","RAM Corsair Vengeance LPX 16GB", 99.99)

jauns.apskate()
jauns.saglabat()

psg.theme('DarkAmber')
layout = [
    [psg.Text('Komponentes')]
    [psg.Text('Veids')]
    ]

layout2 = [[psg.Text('Redegešana')]]

loguGruppa = [
    psg.TabGroup(
        [
            [
                psg.Tab('datu ievade')
            ]
        ]
    )
]
