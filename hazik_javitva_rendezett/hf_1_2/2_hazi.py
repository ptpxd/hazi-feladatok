def  valtas():
    print("\nAdjon meg egy számot és egy mértékegységet (cm/inch)!:")
    print("szám > ")
    szam = input()
    print("mértékegység > ")
    mertekegyseg = input()
    if mertekegyseg == "cm":
        print(2.54 * float(szam), " inches")
    elif mertekegyseg == "inch":
        print(0.393700787 * float(szam), " centimeters")
    else:
        print("Not correct unit!")

if __name__ == "__main__":
    valtas()