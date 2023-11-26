print("Witaj nowy graczu! Zapoznaj się z zasadami oraz poradami do naszej gry:\n 1.Co każdą walkę twoje życie oraz mana się regenerują \n 2.Pisz małymi literami nie używając polskich znaków \n 3.Uważnie czytaj dialogi bo mogą ci pomóc")
instrukcja = input("\nCzy zapoznaleś sie z zadasami? ")
if instrukcja == "tak":
    print(" W takim razie zaczynamy")
else:
    instrukcja_2 = input("Może jednak chcesz zapozhnac sie z instrukcja? ")
    if instrukcja_2 == "tak":
        print("Dobrze, specjalnie dla ciebie podróżniku przytocze te zasady jeszcze raz...\n 1.Co każdą walkę twoje życie oraz mana się regenerują \n 2.Pisz małymi literami nie używając polskich znaków \n 3.Uważnie czytaj dialogi bo mogą ci pomóc")
    else:
        print("No cóż twoja sprawa..")
imie = input(" Jak chcesz się nazywać? ")

print("Witaj,", imie+"!")
print("Wybierz swoje świecidełko mocy!; \n 1.świecidełko światła \n 2.świecidełko mroku \n 3.świecidełko wody \n 4.świecidełko ognia")
świecidełko = int(input())
twoj_wybor_swiecidelka = 0
if świecidełko == 1:
    print("Wybrałeś świecidełko światła!")
    twoj_wybor_swiecidelka = 1
elif świecidełko == 2:
    print("Wybrałeś świecidełko mroku")
    twoj_wybor_swiecidelka = 2
elif świecidełko == 3:
    print("Wybrałeś świecidełko wody")
    twoj_wybor_swiecidelka = 3
elif świecidełko == 4:
    print("Wybrałeś świecidełko ognia")
    twoj_wybor_swiecidelka = 4
else:
    print("Sayonara")
while twoj_wybor_swiecidelka == 0:
    break
potwierdzenie_wyboru = input("Czy jesteś pewien swojego wyboru? \n Tak/Nie ")
if potwierdzenie_wyboru == "tak":
    print("A więc zacznijmy twoją przygodę!")
elif potwierdzenie_wyboru == "nie":
    zmiana_swiecidelka = int(input("Na jakie świecidełko chcesz zmienić? "))
    if zmiana_swiecidelka == 1:
        print("A więc zacznijmy nasza przygodę")
        twoj_wybor_swiecidelka = 1
    elif zmiana_swiecidelka == 2:
        print("A więc zacznijmy nasza przygodę")
        twoj_wybor_swiecidelka = 2
    elif zmiana_swiecidelka == 3:
        print("A więc zacznijmy nasza przygodę")
        twoj_wybor_swiecidelka = 3
    elif zmiana_swiecidelka == 4:
        print("A więc zacznijmy nasza przygodę")
        twoj_wybor_swiecidelka = 4

