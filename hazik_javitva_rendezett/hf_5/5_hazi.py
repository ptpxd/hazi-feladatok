class Team:
    def __init__(self, nev, projekt, munkakor):
        self._nev = nev
        self._projekt = projekt
        self._munkakor = munkakor

    def __str__(self):
        return self._nev + " a " + self._projekt + " -en dolgzik " + self._munkakor + " szerepkörben."

    def __eq__(self, masik_projekt):
        return "\n" + self._nev + " és " + masik_projekt._nev + " egy projekten dolgoznak."

nev1 = Team("Ricsi", "SolArch", "FrontEnd")
nev2 = Team("Angéla", "ZerTeng", "Tesztelő")
nev3 = Team("Peti", "KefERP", "Backend")
nev4 = Team("Éva", "KefERP", "FrontEnd")
nevek = [nev1, nev2, nev3, nev4]

for i in nevek:
    print("-- Developer létrehozva. --")
    print(i)

print(nev3 == nev4)