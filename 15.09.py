import PySimpleGUI as psg

class info():
    def __init__(self,veids, modelis, cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena

    def apskate(self):
        print(self.veids)
        print(self.modelis)
        print(self.cena)

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

psg.theme('darkamber')
logs = [
            [psg.Text('Sastavdalas')],
            [psg.Text('Veids'),psg.InputText()],
            [psg.Text('Modelis'),psg.InputText()],
            [psg.Text('Cena'),psg.InputText()],
            [psg.Button('Saglabat')]
          
          ]

logs2 = [

            [psg.Text('Redigešana')],
            [psg.Text('Veids'),psg.InputText()],
            [psg.Text('Modelis'),psg.InputText()],
            [psg.Text('Cena'),psg.InputText()],
            [psg.Button('Redeget')]
    
    
    ]

loguGruppa = [[
    psg.TabGroup(
        [
            [
                psg.Tab('Datu ievade',logs),
                psg.Tab('Datu redigešana',logs2)
            ]
        ]
    ),
    psg.Button('Aizvert'),
    psg.Button('Datu apskate')
    

]]

window = psg.Window('Datora datnes',loguGruppa)

while True:
    event,values = window.read() #Nolasa ievaditas vertibas un darbibas
    #Apgalvojums
    if event == 'Saglabat':
        print(values)
        veids = values[0]
        modelis = values[1]
        cena = values[2]
        jauns = info(veids,modelis,cena)
        jauns.saglabsana()

    if event == 'Redeget':
        print(values)
        veids = values[3]
        modelis = values[4]
        cena = values[5]
        jauns = info(veids,modelis,cena)
        jauns.saglabsana()
    if event == 'Datu apskate':
        psg.theme("BlueMono")
        logs3 = [
            [psg.Text("esošas komponentes")],
            [psg.Text("Veids:" +values[0] )]
            
            
            ]
        window = psg.Window(logs3)
        event,values = window.read()
    
    
    if event in (psg.WIN_CLOSED,'Aizvert'):
        break

window.close()