goblin_zdrowie = 150
zdrowie_gracza = 100
mana_gracza = 75
def walka(świecidełko, potwor, mana, życie):
    while potwor > 0 and życie > 0:
        if świecidełko == 1:
            wybór_ataku_światło = input("Wybierz atak; \n E.oświecenie - 15HP \n Q.kula światła - 30HP \n P.podstawowy atak różdżką - 10HP \n ")
            if wybór_ataku_światło == "e":
                if mana < 3:
                    print("Masz za mało many")
                else:
                    mana += -3
                    potwor += -15
                    życie += -5
                    print(f" Potworowi zostało {potwor}HP \n Twoje życie {życie}HP \n Pozostała mana {mana}")
            elif wybór_ataku_światło == "q":
                if mana < 5:
                    print("Masz za mało many")
                else:
                    mana += -8
                    potwor += -30
                    życie += -5
                    print(f" Potworowi zostało {potwor}HP \n Twoje życie {życie}HP \n Pozostała mana {mana}")
            elif wybór_ataku_światło == "p":
                mana += 0
                potwor += -10
                życie += -5
                print(f" Potworowi zostało {potwor}HP \n Twoje życie {życie}HP \n Pozostała mana {mana}")
        if świecidełko == 2:
            wybór_ataku_mrok = input("Wybierz atak; \n E.zaćmienie - 15HP \n Q.kula cienia - 30HP \n P.podstawowy atak mieczem - 10HP \n ")
            if wybór_ataku_mrok == "e":
                if mana < 3:
                    print("Masz za mało many")
                else:
                    mana += -3
                    potwor += -15
                    życie += -5
                    print(f" Potworowi zostało {potwor}HP \n Twoje życie {życie}HP \n Pozostała mana {mana}")
            elif wybór_ataku_mrok == "q":
                if mana < 5:
                    print("Masz za mało many")
                else:
                    mana += -8
                    potwor += -30
                    życie += -5
                    print(f" Potworowi zostało {potwor}HP \n Twoje życie {życie}HP \n Pozostała mana {mana}")
            elif wybór_ataku_mrok == "p":
                mana += 0
                potwor += -10
                życie += -5
                print(f" Potworowi zostało {potwor}HP \n Twoje życie {życie}HP \n Pozostała mana {mana}")
        if świecidełko == 3:
            wybór_ataku_mrok = input("Wybierz atak; \n E.fala - 15HP \n Q.tsunami - 30HP \n P.podstawowy atak łukiem - 10HP \n ")
            if wybór_ataku_mrok == "e":
                if mana < 3:
                    print("Masz za mało many")
                else:
                    mana += -3
                    potwor += -15
                    życie += -5
                    print(f" Potworowi zostało {potwor}HP \n Twoje życie {życie}HP \n Pozostała mana {mana}")
            elif wybór_ataku_mrok == "q":
                if mana < 5:
                    print("Masz za mało many")
                else:
                    mana += -8
                    potwor += -30
                    życie += -5
                    print(f" Potworowi zostało {potwor}HP \n Twoje życie {życie}HP \n Pozostała mana {mana}")
            elif wybór_ataku_mrok == "p":
                mana += 0
                potwor += -10
                życie += -5
                print(f" Potworowi zostało {potwor}HP \n Twoje życie {życie}HP \n Pozostała mana {mana}")
        if świecidełko == 4:
            wybór_ataku_mrok = input("Wybierz atak; \n E.iskra - 15HP \n Q.lava - 30HP \n P.podstawowy atak włócznia - 10HP \n ")
            if wybór_ataku_mrok == "e":
                if mana < 3:
                    print("Masz za mało many")
                else:
                    mana += -3
                    potwor += -15
                    życie += -5
                    print(f" Potworowi zostało {potwor}HP \n Twoje życie {życie}HP \n Pozostała mana {mana}")
            elif wybór_ataku_mrok == "q":
                if mana < 5:
                    print("Masz za mało many")
                else:
                    mana += -8
                    potwor += -30
                    życie += -5
                    print(f" Potworowi zostało {potwor}HP \n Twoje życie {życie}HP \n Pozostała mana {mana}")
            elif wybór_ataku_mrok == "p":
                mana += 0
                potwor += -10
                życie += -5
                print(f" Potworowi zostało {potwor}HP \n Twoje życie {życie}HP \n Pozostała mana {mana}")
    while życie <= 0:
        print("Umarłeś")
        return
    if potwor <= 0 and życie > 0:
            print("Udało ci się pokonać potwora!")
            print(f"zostało ci {życie}HP i {mana}many")

print("Udajesz sie do zamku by spotkać Czarodzieja, jednak atakuje cie Goblin")

walka(twoj_wybor_swiecidelka, goblin_zdrowie, mana_gracza, zdrowie_gracza)

print("*wchodzisz do zamku*\n Czarodziej światła \nWitaj podróżniku jestem Czarodziejem światła! Potrzebujemy twojej pomocy w pokonaniu groźnego Smoka który grasuje w naszej krainie")
wybór_pomocy = input("Pomożesz nam go pokonać?" )
if wybór_pomocy == "tak":
        print("To wspaniale!")
elif wybór_pomocy == "nie":
    print("Chyba po coś zaczołeś grać w te grę? I tak mi pomożesz c:<")
else:
    pomoc = input("Możesz powtórzyć?")
    if pomoc == "tak":
        print("To wspaniale!")
    elif pomoc == "nie":
        print("Chyba po coś zaczołeś grać w te grę? I tak mi pomożesz c:<")

