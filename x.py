class Zwierze:
    def __init__(self, waga, prędkość, zwierze, imie) -> None:
        self.waga = waga
        self.prędkość = prędkość
        self.zwierze = zwierze
        self.imie = imie
        pass
    def wyświetl_inf_zwierze(self):
        print("=="*25,f"\nZwierze {self.zwierze} \nImie {self.imie} \nWaga {self.waga} \nPrędkość {self.prędkość}\n","=="*25)

kot = Zwierze("4kg","48 km/h","kot","Szyszka")
kot.wyświetl_inf_zwierze()
pies = Zwierze("20kg","63 km/h","pies","Biszkopt" )
pies.wyświetl_inf_zwierze()
mysz = Zwierze("30g","20m/min","mysz","Szczurek")
mysz.wyświetl_inf_zwierze()


class Pierwiastek:
    def __init__(self, pierwiastek, liczba_atomowa, liczba_masowa, grupa, okres, rok_odkrycia) -> None:
        self.pierwiastek = pierwiastek
        self.liczba_atomowa = liczba_atomowa
        self.liczba_masowa = liczba_masowa
        self.grupa = grupa
        self.okres = okres
        self.rok_odkrycia = rok_odkrycia
        pass

    def wyświetl_inf_pierwiastki(self):
        print("=="*25,f"\nPierwiastek {self.pierwiastek} \nLiczba atomowa {self.liczba_atomowa} \nLiczba masowa {self.liczba_masowa} \nGrupa {self.grupa} \nOkres {self.okres} \nRok odkrycia {self.rok_odkrycia}\n","=="*25)

azot = Pierwiastek("azot","7","14,01u","15","2","1772r")
azot.wyświetl_inf_pierwiastki()
magnez = Pierwiastek("magnez","12","24,31u","2","3","1808r")
magnez.wyświetl_inf_pierwiastki()
bar = Pierwiastek("bar","56","137,33u","2","6","1774r")
bar.wyświetl_inf_pierwiastki()