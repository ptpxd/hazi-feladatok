def mondat():
    print("Házi feladat")
    #
    #
    #
    print("\nAdjon meg egy mondatot: ")
    mondat = input()
    betuk = {}
    for i in mondat:
        if i in betuk:
            betuk[i] += 1
        else:
            betuk[i] = 1
    print("Betűk gyakorisága: ", str(betuk))
    print("Fordítva: ", mondat[::-1])
    print("Listába rendezve szavanként: ", mondat.split(' '))
    #
    #
    #
if __name__ == "__main__":
    mondat()