print(" Czarodziej światła \n*Za pomocą magi Czarodziej leczy cię do 100HP*\nAby udać się przez labirynt musisz podążac za pomocą tych wskazówek:")
print(" 2 razy w prawo, 100m na przód, lewo, 300m na przód, prawo ")
print("Teraz ruszaj bo mamy mało czasu")
wybór1 = input("2 razy w ... ")
if wybór1 == "prawo":
    print("Dobry wybór!")
else:
    print("Zły wybór, tracisz 30HP przez węże")
    zdrowie_gracza += -30
wybór2 = input("...m na przód ")
if wybór2 == "100":
    print("dokładnie tak!")
else:
    print("Zły wybór, tracisz 20HP przez kruka")
    zdrowie_gracza += -20
wybór3 = input("teraz w ... ")    
if wybór3 == "lewo":
    print("już połowa za nami!")
else:
    print("Zły wybór, tracisz 20HP przez pająka")
    zdrowie_gracza += -20
wybór4 = input("...m na przód ")
if wybór4 == "300":
    print("już ostatnia prosta")
else:
    print("Zły wybór, tracisz 20HP przez magmę")
    zdrowie_gracza += -20
    if zdrowie_gracza < 0:
        print("nie umiesz wydostać się z labiryntu... Umierasz")
wybor5 = input("na końcu skręć w ... ")    
if wybor5 == "prawo":
    print("Wydostałes się")
elif wybor5 == "lewo":
    print("Ciesz się że Carodziej zapomnaił o wyjściu z lewej strony.. bo utknałbyś tu na wielki")
    zdrowie_gracza += -10
    while zdrowie_gracza <= 0:
        print("Umierasz")
        break
else:
    print("Czarodziej teleportuje cię do wyjścia...")
    
        
print(f"Zostało ci {zdrowie_gracza}HP")
print("Na drodze napotykasz 3 wieźmy.\n Wiedźma Sara: \n Aby przejść musisz rozwiązać 3 zagadki. Na każdą zagadkę masz 3próby!Co każdą złą próbę tracisz 20many(oprócz 1)")
print(" Wiedźma Sara \nMoja zagadka dla ciebie to:")
próby_do_zagadki_1 = 2
próby_do_zagadki_2 = 2
próby_do_zagadki_3 = 3
mana = 0
zagadka_1 = input("Mama Kasi ma pięć córek. Jeśli imiona jej córek to odpowiednio Klara, Karolina, Klaudia, Kinga, to jakie będzie imię piątej córki? ")
while próby_do_zagadki_1 > 0:
    if zagadka_1 != "kasia":
        próby_do_zagadki_1 += -1
        mana += 20
        kolejna_szansa = input()
        zagadka_1 = kolejna_szansa
        print("Masz jeszcze szanse")
    elif zagadka_1 == "kasia":
        print("Gratulacje!")
        break
if próby_do_zagadki_1 == 0:
    print(f"zartowałam , nie masz juz szansy.\nOdpowiedź to kasia... masz {mana}many")
zagadka_2 = input(" Wiedźma Marta \nMoja zagadka:\nTen, kto mnie tworzy, nie potrzebuje mnie, kiedy to robi.\nTen, który mnie kupuje, nie potrzebuje mnie dla siebie.\nTen, kto mnie użyje, nie będzie o tym wiedział.\nCzym jestem?")
próby_do_zagadki_2 = 2
while próby_do_zagadki_2 > 0:
    if zagadka_2 != "trumna":
        próby_do_zagadki_2 += -1
        mana += 20
        kolejna_szansa2 = input()
        zagadka_2 = kolejna_szansa2
        print("Masz jeszcze szanse")
    elif zagadka_2 == "trumna":
        print("Gratulacje!")
        break
    if próby_do_zagadki_2 == 0:
        print(f"zartowałam , nie masz juz szansy.\nOdpowiedź to trumna... masz {mana}many")
