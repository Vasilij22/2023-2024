import PySimpleGUI as psg

class info():
    def __init__(self,Produkta_kategorija,Produkta_nosaukums,Tehniskie_raksturojumi,Nomas_cena_dienā,Produkts_pieejams,Nomnieks_vārds,Nomnieks_uzvārds,Nomnieks_p_k,Nomnieks_tel_numurs,Nomas_sākuma_datums,Nomas_beigu_datums):
        self.Produkta_kategorija = Produkta_kategorija
        self.Produkta_nosaukums = Produkta_nosaukums
        self.Tehniskie_raksturojumi = Tehniskie_raksturojumi
        self.Nomas_cena_dienā = Nomas_cena_dienā
        self.Produkts_pieejams = Produkts_pieejams
        self.Nomnieks_vārds = Nomnieks_vārds
        self.Nomnieks_uzvārds = Nomnieks_uzvārds
        self.Nomnieks_p_k = Nomnieks_p_k
        self.Nomnieks_tel_numurs = Nomnieks_tel_numurs
        self.Nomas_sākuma_datums = Nomas_sākuma_datums
        self.Nomas_beigu_datums = Nomas_beigu_datums

    def apskate(self):
        print(self.Produkta_kategorija)
        print(self.Produkta_nosaukums)
        print(self.Tehniskie_raksturojumi)
        print(self.Nomas_cena_dienā)
        print(self.Produkts_pieejams)
        print(self.Nomnieks_vārds)
        print(self.Nomnieks_uzvārds)
        print(self.Nomnieks_p_k)
        print(self.Nomnieks_tel_numurs)
        print(self.Nomas_sākuma_datums)
        print(self.Nomas_beigu_datums)

    def saglabsana1(self):
        with open('Produktu info.txt','w', encoding="utf=8") as fails:
            fails.write("-Produktu informacija-\n")
            fails.write(f"Produkta_kategorija: {self.Produkta_kategorija}\n")
            fails.write(f"Produkta_nosaukums: {self.Produkta_nosaukums}\n")
            fails.write(f"Tehniskie_raksturojumi: {self.Tehniskie_raksturojumi} \n")
            fails.write(f"Produkts_pieejams: {self.Produkts_pieejams} \n")

    def saglabsana2(self):
        with open('Noma info.txt','w', encoding="utf=8") as fails:
            fails.write("-Nomas informacija-\n")
            fails.write(f"Nomnieks_vārds: {self.Nomnieks_vārds}\n")
            fails.write(f"Nomnieks_uzvārds: {self.Nomnieks_uzvārds}\n")
            fails.write(f"Nomnieks_p_k: {self.Nomnieks_p_k} \n")
            fails.write(f"Nomnieks_tel_numurs: {self.Nomnieks_tel_numurs} \n")
            fails.write(f"Nomas_sākuma_datums: {self.Nomas_sākuma_datums} \n")
            fails.write(f"Nomas_beigu_datums: {self.Nomas_beigu_datums} \n")
            fails.write(f"Nomas_cena_dienā: {self.Nomas_cena_dienā} \n")

psg.theme('Dark blue')

logi = [
    [psg.Text('Produktu Info')],
    [psg.Text('Produkta_kategorija'), psg.InputText()],
    [psg.Text('Produkta_nosaukums'), psg.InputText()],
    [psg.Text('Tehniskie_raksturojumi'), psg.InputText()],
    [psg.Text('Produkts_pieejams'), psg.InputText()],
    [psg.Button('Saglabat')]
]

logi2 = [
    [psg.Text('Nomnieka Info')],
    [psg.Text('Nomnieks_vārds'), psg.InputText()],
    [psg.Text('Nomnieks_uzvārds'), psg.InputText()],
    [psg.Text('Nomnieks_p_k'), psg.InputText()],
    [psg.Text('Nomnieks_tel_numurs'), psg.InputText()],
    [psg.Text('Nomas_sākuma_datums'), psg.InputText()],
    [psg.Text('Nomas_beigu_datums'), psg.InputText()],
    [psg.Text('Nomas_cena_dienā'), psg.InputText()],
    [psg.Button('Saglabat1')]
]

logugruppa = [[
    psg.TabGroup(
        [
            [
                psg.Tab('Produkta ievade', logi),
                psg.Tab('Nomas ievade',logi2)
            ]
        ]
    ),
    [psg.Button('Aizvert')]
]]

window = psg.Window('Window tittle', logugruppa)

while True:
    event, values = window.read()

    if event == 'Saglabat':
        print(values)
        Produkta_kategorija = values[0]
        Produkta_nosaukums = values[1]
        Tehniskie_raksturojumi = values[2]
        Produkts_pieejams = values[3]
        Nomas_cena_dienā = values[4]
        Nomnieks_vārds = values[5]
        Nomnieks_uzvārds = values[6]
        Nomnieks_p_k = values[7]
        Nomnieks_tel_numurs = values[8]
        Nomas_sākuma_datums = values[9]
        Nomas_beigu_datums = values[10]
        jauns = info(Produkta_kategorija,Produkta_nosaukums,Tehniskie_raksturojumi,Nomas_cena_dienā,Produkts_pieejams,Nomnieks_vārds,Nomnieks_uzvārds,Nomnieks_p_k,Nomnieks_tel_numurs,Nomas_sākuma_datums,Nomas_beigu_datums)
        jauns.saglabsana1()

    if event == 'Saglabat1':
        print(values)
        Produkta_kategorija = values[0]
        Produkta_nosaukums = values[1]
        Tehniskie_raksturojumi = values[2]
        Produkts_pieejams = values[3]
        Nomas_cena_dienā = values[4]
        Nomnieks_vārds = values[5]
        Nomnieks_uzvārds = values[6]
        Nomnieks_p_k = values[7]
        Nomnieks_tel_numurs = values[8]
        Nomas_sākuma_datums = values[9]
        Nomas_beigu_datums = values[10]
        jauns = info(Produkta_kategorija,Produkta_nosaukums,Tehniskie_raksturojumi,Nomas_cena_dienā,Produkts_pieejams,Nomnieks_vārds,Nomnieks_uzvārds,Nomnieks_p_k,Nomnieks_tel_numurs,Nomas_sākuma_datums,Nomas_beigu_datums)
        jauns.saglabsana2()

    if event == psg.WIN_CLOSED or event  == 'Close':
        break

window.close
