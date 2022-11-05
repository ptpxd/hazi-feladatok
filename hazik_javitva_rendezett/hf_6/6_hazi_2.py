def main():
    bekeres = input("Adj meg egy szót vagy egy mondatot! ")
    palindrom = bekeres[::-1]
    print(palindrom)
    if palindrom == bekeres:
        print("A megadott szó/mondat palindrom.")
    else:
        print("A megadott szó/mondat nem palindrom.")

if __name__ == "__main__":
    main()