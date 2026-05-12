def erstelle_konto(startguthaben):
    guthaben=startguthaben
    def einzahlen(betrag):
        nonlocal guthaben
        guthaben = guthaben + betrag
    def auszahlen(betrag):
        nonlocal guthaben
        guthaben = guthaben - betrag
    def kontostand():
        return guthaben
    return einzahlen, auszahlen, kontostand
einzahlen, auszahlen, kontostand = erstelle_konto(100)
print(kontostand())   # 100
einzahlen(50)
print(kontostand())   # 150
auszahlen(20)
print(kontostand())   # 130
# Ein neues Konto erstellen, um zu zeigen, dass die Guthaben getrennt sind
einzahlen2, auszahlen2, kontostand2 = erstelle_konto(200)
print(kontostand2())  # 200
