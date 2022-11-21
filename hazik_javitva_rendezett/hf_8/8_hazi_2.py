def binaris(x, y):
    n = len(x)
    also = 0
    felso = n-1
    while also <= felso:
        k = (felso + also) // 2
        if y < x[k]:
            felso = k-1
        elif y > x[k]:
            also = k+1
        else:
            kimenet = True, k
            break
    else:
        kimenet = False

    return int(k)

def main():
    lista = [2, 5, 6, 8, 13, 32, 42, 50, 53, 62, 66, 70, 80, 89, 91]
    keresett = 70
    print(f"A {keresett} -t a {binaris(lista, keresett) + 1}. lépésben találta meg.")

if __name__ == "__main__":
    main()