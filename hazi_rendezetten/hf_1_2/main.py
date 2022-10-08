print("Házi feladat")
#
#
#
print("\nAdjon meg egy mondatot:")
mondat = input()
betuk = {}
for i in mondat:
    if i in betuk:
        betuk[i] += 1
    else:
        betuk[i] = 1
print("Betűk gyakorisága: ",str(betuk))
print("Fordítva: ",mondat[::-1])
print("Listába rendezve szavanként: ",mondat.split(' '))
#
#
#
print("\nAdjon meg egy számot és egy mértékegységet (cm/inch)!:")
print("szám >")
szam = input()
print("mértékegység >")
mertekegyseg = input()
if mertekegyseg == "cm":
    print(2.54*float(szam)," inches")
elif mertekegyseg == "inch":
    print(0.393700787*float(szam)," centimeters")
else:
    print("Not correct unit!")