zagadka_3 = input(" Wiedźma Sabina \nTym razem dostaniesz 4 próby\nJeśli mnie widzisz, ja widzę ciebie.\nJeśli się ruszysz, ja też się przeprowadzę.\nKiedy mnie dotykasz, ja dotykam ciebie.\nRobię wszystko, co ty, z wyjątkiem jednej rzeczy.\nBez względu na to, jak bardzo się staram, nigdy nie mogę mówić.\nCzym jestem? ")
próby_do_zagadki_3 = 2
while próby_do_zagadki_3 > 0:
    if zagadka_3 != "twoim odbiciem lustrzanym":
        próby_do_zagadki_3 += -1
        mana += 20
        kolejna_szansa3 = input()
        zagadka_3 = kolejna_szansa3
        print("Masz jeszcze szanse")
    elif zagadka_3 == "twoim odbiciem lustrzanym":
        print("Gratulacje!")
        break
    if próby_do_zagadki_3 == 0:
        print(f"zartowałam , nie masz juz szansy.\nOdpowiedź to twoim odbiciem lustrzanym... masz {mana_gracza - mana}many")
mana_gracza = mana_gracza - mana
print(f"W ostatecznym starciu bedziesz miał(co każdą walkę){zdrowie_gracza}HP i {mana_gracza}many")
print("Przechodzisz koło wiedźm i udajesz sie do jamy która jest za lasem")
print("Do wyboru masz 3 drogi:\n1.Prowadząca na plażę\n2.Prowadząca na polanę\n3.Prowadząca w góry")

nimfa_zycie = 200
krasnolud_zycie = 150
smok_zycie = 300
wybór_ścieszki = int(input("Którą drogą sie kierujesz? "))

if wybór_ścieszki == 1:
    print("znajdujesz na plaży Nimfę która wyzywa cie na pojedynek")
    walka(świecidełko, nimfa_zycie, mana_gracza, zdrowie_gracza)
    nowy_wybór_ścieszki = int(input("Musisz wybrać inną trasę: "))
    if nowy_wybór_ścieszki == 2:
        print("Napotykasz 3 krasnoludy które cię atakują")
        walka(świecidełko, krasnolud_zycie, mana_gracza, zdrowie_gracza)
        walka(świecidełko, krasnolud_zycie, mana_gracza, zdrowie_gracza)
        walka(świecidełko, krasnolud_zycie, mana_gracza, zdrowie_gracza)
        print("Musisz udać siędrogą 3")
        print("Dotarliśmy do groty smoka")
        walka(świecidełko, smok_zycie, mana_gracza, zdrowie_gracza)
        if zdrowie_gracza > 0:
            print("Udało ci się pokonać Smoka")
    elif nowy_wybór_ścieszki == 3:
        print("Dotarliśmy do groty smoka")
        walka(świecidełko, smok_zycie, mana_gracza, zdrowie_gracza)
        if zdrowie_gracza > 0:
            print("Udało ci się pokonać Smoka")
elif wybór_ścieszki == 2:
    print("Napotykasz 3 krasnoludy które cię atakują")
    walka(świecidełko, krasnolud_zycie, mana_gracza, zdrowie_gracza)
    walka(świecidełko, krasnolud_zycie, mana_gracza, zdrowie_gracza)
    walka(świecidełko, krasnolud_zycie, mana_gracza, zdrowie_gracza)
    nowy_wybór_ścieszki = int(input("Musisz wybrać inną trasę: "))
    if nowy_wybór_ścieszki == 1:
        print("znajdujesz na plaży Nimfę która wyzywa cie na pojedynek")
        walka(świecidełko, nimfa_zycie, mana_gracza, zdrowie_gracza)
        print("Musisz udać siędrogą 3")
        print("Dotarliśmy do groty smoka")
        walka(świecidełko, smok_zycie, mana_gracza, zdrowie_gracza)
        if zdrowie_gracza > 0:
            print("Udało ci się pokonać Smoka")
    elif nowy_wybór_ścieszki == 3:
        print("Dotarliśmy do groty smoka")
        walka(świecidełko, smok_zycie, mana_gracza, zdrowie_gracza)
        if zdrowie_gracza > 0:
            print("Udało ci się pokonać Smoka")
elif wybór_ścieszki == 3:
    print("Dotarliśmy do groty smoka")
    walka(świecidełko, smok_zycie, mana_gracza, zdrowie_gracza)
while zdrowie_gracza > 0 and smok_zycie < 0:
        print("Udało ci się pokonać Smoka")
