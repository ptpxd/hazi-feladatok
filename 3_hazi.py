print("Adja meg a háromszög három oldalát cm -ben:")
a_oldal = input("a: ")
b_oldal = input("b: ")
c_oldal = input("c: ")
oldalak = {a_oldal, b_oldal, c_oldal}
legnagyobb_oldal = int(max(oldalak))
if int(legnagyobb_oldal) > int(a_oldal) + int(b_oldal) + int(c_oldal) - int(legnagyobb_oldal):
    print("A", a_oldal,",", b_oldal, "és", c_oldal, "háromszög szerkeszthető.")
else:
    print("A", a_oldal, ",", b_oldal, "és", c_oldal, "háromszög NEM szerkeszthető.")