from vinkki import Vinkki

def main():
    
    def viesti():
        print ("Hello Codefairy!")

    viesti()

    vinkki = Vinkki()

    print(vinkki.vastaus())

    print(vinkki.huomenta())

if __name__ == "__main__":
    main()
