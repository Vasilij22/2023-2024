import PySimpleGUI as psg

class info():
    def __init__(self,veids, modelis, cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena

    def apskate(self):
        print(self.modelis)
        print(self.cena)
        print(self.veids)

    def laboshana(self, veids, modelis,cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena
    def saglabsana(self):
        with open('sastavdalas.txt','w', encoding="utf=8") as fails:
            fails.write("-Personālā datora sastāvdaļas-\n")
            fails.write(f"Veids: {self.veids}\n")
            fails.write(f"Modelis: {self.modelis}\n")
            fails.write(f"Cena: {self.cena} EUR\n")

jauns = info("RAM", 'Corsair Vengeance LPX 16GB',99.99)
jauns.apskate()
jauns.saglabsana()

psg.theme('darkamber')
logs = [
            [psg.Text('Sastavdalas')],
            [psg.Text('Veids',psg.InputText())],
            [psg.Text('Modelis',psg.InputText())],
            [psg.Text('Cena',psg.InputText())]
          
          ]

logs2 = [[psg.Text('Redigešana')]]

loguGruppa = [
    psg.TabGroup(
        [
            [
                psg.Tab('Datu ievade',logs),
                psg.Tab('Datu redigešana',logs2)
            ]
        ]
    ),
    psg.Button('Aizvert')
]
window = psg.Window('Datora datnes',loguGruppa)

while True:
    event,values = window.read()
  
    if event in (psg.WIN_CLOSED,'Aizvert'):
        break

window.close()
