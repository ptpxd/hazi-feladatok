def buborek(x):
    n = len(x)
    for k in range(0, n):
        for i in range (1, n-k):
            if x[i-1] > x[i]:
                x[i],x[i-1] = x[i-1],x[i]
    return x

def main():
    lista = [54, 76, 23, 45, 21, 5, 67, 22, 12, 64, 26, 59, 82, 99]
    print(buborek(lista))

if __name__ == "__main__":
    main()