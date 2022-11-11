def fajl():
    i = 0
    kihagyas = ['a', 'e', 'ö', 'ü', 'ó', 'ő', 'ú', 'ű', 'é', 'á', 'u', 'o', 'i', 'í', '.', '!', '?', ',', '"', 'A', 'E', 'U', 'I', 'O', 'Ő', 'Ú', 'Ű', 'Ö', 'Ü', 'Ó', 'É', 'Á', 'Í']
    szoveg = ""

    with open ("hazi.txt", 'r', encoding="utf-8") as f, open ("hazi_Szerkesztett.txt", 'w', encoding="utf-8") as a:
        for sor in f:
            if i%3 == 0 and i/3 != 0:
                if sor.strip():
                    szoveg += sor
            i += 1
        for karakter in szoveg:
            if karakter in kihagyas:
                szoveg = szoveg.replace(karakter, '')
        a.write(szoveg)
if __name__ == "__main__":
    fajl()