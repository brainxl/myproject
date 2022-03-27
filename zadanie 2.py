class Timetable:
    def init(self, przystanek, odjazd_godzina, odjazd_minuty):
        self.przystanek = przystanek
        self.odjazd_godzina = odjazd_godzina
        self.odjazd_minuty = odjazd_minuty

Kurs1 = Timetable("Bierutów",11,50)
Kurs2 = Timetable("Oleśnica",12,10)

print("pociąg do", Kurs1.przystanek, "odjedzie o godzinie", Kurs1.odjazd_godzina, ":", Kurs1.odjazd_minuty)


class train:
    def init(self, numer_lini):
        self.numer_lini = numer_lini


autobus = train("14")
autobus = train("14")


class Passenger:
    def init(self, dane, numer_pasażera, ulgi):
        self.dane = dane
        self.numer_pasażera = numer_pasażera
        self.ulgi = ulgi


user1 = Passenger("Dawid", 157, "senior")
user2 = Passenger("Marta", 3, "student")
user3 = Passenger("Franio", 164, "brak")


class Ticket:
    def init(self, cena, ulga, cena_po_uldze):
        self.cena = cena
        self.ulga = ulga
        self.cena_po_uldze = cena_po_uldze


salle1 = Ticket("-50%", "senior", "15")
salle2 = Ticket("-25%", "studencki", "22zł")
salle3 = Ticket("0", "brak ulgi", "35zł")